from django.shortcuts import render
from .models import profile
from get_user_data.models import *

def login_check(request):
    login_error = "Неверный логин или пароль"
    if(request.method == 'POST'):
        if(profile.objects.filter(login=request.POST.get('login')).exists()):
            if(profile.objects.filter(password=request.POST.get('password')).exists()):
                profile_obj = profile.objects.get(login=request.POST.get('login'))
                student_obj = profile_obj.student_id
                worker_obj = student_obj.worker
                auto_obj = worker_obj.car
                next_lesson = lessons.objects.filter(student=student_obj.id).get
                # time = strftime(next_lesson)
                return render(request, 'myaccount.html', {'afterlogin': True, 'student': student_obj, 'worker': worker_obj, 'auto': auto_obj, 'lessons': next_lesson})
            else:
                return render(request, 'login.html', {'login_error': login_error})
        else:
            return render(request, 'login.html', {'login_error': login_error})
    return render(request, 'login.html')
