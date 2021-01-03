from django.shortcuts import render, redirect
from Patient.models import Patient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# Patient #
def add_Patient(request):
    if request.method == 'POST':
        add = Patient(
            name = request.POST['name'],
            gender = request.POST['gender'],
            birthdate = request.POST['birthdate'],
            age = request.POST['age'],
            marital_status = request.POST['marital_status'],
            mobile_no = request.POST['phone'],
            email = request.POST['email'],
            category = request.POST['category'],
            blood_group = request.POST['blood_group'],
            blood_pressure = request.POST['blood_pressure'],
            height = request.POST['height'],
            weight = request.POST['weight'],
            address = request.POST['address'],
            guardian_name = request.POST['guardian_name'],
            relationship = request.POST['relationship'],
            guardian_mobile_no = request.POST['guardian_mobile'],
        )
        add.save()
    return render(request, 'Patient_template/add_patient.html')

@csrf_exempt
def delete_patient(request):
    if request.method == 'POST':
        id = request.POST.get('pid')
        rem = Patient.objects.get(id=id)
        rem.delete()
        data = {
            'deleted': 1
        }
    return redirect('patient/view')

def patient_list(request):
    list = Patient.objects.all()
    context = {'all_patient': list}
    return render(request, 'Patient_template/patient_list.html', context)

def category(request):
    return render(request, 'Patient_template/category.html')