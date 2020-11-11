# Padrão comportamental, que tem como foco as responsabilidades de um objeto
# Baixo acoplamento
# Cenário em que um serviço dependente monitora mudanças de estado no serviço básico
# Define uma dependência de um para muitos, de modo que qualquer mudança em um objeto
# será notificada as demais objetos dependentes automaticamente
# Encapsula o componente nucler, isto é, o Sujeito

class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notify_all('notification')