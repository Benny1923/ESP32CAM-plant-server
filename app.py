from _init_ import app,db,api
from geventwebsocket import WebSocketServer, Resource
from esp32websocket import Esp32conns
from route import Index,Sendingjpg,PhotoList,Status,Gif,Uploadimg,Esp32setting,Esp32manual
from flask_cors import CORS
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://plant:plant@localhost/plant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.create_all()
api.add_resource(Index,'/')

#api路由，參見開會api文件
api.add_resource(Sendingjpg,'/api/photos/<path:path>')
api.add_resource(PhotoList,'/api/photos/list')
api.add_resource(Status,'/api/status')
api.add_resource(Gif,'/api/photos/gif')
api.add_resource(Esp32setting, '/api/setting')
api.add_resource(Esp32manual, '/api/manual', endpoint="manua")
api.add_resource(Esp32manual, '/api/manual/<string:device>', endpoint="manual")
api.add_resource(Uploadimg, '/api/ESP32/saveimg')

if __name__ == "__main__":
    server = WebSocketServer(("0.0.0.0", 8080), Resource([
        ('^/websocket', Esp32conns),
        ('^/.*', app)
    ]))
    server.serve_forever()