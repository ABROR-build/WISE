from django.shortcuts import render, redirect
from django.views import View
from . import models
from . import forms


class Home(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            balances = models.Balance.objects.filter(pk=request.user.pk)
            context = {
                'balances': balances
            }
            return render(request, 'income_expenses/home.html', context=context)


class AddIncome(View):
    def get(self, request):
        income_form = forms.AddIncomeForm()
        income_types = models.IncomeTypes.objects.all()
        context = {
            'income_form': income_form,
            'income_types': income_types
        }
        return render(request, 'income_expenses/add_income.html', context=context)

    def post(self, request):
        income_types = models.IncomeTypes.objects.all()
        income_form = forms.AddIncomeForm(request.POST)
        if income_form.is_valid():
            income = income_form.save(commit=False)
            income.user = request.user
            income.save()

            reports = models.Reports.objects.create(
                user=request.user,
                activity=income.earned_from,
                amount=income.amount,
                comment=income.comment,
                is_income=True,
            )
            reports.save()

            balance, created = models.Balance.objects.get_or_create(user=request.user)
            balance.save()

            balances = models.Balance.objects.get(user=request.user)
            balances.balance_amount += income.amount
            balances.save()

            return redirect('home')
        else:
            context = {
                'income_form': income_form,
                'income_types': income_types
            }
            return render(request, 'income_expenses/add_income.html', context=context)


class AddExpense(View):
    def get(self, request):
        expense_form = forms.AddExpenseForm()
        expense_types = models.ExpenseTypes.objects.all()
        context = {
            'expense_form': expense_form,
            'expense_types': expense_types
        }
        return render(request, 'income_expenses/add_expense.html', context=context)

    def post(self, request):
        expense_types = models.ExpenseTypes.objects.all()
        expense_form = forms.AddExpenseForm(request.POST)
        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.user = request.user
            expense.save()

            balance, created = models.Balance.objects.get_or_create(user=request.user)
            balance.save()

            reports = models.Reports.objects.create(
                user=request.user,
                activity=expense.spent_to,
                amount=expense.amount,
                comment=expense.comment,
                is_expense=True,
            )
            reports.save()

            balances = models.Balance.objects.get(user=request.user)
            balances.balance_amount -= expense.amount
            balances.save()

            return redirect('home')
        else:
            context = {
                'expense_form': expense_form,
                'expense_types': expense_types
            }
            return render(request, 'income_expenses/add_expense.html', context=context)


class ListReports(View):
    def get(self, request):
        reports = models.Reports.objects.filter(user=request.user)
        context = {
            'reports': reports
        }
        print(reports)
        return render(request, 'income_expenses/reports/list_reports.html', context=context)
