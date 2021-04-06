import os, time
from geventwebsocket import WebSocketServer, WebSocketError, WebSocketApplication, Resource
from flask import Flask, request, render_template, abort ,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/plant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
#esp32 last reponse time
lastresponse = time.time()

client = None
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))
    def __init__(self, title, description):
        self.title = title
        self.description = description
db.create_all()
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
@app.route('/tasks', methods=['GET'])
def get_tasks():
  all_tasks = Task.query.all()
  result = tasks_schema.dump(all_tasks)
  return jsonify(result)

@app.route('/')
def index():
    return "Hello nothing there"

@app.route('/api/status')
def isonline():
    global lastresponse
    if ((time.time() - lastresponse) < 5):
        return "online"
    else:
        return "offline"

@app.route('/api/manual')
def all_manual():
    op = request.args.get('op')
    if (op == None):
        return "error"
    client.ws.send("hello")
    return "nuke code sended"

@app.route('/api/manual/<string:device>')
def manual(device):
    op = request.args.get('op')
    if (op == None):
        return "error"
    if (device == "sprinklers"):
        pass
    elif (device == "light"):
        pass
    return "nuke code sended"

@app.route('/api/ESP32/saveimg', methods=['POST'])
def saveimg():
    if request.files['img']:
        file = request.files['img']
        file.save(file.filename)
        print("saveimg: {}".format(file.filename))
        return "OK"
    else:
        return "FAIL"

class ChatApplication(WebSocketApplication):
    def on_open(self):
        global lastresponse
        print("client connected!")
        lastresponse = time.time()
    def on_message(self, message):
        global lastresponse
        global client
        client = self
        if (message not in "pong"):
            print("message received!")
            print(message)
        lastresponse = time.time()
    def on_close(self, reason):
        print("Connection closed!")


if __name__ == '__main__':
    server = WebSocketServer(("0.0.0.0", 8080), Resource([
        ('^/websocket', ChatApplication),
        ('^/.*', app)
    ]))
    server.serve_forever()