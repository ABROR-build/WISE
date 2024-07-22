from django.contrib import admin
from . import models


admin.site.register(models.Balance)
admin.site.register(models.IncomeTypes)
admin.site.register(models.Incomes)
admin.site.register(models.ExpenseTypes)
admin.site.register(models.Expenses)
admin.site.register(models.Reports)


