#Profesor perteneciente a la academia

from google.appengine.ext import ndb

from materia import Materia

class Profesor(ndb.Model):
    dni_profesor = ndb.StringProperty()
    clave_materia = ndb.KeyProperty(kind=Materia)
    nombre_profesor = ndb.StringProperty()
    apellidos_profesor = ndb.StringProperty()


    @staticmethod
    def recupera(req):
        try:
            id_mat= req.GET["mat"]

        except KeyError:
            is_mat = ""

        if id_mat:
            clave_materia = ndb.Key(urlsafe=id_mat)
            profesores = Profesor.query(Profesor.clave_materia == clave_materia)
            return (clave_materia.get(), profesores)
        else:
            print("ERROR: materia no existente")


    @staticmethod
    def recupera_del(req):
        try:
            id= req.GET["id"]

        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()