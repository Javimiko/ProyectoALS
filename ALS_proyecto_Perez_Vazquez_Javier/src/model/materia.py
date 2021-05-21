#Clase perteneciente a un determinado curso

from google.appengine.ext import ndb


class Materia(ndb.Model):
    cuatri = ndb.IntegerProperty()
    curso = ndb.StringProperty()
    nombreMateria = ndb.StringProperty()

    @staticmethod
    def recupera(req):
        try:
            id= req.GET["id"]

        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()