# Padrão de criação.
# Singleton é usado quando precisamos ter apenas um objeto de uma determinada classe.

class Singleton(object):

    # Método especial para instanciar objetos.
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(f'Object created', s)

s1 = Singleton()
print(f'Object created', s1)
