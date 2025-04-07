from Curso import Curso
class CursoPresencial(Curso):
    def __init__(self, nombre, prof_cargo, interaccion = "Alta"):
        super().__init__(nombre, prof_cargo, interaccion)
        self.est_ins = []
