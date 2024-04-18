import Evento

class ReunionEstudio(Evento.Evento):
    def __init__(self, fecha, descripcion, lugar):
        super().__init__(fecha, descripcion)
        self.lugar = lugar

    def __str__(self):
        return f'{super().__str__()}, Lugar: {self.lugar}'