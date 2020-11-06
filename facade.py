# Padrão de projeto estrutural.
# Enquanto os padrões Classe descrevem abstrações com a ajuda de herança e oferecem uma interface
# e oferecem uma interface de programação mais conveniente, o padrão Objeto descreve como os
# objetos podem ser associados e compostos para formar objetos maiores. Os padrões estruturais
# são uma combinação dos padrões Classe e Objeto.
# O Façade oculta as complexidades do sistema interno e oferece uma interface ao cliente para
# que este possa acessar o sistema de forma bem simplificada.
# Princípio do conhecimento mínimo, que nos orienta no sentido de reduzir as interações entre
# os objetos a apenas alguns "amigos" que sejam próximos a você.

# Classe Façade
# EventManager usa composição para criar objetos de susbistemas como Hotelier, Caterer e
# outros.
class EventManager(object):
    def __init__(self):
        print(f'Event Manager:: Let me talk to the folks!\n')

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.caterer = Caterer()
        self.caterer.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


# Sistema
class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for marriage? --")

    def __is_available(self):
        print("Is this Hotel free for the event on given day?")
        return True

    def book_hotel(self):
        if self.__is_available():
            print("Registered the Booking\n\n")


# Sistema
class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")

    def set_flower_requirements(self):
        print("Carnations, Roses and Lillies would be used for Decoration\n\n")


# Sistema
class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")

    def set_cuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")


# Sistema
class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")

    def set_music_type(self):
        print("Jazz and Classical will be played\n\n")


# Cliente
class You(object):
    def __init__(self):
        print("You:: Whoa! Marriage arrangements??!!")

    def ask_event_manager(self):
        print("You:: Let's contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    # __del__ is a finalizer. It is called when an object is garbage collected which
    # happens at some point after all references to the object have been deleted.
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")


you = You()
you.ask_event_manager()
