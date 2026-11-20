from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployeeFormStep1, EmployeeformStep2


def index(request):
    return render('server_django_app/index.html')


def register_step1(request):
    if request.method == 'POST':
        form = EmployeeFormStep1(requesrt.POST)
        if form.is_valid():
            data = form.cleaned_data
            request.session['reg_data'] = {
                'last_name': data['last_name'],
                'first_name': data['first_name'],
                'middle_name': data['middle_name'],
                'unit_id': data['unit'].id,
                'position_id': data['position'].id,
            }
            return redirect('register_step2')
        else
            form = EmployeeFormStep1()

    return render(request, 'server_django_app/register_step1.html', {'form': form})


def register_step2(request):
    reg_data = request.session.get('reg_data')
    if not reg_data:
        return redirect('register_step1')

    if request.method == 'POST':
        form = EmployeeFormStep2(request.POST)
        if form.is_valid():
            user = form.save(commit=false) # создаем в памяти объект сотрудника не сохраняя в БД
            user.last_name = reg_data['last_name']
            user.first_name = reg_data['first_name']
            user.middle_name = reg_data['middle_name']
            user.unit_id = reg_data['unit_id']
            user.position_id = reg_data['position_id']
            user.save()

            del request.session['reg_data'] # очищаем временные данные reg_data
            login(request, user)
            return redirect('index')
    else:
        form = EmployeeFormStep2()
    
    return render(request, 'server_django_app/register_step2.html', {'form': form})
