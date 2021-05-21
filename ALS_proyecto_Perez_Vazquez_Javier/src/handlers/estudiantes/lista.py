import webapp2
from webapp2_extras import jinja2

from model.materia import Materia
from model.estudiante import Estudiante

class ListaEstudiantesHandler(webapp2.RequestHandler):
    def get(self):
        materia, estudiantes = Estudiante.recupera(self.request)


        valores_plantilla = {
            "estudiantes": estudiantes,
            "materia": materia
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_estudiantes.html",
            **valores_plantilla))





app = webapp2.WSGIApplication([
    ('/estudiantes/lista', ListaEstudiantesHandler)
], debug=True)
