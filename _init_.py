from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
app = Flask(__name__,static_url_path='/',static_folder='./static/dist')
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)