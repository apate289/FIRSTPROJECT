from django.shortcuts import render, HttpResponse
from faker import Faker
from .models import Employee
from django.http import HttpResponseRedirect

# Create your views here.

'''
def index(request):
    return HttpResponse("Hello, world. You're in the FIRSTAPPLICATION.")
'''
fake = Faker()


def home(request):
    context = {}
    return render(request, "index.html", context)


def randomData(request):
    Employee.objects.all().delete()
    for _ in range(0, 30):
        Employee.objects.create(EmployeeID=fake.pyint(), EmployeeName=fake.name(),
                                Contact=fake.phone_number(), Address=fake.address())
        context = {
            'posts': Employee.objects.all()
        }
    return render(request, "random.html", context)
