from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_firstname = models.CharField(max_length=100)
    customer_lastname = models.CharField(max_length=100)
    customer_account_no = models.IntegerField(blank=True, null=True)
    customer_contact_no = models.IntegerField(blank=True, null=True)

def __str__(self):
    return f"self.firstname + " " + self.lastname + " " + self.account_no + " " + self.contact_no "
