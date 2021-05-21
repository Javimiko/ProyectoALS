#coding: utf-8


import webapp2
import time

from webapp2_extras import jinja2

from model.profesor import Profesor



class EliminaProfesorHandler(webapp2.RequestHandler):
    def get(self):
        profesor = Profesor.recupera_del(self.request)
        profesor.key.delete()
        time.sleep(1)
        return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/profesores/elimina', EliminaProfesorHandler)
], debug=True)
