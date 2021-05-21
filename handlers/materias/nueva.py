#coding: utf-8
#Nueva materia

import webapp2
import time

from webapp2_extras import jinja2

from model.materia import Materia



class NuevaMateriaHandler(webapp2.RequestHandler):
    def get(self):
        materias = Materia.query().order(Materia.curso)

        valores_plantilla = {
            "materias": materias
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_materia.html",
        **valores_plantilla))


    def post(self):
        str_cuatri = self.request.get("cuatri", "")
        nombreMateria = self.request.get("nombreMateria", "")
        curso = self.request.get("curso", "")

        try:
            cuatri = int(str_cuatri)
        except ValueError:
            cuatri = -1

        if (cuatri < 0
            or  not(nombreMateria)
            or not(curso)):
                return self.redirect("/materias/nueva")
        else:

            materia = Materia(nombreMateria=nombreMateria, curso= curso, cuatri=cuatri)
            materia.put()
            time.sleep(1)
            return self.redirect("/")




app = webapp2.WSGIApplication([
    ('/materias/nueva', NuevaMateriaHandler)
], debug=True)
