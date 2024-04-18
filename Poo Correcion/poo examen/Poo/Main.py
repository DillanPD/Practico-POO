import Agenda


def mostrar_menu():
    print('1. Agregar evento')
    print('2. Eliminar evento')
    print('3. Mostrar eventos')
    print('4. Salir')
def agregar_evento():
    fecha = input('Ingrese la fecha del evento: ')
    descripcion = input('Ingrese la descripción del evento: ')
    materia = input('Ingrese la materia del evento: ')

    evento = Agenda.Examen(fecha, descripcion, materia) if materia else Agenda.TrabajoPractico(fecha, descripcion, materia) if materia else Agenda.ReunionEstudio(fecha, descripcion)

    agenda.agregar_evento(evento)
def eliminar_evento():
    descripcion = input('Ingrese la descripción del evento a eliminar: ')
    agenda.eliminar_evento(descripcion)
def mostrar_eventos():
    print('Eventos en la agenda:')
    agenda.mostrar_eventos()
  

agenda = Agenda.Agenda()

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