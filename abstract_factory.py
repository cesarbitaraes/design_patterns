# O objetivo principal do padrão Abstract Factory é fornecer uma interface para criar
# famílias de objetos relacionados sem especificar a classe concreta.

from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def create_veg_pizza(self):
        return MexVeggiePizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VeggiePizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, veggie_pizza):
        pass


class NonVeggiePizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veggie_pizza):
        pass


class DeluxVeggiePizza(VeggiePizza):
    def prepare(self, veggie_pizza):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVeggiePizza):
    def serve(self, veggie_pizza):
        print(type(self).__name__, "is served with Chicken on ", type(veggie_pizza).__name__)


class MexVeggiePizza(VeggiePizza):
    def prepare(self, veggie_pizza):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVeggiePizza):
    def serve(self, veggie_pizza):
        print(type(self).__name__, " is served with Ham on ", type(veggie_pizza).__name__)


class PizzaStore:
    def __init__(self):
        pass

    def make_pizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.NonVeggiePizza = self.factory.create_non_veg_pizza()
            self.VeggiePizza = self.factory.create_veg_pizza()
            self.VeggiePizza.prepare(self.NonVeggiePizza)
            self.NonVeggiePizza.serve(self.VeggiePizza)


pizza = PizzaStore()
pizza.make_pizzas()