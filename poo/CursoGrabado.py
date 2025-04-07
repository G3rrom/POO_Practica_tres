from Curso import Curso
class CursoGrabado(Curso):
    def __init__(self, nombre, prof_cargo, interaccion = "Baja"):
        super().__init__(nombre, prof_cargo, interaccion)
        self.est_ins = []