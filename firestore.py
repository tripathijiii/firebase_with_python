import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore,storage

cred = credentials.Certificate("/Users/shashwateshtripathi/Desktop/django_firebase/firebase_django/firebase_app/serviceaccountkey.json")
firebase_admin.initialize_app(cred,{'storageBucket' : 'flutterboardapp-1aaff.appspot.com' })
db = firestore.client()
def fetch_user_data(name):
    for obj in db.collection('users').get():
        if obj.to_dict()['name']==name:
            return obj.to_dict()
    return -1

def uploadingImage(filepath):
    bucket = storage.bucket()
    blob = bucket.blob(filepath)
    blob.upload_from_filename(filepath)
    blob.make_public()
    print(blob.public_url)

uploadingImage("/Users/shashwateshtripathi/Spects.jpeg")