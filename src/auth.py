import firebase_admin as fa

from firebase_admin import credentials
from firebase_admin import db


class FirebaseAuth:

    credurl = 'path2Json/jsonfile.json'
    dburl = 'http://link.url/'

    def initialisedb(self,):
        cred = credentials.Certificate(self.credurl)
        fa.initialize_app(cred, {'databaseURL': self.dburl})

    # Creating object
    def createdb(self, childname=None):
        ref = db.reference()
        root = ref.child(childname)
        return root

