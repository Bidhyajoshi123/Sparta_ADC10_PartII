from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    account_no = models.IntegerField()
    contact_no = models.IntegerField()
    
    def __str__(self):
        return f"self.firstname + " " + self.lastname + " " + self.account_no + " " + self.contact_no "

    def valid_customer_name(self):
        return self.firstname!="" and self.lastname!=""   

    def valid_customer_account_no(self):
        return self.account_no!=""     
 

class Depositor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

    def valid_depositor_name(self):
        return self.name!=""    
            

class Branch(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

class Transaction(models.Model):
    Amount = models.IntegerField()

    def __str__(self):
        return f"self.amount"  

    

class Account(models.Model):
    accountholder = models.CharField(max_length=50)
    depositors = models.ManyToManyField(Depositor)
    branchs = models.ForeignKey(Branch, on_delete=models.CASCADE)
    transactions = models.ForeignKey(Transaction,  on_delete=models.CASCADE)
    customers = models.ForeignKey(Customer,  on_delete=models.CASCADE)

    def __str__(self):
        return self.accountholder

    def valid_Account_accountholder(self):
        return self.accountholder!=""




