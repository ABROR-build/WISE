from django.db import models
from app_users.models import Users


class IncomeTypes(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'IncomeTypes'

    def __str__(self):
        return self.name


class ExpenseTypes(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = 'ExpenseTypes'

    def __str__(self):
        return self.name


class Incomes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    income_type = models.ForeignKey(IncomeTypes, on_delete=models.CASCADE)
    earned_from = models.CharField(max_length=800)
    amount = models.IntegerField()
    comment = models.CharField(max_length=400, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Incomes'

    def __str__(self):
        return self.earned_from


class Expenses(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    expense_type = models.ForeignKey(ExpenseTypes, on_delete=models.CASCADE)
    spent_to = models.CharField(max_length=800)
    amount = models.IntegerField()
    comment = models.CharField(max_length=400, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Expenses'

    def __str__(self):
        return self.spent_to


class Reports(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    activity = models.CharField(max_length=800, null=True)
    comment = models.CharField(max_length=1000, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(null=True)
    is_income = models.BooleanField(default=False, null=True)
    is_expense = models.BooleanField(default=False, null=True)

    class Meta:
        db_table = 'Reports'

    def __str__(self):
        return self.activity


class Balance(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    balance_amount = models.IntegerField(default=0)

    class Meta:
        db_table = 'Balance'

    def __int__(self):
        return self.balance_amount
