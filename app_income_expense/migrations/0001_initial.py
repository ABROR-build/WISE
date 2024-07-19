# Generated by Django 5.0.7 on 2024-07-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'Balance',
            },
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spent_to', models.CharField(max_length=800)),
                ('amount', models.IntegerField()),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('is_expense', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Expenses',
            },
        ),
        migrations.CreateModel(
            name='ExpenseTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'ExpenseTypes',
            },
        ),
        migrations.CreateModel(
            name='Incomes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earned_from', models.CharField(max_length=800)),
                ('amount', models.IntegerField()),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('is_income', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Incomes',
            },
        ),
        migrations.CreateModel(
            name='IncomeTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'IncomeTypes',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=800)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'Reports',
            },
        ),
    ]