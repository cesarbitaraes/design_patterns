from abc import ABCMeta, abstractmethod


# Objeto Command
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


# Objeto ConcreteCommand
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


# Objeto ConcreteCommand
class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# Objeto Receiver
class StockTrade:
    def buy(self):
        print("You will buy stocks!")

    def sell(self):
        print("You will sell stocks!")


# Objeto Invoker
class Agent:
    def __init__(self):
        self.__order_queue = []

    def place_order(self, order):
        self.__order_queue.append(order)
        order.execute()


if __name__ == "__main__":
    # Cliente
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    # Chamador
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)