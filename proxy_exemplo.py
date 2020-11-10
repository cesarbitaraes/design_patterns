from abc import ABCMeta, abstractmethod


# Classe Client
class You:
    def __init__(self):
        print("You:: Lets buy the Denin shirt")
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        if self.is_purchased:
            print("You:: Wow! Denin shirt is mine :-)")
        else:
            print("You:: I should earn more :(")


# Classe Subjet, que é uma interface implementada pelo Proxy e por RealSubject
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# RealSubject
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        self.account = self.card    # Supõe-se que o número do cartão é o número da conta
        return self.account

    def __has_funds(self):
        print(f'Bank:: Checking if account {self.__get_account()} has enough funds')
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        if self.__has_funds():
            print(f'Bank:: Paying the merchant')
            return True
        else:
            print(f'Bank:: Sorry,not enough funds!')
            return False


# Classe Proxy, pois atua como substituto para o RealSubject, que é Bank
# O método pay_with_card internamento controla a criação do objeto RealSubject e apresenta
# os detalhes do cartão para Bank.
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number: ")
        self.bank.set_card(card)
        return self.bank.do_pay()


you = You()
you.make_payment()

# Os Proxies podem ajudar a melhorar o desempenho da aplicação ao fazer caching de objetos pesados
# ou, geralmente, de objetos acessados com frequência
# Os Proxies também autorizam o acesso ao RealSubject; portanto esse padrão auxilia na delegação
# somente se as permissões estiverem corretas
# Os Proxies remotos também facilitam a interação com servidores remotos, que podem funcionar como
# conexões de rede e de bancos de dados, além de poderem ser usados para monitorar sistemas
