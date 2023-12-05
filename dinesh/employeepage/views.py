from django.shortcuts import render
from .models import Employees
from .forms import EmployeesForm
from django.http import HttpResponse

# Create your views here.
def retrive_employee(request):
    emp = Employees.objects.all()
    return render(request, "register/Employeesdetails.html", context={"emp": emp})


def addnew_employee(request):
    form = EmployeesForm()
    if request.method == "POST":
        form = EmployeesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Successfully Registered <a href='/empdetails'>Click here to employeedetails</a></h1>")
    return render(request, "register/addemployee.html", context={"form": form})


def delete_employee(request, id):
    emp = Employees.objects.get(id=id)
    emp.delete()
    return HttpResponse("<h1>User data Delete Succesfully <a href='/empdetails'>Click here</a> to View the Update employedetails</h1>")


def update_employee(request, id):
    emp = Employees.objects.get(id=id)
    if request.method == "POST":
        form = EmployeesForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Update data Succesfuly<a href='/empdetails'>Click here</a> to View the Updated employedetails")
    return render(request, "register/updateemployee.html", context={"emp": emp})
