from pymongo import MongoClient
from PIL import Image
import io

uri = "mongodb://vagrant:vagrant@localhost:27017/admin"

client = MongoClient(uri)
db = client.db
images = db.images

im = Image.open('home/vagrant/visualise/graph.png')

image_bytes = io.BytesIO()
im.save(image_bytes, format='JPEG')

image = {
    'data': image_bytes.getvalue()
}

image_id = images.insert_one(image).inserted_id