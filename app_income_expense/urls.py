from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('add_income/', views.AddIncome.as_view(), name='add-income'),
    path('add_expense/', views.AddExpense.as_view(), name='add-expense'),
    path('list_reports/', views.ListReports.as_view(), name='list-reports'),
]
