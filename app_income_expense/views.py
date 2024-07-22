from django.shortcuts import render, redirect
from django.views import View
from . import models


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
