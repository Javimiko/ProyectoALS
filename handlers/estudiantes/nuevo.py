#coding: utf-8
#Nuevo estudiante

import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.ext import ndb

from model.materia import Materia

from model.estudiante import Estudiante



class NuevoEstudianteHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "clave_materia": self.request.GET["mat"]

        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_estudiante.html",
            **valores_plantilla))


    def post(self):
        apellidos_estudiante = self.request.get("apellidos_estudiante", "")
        nombre_estudiante = self.request.get("nombre_estudiante", "")
        dni_estudiante = self.request.get("dni_estudiante", "")
        clave_materia = self.request.GET["mat"]

        if (not apellidos_estudiante
            or not nombre_estudiante
            or not dni_estudiante):
                return self.redirect("/estudiantes/nuevo")
        else:

            estudiante = Estudiante(nombre_estudiante=nombre_estudiante,
                                apellidos_estudiante= apellidos_estudiante,
                                dni_estudiante=dni_estudiante,
                                clave_materia=ndb.Key(urlsafe=clave_materia))
            estudiante.put()
            time.sleep(1)
            return self.redirect("/estudiantes/lista?mat="+ clave_materia)




app = webapp2.WSGIApplication([
    ('/estudiantes/nuevo', NuevoEstudianteHandler)
], debug=True)
