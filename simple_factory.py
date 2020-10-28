# Padrão de criação.
# Padrão mais usado.
# Ajuda a criar objetos de tipos diferentes em vez de objetos serem diretamente instanciados.
# Permite que as interfaces criem objetos sem expor a lógica de sua criação.

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


# Fábrica forest definida
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


# Código cliente
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound: Dog or Cat? ")
    ff.make_sound(animal)
