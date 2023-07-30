# Generated by Django 4.2.3 on 2023-07-16 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_number', models.IntegerField(primary_key=True, serialize=False)),
                ('type_of', models.CharField(blank=True, choices=[('SINGLE', 'single'), ('JOINT', 'joint')], default='SINGLE', max_length=10, null=True)),
                ('balance', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('mobile_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bank.account')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('degination', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('tran_type', models.CharField(choices=[('DEBIT', 'debit'), ('CREDIT', 'credit')], max_length=30)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.account')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('loan_amount', models.FloatField()),
                ('desc', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.customer')),
            ],
        ),
    ]