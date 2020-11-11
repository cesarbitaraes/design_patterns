
# Sujeito
class NewPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latest_news = []

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__latest_news = news

    def get_news(self):
        return "Got news:", self.__latest_news


from abc import ABCMeta, abstractmethod


# Classe Observer
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


# Classe ConcreteObserver
class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


# Classe ConcreteObserver
class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


# Classe ConcreteObserver
class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == '__main__':
    news_publisher = NewPublisher()

    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.add_news("Hello world!")
    news_publisher.notify_subscribers()

    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscribers())

    news_publisher.add_news("My second news!")
    news_publisher.notify_subscribers()
