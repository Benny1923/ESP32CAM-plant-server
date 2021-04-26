from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
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
    lux = db.Column(db.Integer)
    def __init__(self, timestamp, moisture,tankfluid,lux):
        self.timestamp = timestamp
        self.moisture = moisture
        self.tankfluid = tankfluid
        self.lux = lux
class plant_gif(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Date, unique=True)
    filename = db.Column(db.String(100))
    def __init__(self, timestamp, filename):
        self.timestamp = timestamp
        self.filename = filename
class plant_message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Date, unique=True)
    message = db.Column(db.String(100))
    def __init__ (self, timestamp, message):
        self.timestamp = timestamp
        self.message = message
class plant_automatic(db.Model):
    module = db.Column(db.String(100),primary_key=True)
    start = db.Column(db.String(100))
    end = db.Column(db.String(100))
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
    cam_nightmode = db.Column(db.Integer)
    cam_interval = db.Column(db.Integer)
    def __init__ (self, module, start, end, min=None, max=None, nightmode=None, interval=None):
        self.module = module
        self.start = start
        self.end = end,
        self.min = min
        self.max = max
        self.cam_nightmode = nightmode
        self.cam_interval = interval
class PhotoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp', 'filename')
class StatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp', 'moisture','tankfluid','lux')
class GifSchema(ma.Schema):
    class Meta:
        fields = ('id', 'timestamp','filename')
class AutomaticSchema(ma.Schema):
    class Meta:
        fields = ("module", "start", "end", "min", "max", "nightmode", "interval")
    nightmode = fields.fields.Number(attribute="cam_nightmode")
    interval = fields.fields.Number(attribute="cam_interval")