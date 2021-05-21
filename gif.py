from os import listdir, path
from _init_ import app, db
import imageio
from model import plant_photo, plant_gif
import datetime, time, uuid

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://plant:plant@localhost/plant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.create_all()

today = datetime.datetime.now().strftime("%Y-%m-%d")

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def make_gif():
    result = plant_photo.query.filter(plant_photo.timestamp >= yesterday, plant_photo.timestamp < today).all()
    path_list = [f.filename for f in result]
    gif_images = []
    for f in path_list:
        gif_images.append(imageio.imread("static/jpg/"+f))
    gifid = str(uuid.uuid1())
    imageio.mimsave("static/gif/"+gifid+".gif", gif_images, fps=24)
    data = plant_gif(yesterday, gifid+".gif")
    db.session.add(data)
    db.session.commit()
    return

while True:
    if (today != datetime.datetime.now().strftime("%Y-%m-%d")):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        make_gif()
    time.sleep(60)
