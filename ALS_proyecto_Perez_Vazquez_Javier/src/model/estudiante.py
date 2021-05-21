#Estudiante perteneciente a la academia

from google.appengine.ext import ndb
from materia import Materia

class Estudiante(ndb.Model):
    dni_estudiante = ndb.StringProperty()
    nombre_estudiante = ndb.StringProperty()
    apellidos_estudiante = ndb.StringProperty()
    clave_materia = ndb.KeyProperty(kind=Materia)


    @staticmethod
    def recupera(req):
        try:
            id_mat = req.GET["mat"]

        except KeyError:
            is_mat = ""

        if id_mat:
            clave_materia = ndb.Key(urlsafe=id_mat)
            estudiantes = Estudiante.query(Estudiante.clave_materia == clave_materia)
            return (clave_materia.get(), estudiantes)
        else:
            print("ERROR: materia no existente")


    @staticmethod
    def recupera_del(req):
        try:
            id= req.GET["id"]

        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()