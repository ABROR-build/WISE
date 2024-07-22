from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_income_expense.urls')),
    path('users/', include('app_users.urls'))
]
