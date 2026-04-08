from django.shortcuts import render
from .models import Patient
from .forms import PatientForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def layout(request):
    return render(request,'home.html')


def patient_form(request):  
    print("METHOD:", request.method)
    if request.method == 'POST':
        print("POST HIT")
        form = PatientForm(request.POST, request.FILES)
        #print("FORM VALID?", form.is_valid())
        if form.is_valid():
            patient = form.save(commit=False)
            diseases = form.cleaned_data['existing_diseases']
            patient.existing_diseases = ",".join(diseases)
            patient.save()
            messages.success(request, "Patient registered successfully!")
            return redirect('patient_form')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})

@login_required
def doctor_dashboard(request):
    patients = Patient.objects.all()
    return render(request, 'doctor_dashboard.html', {'patients': patients})

@login_required
def toggle_status(request, id):
    patient = get_object_or_404(Patient, pk=id)
    patient.status = not patient.status
    patient.save()
    return redirect('doctor_dashboard')

@login_required
def patient_detail(request, id):
    patient = get_object_or_404(Patient, pk=id)
    return render(request, 'patient_detail.html', {'patient': patient})

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('doctor_dashboard')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'doctor_login.html')

def doctor_logout(request):
    logout(request)
    return redirect('layout')