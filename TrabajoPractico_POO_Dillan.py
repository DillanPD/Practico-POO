class Event:
    def __init__(self, date, description):
        self.date = date
        self.description = description

    def __str__(self):
        return f"Evento: {self.description}, Fecha: {self.date}"

class Exam(Event):
    def __init__(self, date, description, subject):
        super().__init__(date, description)
        self.subject = subject

    def __str__(self):
        return f"Examen: {self.description}, Fecha: {self.date}, Asignatura: {self.subject}"

class PracticalWork(Event):
    def __init__(self, date, description, subject):
        super().__init__(date, description)
        self.subject = subject

    def __str__(self):
        return f"Trabajo Práctico: {self.description}, Fecha: {self.date}, Asignatura: {self.subject}"

class StudyGroup(Event):
    def __init__(self, date, description, subject):
        super().__init__(date, description)
        self.subject = subject

    def __str__(self):
        return f"Reunión de Estudio: {self.description}, Fecha: {self.date}, Asignatura: {self.subject}"

class Agenda:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def show_events(self):
        for event in self.events:
            print(event)

class User:
    def __init__(self, name):
        self.name = name
        self.agenda = Agenda()

    def add_event(self, event):
        self.agenda.add_event(event)

    def show_agenda(self):
        self.agenda.show_events()

# Ejemplo de uso
user = User("Juan")
user.add_event(Exam("2023-03-15", "Examen de Matemáticas", "Matemáticas"))
user.add_event(PracticalWork("2023-03-20", "Trabajo Práctico de Programación", "Programación"))
user.show_agenda()