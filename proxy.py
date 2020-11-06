# Padrão de projeto estrutural.
# O principal propósito do padrão Proxy é oferecer um substituto ou um placeholder
# para outro objeto a fim de controlar o acesso a um objeto real.

class Actor(object):
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(type(self).__name__, "is occupied with current movie.")

    def available(self):
        self.is_busy = False
        print(type(self).__name__, "is free for the movie.")

    def get_status(self):
        return self.is_busy


# Classe Proxy
class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
