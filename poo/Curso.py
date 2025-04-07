class Curso():
    def __init__(self, nombre, prof_cargo, interaccion):
        self.nombre = nombre
        self.profe_cargo = prof_cargo
        self.interaccion = interaccion
        self.est_ins = []
        self.cursos_total = {}

    def registrar_curso(self, curso_particular, uc):
        self.cursos_total[curso_particular] = uc
        print("Curso registrado.")

    def mostrar_info(self):
        print(f"Curso: {self.nombre} | Numero de estudiantes: {self.est_ins} | Nivel de interaccion: {self.interaccion}")

    def agregar_estudiantes(self, estudiante):
        self.est_ins.append(estudiante)
        print("Alumno agregado.")

    def calcular_interaccion (self):
        if len(self.est_ins) > 10:
            if self.interaccion == "Alta":
                self.interaccion = "Muy alta"
                print(f"La interaccion subio a {self.interaccion}")
            elif self.interaccion == "Media":
                self.interaccion = "Alta"
                print(f"La interaccion subio a {self.interaccion}")
            elif self.interaccion == "Baja":
                self.interaccion = "Media"
                print(f"La interaccion subio a {self.interaccion}")
        else:
            print("No se modifica la interaccion.")
            print(f"Interaccion actual: {self.interaccion}")
    
    


 
