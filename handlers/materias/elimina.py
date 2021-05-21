#coding: utf-8
#Nueva materia

import webapp2
import time

from webapp2_extras import jinja2

from model.materia import Materia



class EliminaMateriaHandler(webapp2.RequestHandler):
    def get(self):
        materia = Materia.recupera(self.request)
        materia.key.delete()
        time.sleep(1)
        return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/materias/elimina', EliminaMateriaHandler)
], debug=True)
