import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from Authentication.models import CustomUser
from Patient.models import Patient, Category


# Patient #
def add_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        age = request.POST['age']
        marital_status = request.POST['marital_status']
        mobile_no = request.POST['phone']
        email = request.POST['email']
        category = request.POST['category']
        blood_group = request.POST['blood_group']
        blood_pressure = request.POST['blood_pressure']
        height = request.POST['height']
        weight = request.POST['weight']
        address = request.POST['address']
        username = request.POST['username']
        password = request.POST['retype_password']
        category = int(category)

        if not birthdate:
            birthdate = None

        if not blood_pressure:
            blood_pressure = None

        if not height:
            height = None

        if not weight:
            weight = None

        if not address:
            address = None

        check = CustomUser.objects.filter(username=username)
        if check:
            return JsonResponse({'exist': 1})

        add = Patient(name=name, gender=gender, birthdate=birthdate, age=age, marital_status=marital_status,
                      mobile_no=mobile_no, email=email, category_id=category, blood_group=blood_group,
                      blood_pressure=blood_pressure, height=height, weight=weight, address=address)
        add.save()

        role = 4
        aid = add.id

        user = CustomUser.objects.create_user(username=username, password=password, role=role, aid=aid)
        user.save()
        return JsonResponse({'insert': 1})
    else:
        cat_list = Category.objects.all()
        context = {'category_list': cat_list}
        return render(request, 'Patient_template/add_patient.html', context)


def delete_patient(request):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        rem = Patient.objects.get(pk=patient_id)
        rem2 = CustomUser.objects.get(aid=patient_id, role=4)
        rem.delete()
        rem2.delete()
        return JsonResponse({'delete': 1})
    else:
        return redirect('/dashboard')


def patient_list(request):
    if request.user.role == 1 or request.user.role == 2 or request.user.role == 3:
        patient_all_list = Patient.objects.all()
        context = {'all_patient': patient_all_list}
        return render(request, 'Patient_template/patient_list.html', context)
    else:
        return render(request, '404.html')


def update_patient(request):
    if request.user.role == 1 or request.user.role == 3:
        pass
    else:
        return render(request, '404.html')


# Category #
def category(request):
    if request.user.role == 1:
        if request.method == 'POST':
            category = request.POST['category']

            check = Category.objects.filter(category=category)
            if check:
                return JsonResponse({'exist': 1})

            add = Category(category=category)
            add.save()
            return JsonResponse({'insert': 1})
        else:
            list = Category.objects.all()
            context = {'category_list': list}
            return render(request, 'Patient_template/category.html', context)
    else:
        return render(request, '404.html')


def delete_category(request):
    if request.user.role == 1:
        if request.method == 'POST':
            id = request.POST['category_id']

            cat = Category.objects.get(pk=id)
            cat.delete()

            return JsonResponse({'delete': 1})
        else:
            return redirect('/dashboard')
    else:
        return render(request, '404.html')


def update_category(request):
    if request.user.role == 1:
        if request.method == 'POST':
            id = request.POST['id']
            category = request.POST['update_category']

            check = Category.objects.filter(category=category)
            if check:
                return JsonResponse({'exist': 1})

            Category.objects.filter(pk=id).update(category=category)

            return JsonResponse({'update': 1})
        else:
            return redirect('/dashboard')
    else:
        return render(request, '404.html')