import Evento

class TrabajoPractico(Evento.Evento):
    def __init__(self, fecha, descripcion, materia, entrega):
        super().__init__(fecha, descripcion)
        self.materia = materia
        self.entrega = entrega

    def __str__(self):
        return f'{super().__str__()}, Materia: {self.materia}, Entrega: {self.entrega}'