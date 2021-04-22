from flask import Flask, request,jsonify,make_response,send_from_directory
from flask_restful import Resource
from model import *
import datetime
def toDate(dateString): 
    return datetime.datetime.strptime(dateString,"%Y-%m-%d-%H").date()
class Index(Resource):
    def get(self):
        return send_from_directory('static/dist', 'index.html')
class Sendingjpg(Resource):
    def get(path):
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
            results = plant_status.query.all()
        else:
            start = toDate(request.args.get('start'))
            end = toDate(request.args.get('end'))
            results = plant_status.query.filter(plant_status.timestamp>=start,plant_status.timestamp<=end).all()
        status_schema = StatusSchema(many=True)
        status = status_schema.dump(results)
        return make_response(jsonify({"totoal":len(status), "logs": status}))
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