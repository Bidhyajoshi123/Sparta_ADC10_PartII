# Generated by Django 3.0.1 on 2020-01-23 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BankingApp', '0002_account_branch_depositor_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='date',
            new_name='Amount',
        ),
    ]