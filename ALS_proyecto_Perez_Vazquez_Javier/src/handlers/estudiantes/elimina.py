#coding: utf-8


import webapp2
import time

from webapp2_extras import jinja2

from model.estudiante import Estudiante



class EliminaEstudiantesHandler(webapp2.RequestHandler):
    def get(self):
        estudiante = Estudiante.recupera_del(self.request)
        estudiante.key.delete()
        time.sleep(1)
        return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/estudiantes/elimina', EliminaEstudiantesHandler)
], debug=True)
