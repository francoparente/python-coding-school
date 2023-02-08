import unittest

from CheckingAccount import CheckingAccount


class CuentasBancariasTest(unittest.TestCase):
    def test_initial_balance_of_a_checking_account_is_zero_pesos(self):
        a_checking_account = CheckingAccount()
        
        self.assertEqual(0, a_checking_account.balance()) #pesos

    def test_when_depositing_an_amount_of_money_the_balance_is_incremented_in_that_amount(self):
        a_checking_account = CheckingAccount()
        a_checking_account.deposit(1000) #pesos

        self.assertEqual(1000, a_checking_account.balance()) #pesos

    def test_when_withdrawing_an_amount_of_money_the_balance_is_decremented_in_that_amount(self):
        a_checking_account = CheckingAccount()
        a_checking_account.deposit(1000) #pesos
        a_checking_account.withdraw(600) #pesos

        self.assertEqual(400, a_checking_account.balance()) #pesos


if __name__ == '__main__':
    unittest.main()
