import Evento

class Examen(Evento.Evento):
    def __init__(self, fecha, descripcion, materia):
        super().__init__(fecha, descripcion)
        self.materia = materia

    def __str__(self):
        return f'{super().__str__()}, Materia: {self.materia}'