import sqlite3


class MetaSingleton(type):
    _instances = {}

    # O método especial __call__ é chamado quando um objeto precisa ser criado para uma
    # classe já existente. Sempre que o objeto for chamado esse método será executado.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


db1 = Database().connect()
db2 = Database().connect()

print(f'Database object DB1: {db1}')
print(f'Database object DB2: {db2}')
