from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
import io
import matplotlib as plt

uri = "mongodb://vagrant:vagrant@localhost:27017/admin"

client = MongoClient(uri)
db = client.db
images = db.images
image = images.find_one()

pil_img = Image.open(io.BytesIO(image['data']))
plt.imshow(pil_img)
plt.savefig('./www/graph.png')