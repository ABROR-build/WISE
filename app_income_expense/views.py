from django.shortcuts import render, redirect
from django.views import View
from datetime import date, datetime, timedelta
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
        return render(request, 'income_expenses/reports/list_reports.html', context=context)


# filters
class FilterIncomes(View):
    def get(self, request):
        incomes = models.Incomes.objects.filter(user=request.user)
        income_amount = 0
        for i in models.Incomes.objects.filter(user=request.user):
            income_amount += i.amount

        context = {
            'incomes': incomes,
            'income_amount': income_amount
        }
        return render(request, 'income_expenses/reports/filter_incomes.html', context=context)


class FilterExpenses(View):
    def get(self, request):
        expenses = models.Expenses.objects.filter(user=request.user)
        expense_amount = 0
        for i in models.Expenses.objects.filter(user=request.user):
            expense_amount += i.amount

        context = {
            'expenses': expenses,
            'expense_amount': expense_amount
        }
        return render(request, 'income_expenses/reports/filter_expenses.html', context=context)


class FilterToday(View):
    def get(self, request):
        today = date.today()
        today_expenses = 0
        today_incomes = 0
        today_reports = models.Reports.objects.filter(timestamp__date=today, user=request.user)

        for i in models.Reports.objects.filter(timestamp__date=today, user=request.user):
            if i.is_income is True:
                today_incomes += i.amount

            elif i.is_expense is True:
                today_expenses += i.amount

        context = {
            'today': today,
            'today_expenses': today_expenses,
            'today_incomes': today_incomes,
            'today_reports': today_reports,
        }
        return render(request, 'income_expenses/reports/today_reports.html', context=context)


class FilterTodayIncomes(View):
    def get(self, request):
        today = date.today()
        incomes = models.Incomes.objects.filter(user=request.user, timestamp__date=today)
        income_amount = 0
        for i in models.Incomes.objects.filter(user=request.user, timestamp__date=today):
            income_amount += i.amount

        context = {
            'incomes': incomes,
            'income_amount': income_amount
        }
        return render(request, 'income_expenses/reports/filter_today_incomes.html', context=context)


class FilterTodayExpenses(View):
    def get(self, request):
        today = date.today()
        expenses = models.Expenses.objects.filter(user=request.user, timestamp__date=today)
        expense_amount = 0
        for i in models.Expenses.objects.filter(user=request.user, timestamp__date=today):
            expense_amount += i.amount

        context = {
            'expenses': expenses,
            'expense_amount': expense_amount
        }
        return render(request, 'income_expenses/reports/filter_today_expenses.html', context=context)


class FilterCustomDate(View):
    def get(self, request, custom_date):
        custom_date = datetime.strptime(custom_date, '%B %d, %Y').date()
        custom_date_expenses = 0
        custom_date_incomes = 0
        custom_date_reports = models.Reports.objects.filter(timestamp__date=custom_date, user=request.user)

        for i in models.Reports.objects.filter(timestamp__date=custom_date, user=request.user):
            if i.is_income is True:
                custom_date_incomes += i.amount

            elif i.is_expense is True:
                custom_date_expenses += i.amount

        context = {
            'custom_date': custom_date,
            'custom_date_expenses': custom_date_expenses,
            'custom_date_incomes': custom_date_incomes,
            'custom_date_reports': custom_date_reports,
        }
        return render(request, 'income_expenses/reports/custom_date_reports.html', context=context)


class FilterThisMonth(View):
    def get(self, request):
        today = date.today()
        first_day_of_month = today.replace(day=1)
        last_day_of_month = today.replace(day=1) + timedelta(days=32)
        last_day_of_month = last_day_of_month.replace(day=1) - timedelta(days=1)

        month_expenses = 0
        month_incomes = 0
        month_reports = models.Reports.objects.filter(
            timestamp__date__range=[first_day_of_month, last_day_of_month],
            user=request.user,
        )

        for report in month_reports:
            if report.is_income:
                month_incomes += report.amount
            elif report.is_expense:
                month_expenses += report.amount

        context = {
            'current_month': today.strftime('%B %Y'),
            'month_expenses': month_expenses,
            'month_incomes': month_incomes,
            'month_reports': month_reports,
        }
        return render(request, 'income_expenses/reports/this_month_reports.html', context=context)
