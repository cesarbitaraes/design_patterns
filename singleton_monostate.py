class Borg:
    __shared_state = {"1": "2"}

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass


b = Borg()
b1 = Borg()
b1.x = 4

print(f'Borg object b: {b}')
print(f'Borg object b1: {b1}')
print(f'Borg state b: {b.__dict__}')
print(f'Borg state b1: {b1.__dict__}')
