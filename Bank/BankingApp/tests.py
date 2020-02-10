from django.test import TestCase
from .models import Customer , Depositor, Transaction, Account, Branch

# Create your tests here.

class ModelTestCase(TestCase):

    def test_valid_customer_name(self):
        cus1=Customer(firstname="Karlosh",lastname="Rai",account_no="456123789",contact_no="9813106759")
        self.assertEqual(cus1.valid_customer_name(),True)

    def test_valid_customer_account_no(self):
        cus1=Customer(firstname="karlosh",lastname="Rai",account_no="478965123",contact_no="9803274007")
        self.assertTrue(cus1.valid_customer_account_no()) 

    def test_valid_depositor_name(self):
        dep1=Depositor(name="Anish")
        self.assertEqual(dep1.valid_depositor_name(),True)

    def test_valid_Account_accountholder(self):
        a1=Account(accountholder="Anish")
        self.assertEqual(a1.valid_Account_accountholder(),True)


    

            

    




    
   





