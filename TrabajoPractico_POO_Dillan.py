class Evento:
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f'Fecha: {self.fecha}, Descripción: {self.descripcion}'
    
class Examen(Evento):
    def __init__(self, fecha, descripcion, materia):
        super().__init__(fecha, descripcion)
        self.materia = materia

    def __str__(self):
        return f'{super().__str__()}, Materia: {self.materia}'

class TrabajoPractico(Evento):
    def __init__(self, fecha, descripcion, materia, entrega):
        super().__init__(fecha, descripcion)
        self.materia = materia
        self.entrega = entrega

    def __str__(self):
        return f'{super().__str__()}, Materia: {self.materia}, Entrega: {self.entrega}'

class ReunionEstudio(Evento):
    def __init__(self, fecha, descripcion, lugar):
        super().__init__(fecha, descripcion)
        self.lugar = lugar

    def __str__(self):
        return f'{super().__str__()}, Lugar: {self.lugar}'
    
class Agenda:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def mostrar_eventos(self):
        for evento in self.eventos:
            print(evento)

    def eliminar_evento(self, descripcion):
        self.eventos = [evento for evento in self.eventos if evento.descripcion != descripcion]


def mostrar_menu():
    print('1. Agregar evento')
    print('2. Eliminar evento')
    print('3. Mostrar eventos')
    print('4. Salir')

def agregar_evento():
    fecha = input('Ingrese la fecha del evento: ')
    descripcion = input('Ingrese la descripción del evento: ')
    materia = input('Ingrese la materia del evento (si aplica): ')
    entrega = input('Ingrese la fecha de entrega del evento (si aplica): ')
    lugar = input('Ingrese el lugar del evento (si aplica): ')

    evento = Examen(fecha, descripcion, materia) if materia else TrabajoPractico(fecha, descripcion, materia, entrega) if entrega else ReunionEstudio(fecha, descripcion, lugar)

    agenda.agregar_evento(evento)

def eliminar_evento():
    descripcion = input('Ingrese la descripción del evento a eliminar: ')
    agenda.eliminar_evento(descripcion)

def mostrar_eventos():
    print('Eventos en la agenda:')
    agenda.mostrar_eventos()

if __name__ == '__main__':
    agenda = Agenda()

    while True:
        mostrar_menu()
        opcion = int(input('Seleccione una opción: '))

        if opcion == 1:
            agregar_evento()
        elif opcion == 2:
            eliminar_evento()
        elif opcion == 3:
            mostrar_eventos()
        elif opcion == 4:
            break
        else:
            print('Opción inválida. Intente nuevamente.')
