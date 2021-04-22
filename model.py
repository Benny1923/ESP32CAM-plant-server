from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from _init_ import app,db,ma
class plant_photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, unique=True)
    filename = db.Column(db.String(100))
    def __init__(self, timestamp, filename):
        self.timestamp = timestamp
        self.filename = filename
class plant_status(db.Model):
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
    timestamp = db.Column(db.Date, unique=True)
    filename = db.Column(db.String(100))
    def __init__(self, timestamp, moisture,tankfluid,online):
        self.timestamp = timestamp
        self.filename = filename   
class PhotoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp', 'filename')
class StatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp', 'moisture','tankfluid','online')
class GifSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp','filename')