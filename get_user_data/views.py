from django.shortcuts import render
from django.http import HttpResponse
from .models import students

def site(request):
    if(request.method == 'POST'):
        stud = students(
            name = request.POST.get('name'),
            surname = request.POST.get('surname'),
            tel_number = request.POST.get('telephone'),
            category = request.POST.get('category'),
            worker = request.POST.get('worker'),
        )
        
        stud.save()
    return render(request, 'registration.html')