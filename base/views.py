from django.shortcuts import render

def userAuth(request):
    return render(request, 'auth.html')
