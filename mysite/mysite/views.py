from django.shortcuts import render
# noinspection PyUnresolvedReferences


def home(request):
       return render(request, 'index.html', {'blogs': blog})
