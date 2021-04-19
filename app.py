from flask import Flask, request, render_template, abort ,jsonify,make_response,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__,static_url_path='/',static_folder='./static/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/plant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, unique=True)
    filename = db.Column(db.String(100))
    def __init__(self, timestamp, filename):
        self.timestamp = timestamp
        self.filename = filename
class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime,unique=True)
    moisture = db.Column(db.Integer)
    tankfluid = db.Column(db.Integer)
    online = db.Column(db.Boolean)
    def __init__(self, timestamp, moisture,tankfluid,online):
        self.timestamp = timestamp
        self.moisture = moisture
        self.tankfluid = tankfluid
        self.online=online
class plant_gif(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, unique=True)
    filename = db.Column(db.String(100))
    def __init__(self, timestamp, moisture,tankfluid,online):
        self.timestamp = timestamp
        self.filename = filename   
db.create_all()

class PhotoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp', 'filename')
class StatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp', 'moisture','tankfluid','online')
class GifSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp','filename')
@app.route('/')
def indexhtm():
    return send_from_directory('static/dist', 'index.html')
@app.route('/api/photos/<path:path>')
def sendjpg(path):
    return send_from_directory('static/jpg', path)

@app.route('/api/photos/list', methods=['GET'])
def get_photos():
    page = int(request.args.get('page'))
    limit = int(request.args.get('limit'))
    #page選擇頁數 per_page每頁有幾筆資料
    results = Photo.query.order_by((Photo.timestamp).desc()).paginate(page, per_page=limit, error_out=False)
    #假如有下一頁hasnext = True
    if results.has_next:
        hasnext = True
    else:
        hasnext = False
    photo_schema = PhotoSchema(many=True)
    photos = photo_schema.dump(results.items)
    return make_response(jsonify({"totoal":len(photos),"hasnext":hasnext,"photos": photos}))
#format日期格式

def toDate(dateString): 
    return datetime.datetime.strptime(dateString,"%Y-%m-%d-%H").date()
@app.route('/api/status', methods=['GET'])
def get_histroy(): 
    start = request.args.get('start')
    end = request.args.get('end')
    if (start==None or end==None):
        results = Status.query.all()
    else:
        start = toDate(request.args.get('start'))
        end = toDate(request.args.get('end'))
        results = Status.query.filter(Status.timestamp>=start,Status.timestamp<=end).all()
    status_schema = StatusSchema(many=True)
    status = status_schema.dump(results)
    return make_response(jsonify({"totoal":len(status), "logs": status}))
#format日期格式
def toDates(dateString): 
    return datetime.datetime.strptime(dateString,"%Y-%m-%d").date()
@app.route('/api/photos/gif',methods=['GET'])
def get_gif():
    date = request.args.get('date')
    gif_schma = GifSchema(many=True)
    if (date==None):
    plant_gif.query.all()
    else:
        date = toDates(request.args.get('date'))
        gif_results = plant_gif.query.filter(plant_gif.timestamp==date).all()
    gifs =  gif_schma.dump(gif_results)
    return make_response(jsonify({"gifs":gifs}))

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False) 