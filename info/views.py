from django.shortcuts import render

def HOME(request):
    return render (request, 'home.html')