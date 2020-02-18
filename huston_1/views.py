from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.views.generic.base import View

class Move(View):
    def get(self, request):
        # one_tit = 'Строительство заборов'
        # zaboru = 'заборы'
        return render(request, 'huston_1/index.html')
        # return HttpResponse('<h1>Hello every one, even you</h1>')