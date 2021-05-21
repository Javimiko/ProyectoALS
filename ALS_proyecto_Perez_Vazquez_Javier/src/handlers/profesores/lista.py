import webapp2
from webapp2_extras import jinja2

from model.materia import Materia
from model.profesor import Profesor

class ListaProfesoresHandler(webapp2.RequestHandler):
    def get(self):
        materia, profesores = Profesor.recupera(self.request)


        valores_plantilla = {
            "profesores": profesores,
            "materia": materia
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("lista_profesores.html",
            **valores_plantilla))





app = webapp2.WSGIApplication([
    ('/profesores/lista', ListaProfesoresHandler)
], debug=True)
