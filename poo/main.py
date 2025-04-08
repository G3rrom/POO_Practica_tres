from CursoGrabado import CursoGrabado
from CursoPresenical import CursoPresencial
from CursoVirtual import CursoVirtual
from Estudiantes import Estudiantes

class Main():
    pepe = Estudiantes("Pepe", 1234567, "Jaime123")

    curso1 = CursoPresencial("5to 3ra", "Alan Uzal")
    curso2 = CursoGrabado("4to 2da", "Miguel Samela")
    curso3 = CursoVirtual("2do 1ra", "Fava")

    curso1.registrar_curso("5to 3ra", 123)
    curso2.registrar_curso("4to 2ra", 321)
    curso3.registrar_curso("2to 1ra", 987)

    curso1.agregar_estudiantes(pepe)
    curso2.agregar_estudiantes(pepe)
    curso3.agregar_estudiantes(pepe)

    curso1.calcular_interaccion()
    curso2.calcular_interaccion()
    curso3.calcular_interaccion()

    curso1.mostrar_info()
    curso2.mostrar_info()
    curso3.mostrar_info()
