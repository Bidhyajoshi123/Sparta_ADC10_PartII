# Generated by Django 3.0.1 on 2020-01-23 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BankingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Depositor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountholder', models.CharField(max_length=50)),
                ('branchs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankingApp.Branch')),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankingApp.Customer')),
                ('depositors', models.ManyToManyField(to='BankingApp.Depositor')),
                ('transactions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankingApp.Transaction')),
            ],
        ),
    ]