from _init_ import app,db,api
from route import Index,Sendingjpg,PhotoList,Status,Gif
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/plant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.create_all()
api.add_resource(Index),'/')
api.add_resource(Sendingjpg,'/api/photos/<path:path>')
api.add_resource(PhotoList,'/api/photos/list')
api.add_resource(Status,'/api/status')
api.add_resource(Gif,'/api/photos/gif')
if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False) 