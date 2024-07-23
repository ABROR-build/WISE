from django import forms
from . import models


class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = models.Incomes
        fields = ['income_type', 'earned_from', 'amount', 'comment']


class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expenses
        fields = ['expense_type', 'spent_to', 'amount', 'comment']
