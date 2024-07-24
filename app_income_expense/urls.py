from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('add_income/', views.AddIncome.as_view(), name='add-income'),
    path('add_expense/', views.AddExpense.as_view(), name='add-expense'),
    path('list_reports/', views.ListReports.as_view(), name='list-reports'),

    # filters
    path('filter_incomes/', views.FilterIncomes.as_view(), name='filter-incomes'),
    path('filter_expenses/', views.FilterExpenses.as_view(), name='filter-expenses',),
    path('today_reports/', views.FilterToday.as_view(), name='today-reports'),
    path('custom-date-reports/<str:custom_date>/', views.FilterCustomDate.as_view(), name='custom-date-reports'),
    path('this_mont_reports/', views.FilterThisMonth.as_view(), name='this-month-reports'),
    path('filter_today_incomes/', views.FilterTodayIncomes.as_view(), name='filter-today-incomes'),
    path('filter_today_expenses/', views.FilterTodayExpenses.as_view(), name='filter-today-expenses'),
]
