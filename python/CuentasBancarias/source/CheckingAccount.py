from AccountMovement import AccountMovement


class CheckingAccount:
    def __init__(self):
        self._movements = []
        self._balance = 0 #pesos

    def balance(self):
        balance = 0
        for movement in self._movements:
            balance += movement.amount()
        return balance

    def deposit(self, an_amount_of_money):
        self._movements.append(AccountMovement(an_amount_of_money))

    def withdraw(self, an_amount_of_money):
        self._movements.append(AccountMovement(- an_amount_of_money))

    
