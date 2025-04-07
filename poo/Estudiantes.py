class Estudiantes():
    def __init__(self, nom, dni, correo):
        self.nom = nom 
        self.__dni = dni 
        self.corre = correo 
    def get_dni(self):
        return self.__dni
    def set_dni(self, nuevo_dni):
        if isinstance(nuevo_dni, int):
            self.__dni = nuevo_dni
        else: 
            raise ValueError("ERROR")
    
    

        