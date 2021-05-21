#coding: utf-8
#Nuevo profesor

import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.materia import Materia

from model.profesor import Profesor



class NuevoProfesorHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "clave_materia": self.request.GET["mat"]

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_profesor.html",
            **valores_plantilla))


    def post(self):
        apellidos_profesor = self.request.get("apellidos_profesor", "")
        nombre_profesor = self.request.get("nombre_profesor", "")
        dni_profesor = self.request.get("dni_profesor", "")
        clave_materia = self.request.GET["mat"]

        if (not apellidos_profesor
            or not nombre_profesor
            or not dni_profesor):
                return self.redirect("/profesores/nuevo")
        else:

            profesor = Profesor(nombre_profesor=nombre_profesor,
                                apellidos_profesor= apellidos_profesor,
                                dni_profesor=dni_profesor,
                                clave_materia=ndb.Key(urlsafe=clave_materia))
            profesor.put()
            time.sleep(1)
            return self.redirect("/profesores/lista?mat="+ clave_materia)




app = webapp2.WSGIApplication([
    ('/profesores/nuevo', NuevoProfesorHandler)
], debug=True)
