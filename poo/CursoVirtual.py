from Curso import Curso
class CursoVirtual(Curso):
    def __init__(self, nombre, prof_cargo, interaccion = "Media"):
        super().__init__(nombre, prof_cargo, interaccion)
        self.est_ins = []