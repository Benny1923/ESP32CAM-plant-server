from flask import Flask, request,jsonify,make_response,send_from_directory
from flask_restful import Resource
from model import *
import datetime, uuid
from esp32websocket import Esp32cmd

def toDate(dateString): 
    return datetime.datetime.strptime(dateString,"%Y-%m-%d-%H")#將date()去掉
class Index(Resource):
    def get(self):
        return send_from_directory('static/dist', 'index.html')
class Sendingjpg(Resource):
    def get(self, path):
        return send_from_directory('static/jpg', path)
class PhotoList(Resource):
    def get(self):
        limit = int(request.args.get('limit'))
        results = plant_photo.query.order_by((plant_photo.timestamp).desc()).limit(limit).all()
        photo_schema = PhotoSchema(many=True)
        photos = photo_schema.dump(results)
        return make_response(jsonify({"totoal":len(photos),"photos": photos}))
class Status(Resource):
    def get(self): 
        start = request.args.get('start')
        end = request.args.get('end')
        if (start==None or end==None):
            results = plant_status.query.order_by((plant_status.timestamp).desc()).all()#修改排序由高到低
        else:
            start = toDate(request.args.get('start'))
            end = toDate(request.args.get('end'))
            results = plant_status.query.order_by((plant_status.timestamp)).filter(plant_status.timestamp>=start,plant_status.timestamp<=end).all()#增加orderby
        status_schema = StatusSchema(many=True)
        status = status_schema.dump(results)
        return make_response(jsonify({"totoal":len(status), "logs": status, "online": Esp32cmd.isonline()}))
class Gif(Resource):
    def get(self):
        date = request.args.get('date')
        gif_schma = GifSchema(many=True)
        if (date==None):
            gif_results = plant_gif.query.order_by((plant_gif.timestamp).desc()).all()
        else:
            gif_results = plant_gif.query.filter(plant_gif.timestamp==date).all()
        gifs =  gif_schma.dump(gif_results)
        return make_response(jsonify({"gifs":gifs}))

#更新設定api
#欄位參考api文件 和 config-example.txt
class Esp32setting(Resource):
    def get(self):
        result = plant_automatic.query.all()
        setting_schema = AutomaticSchema(many=True)
        data = setting_schema.dump(result)
        return make_response(jsonify(data))
    def post(self):
        data = request.get_json()
        config = {}
        for m in data:
            name = m["module"]
            query = plant_automatic.query.filter_by(module=name).first()
            config[name+"-start"] = m["start"]
            query.start = m["start"]
            config[name+"-end"] = m["end"]
            query.end = m["end"]
            if "min" in m:
                config[name+"-min"] = int(m["min"])
                query.min = int(m["min"])
            if "max" in m:
                config[name+"-max"] = int(m["max"])
                query.max = int(m["max"])
            if "interval" in m:
                config[name+"-interval"] = int(m["interval"])
                query.cam_interval = int(m["interval"])
            if "nightmode" in m:
                config[name+"-nightmode"] = int(m["nightmode"])
                query.cam_nightmode = int(m["nightmode"])
            db.session.commit()
        Esp32cmd.updatecfg(config)
        return make_response(jsonify({"msg": "OK"}))
        

class Esp32manual(Resource):
    def get(self, device = "all"):
        op = request.args.get('op')
        if op == None:
            return make_response(jsonify({"msg":"Fail"}))
        Esp32cmd.manual(device, op)
        return make_response(jsonify({"msg":"OK"}))

class Uploadimg(Resource):
    def post(self):
        if request.files['img']:
            photoid = str(uuid.uuid1())
            file = request.files['img']
            file.save("static/jpg/"+photoid+".jpg")
            data = plant_photo(datetime.datetime.now(), photoid+".jpg")
            db.session.add(data)
            db.session.commit()
            return "OK"
        else:
            return "FAIL"