from django.shortcuts import render
import sqlite3

# Create your views here.
from django.http import HttpResponse
from django_tables2 import RequestConfig
from .models import Student

from .tables import StudentTable
from .forms import NewStudent

from django.views.decorators.csrf import csrf_exempt


def index(request):

    return HttpResponse("Hello, MercyCorps app <br> Add Student")

def addstudent(request):
     return render(request, 'mercycorps_app/AddStudent.html')

@csrf_exempt 
def new_student(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        print("Ian")
        form = NewStudent(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            if form.doesRecordExit():
                #The student already exists return error
                return HttpResponse("Error, Student already exist")
            # redirect to a new URL:
            form.addStudent()
            
            return HttpResponse("Student added")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewStudent()

    return render(request, 'mercycorps_app/AddStudent.html', {'form': form})



def student(request):
    db = sqlite3.connect('../db/MercyCorps.db')

    # Get a cursor object
    cursor = db.cursor()
    
    cursor.execute('''SELECT lastname, firstname, Person.id, Person.att_percent FROM Person INNER JOIN Student ON Person.id=Student.personid''')
    
    student_list = cursor.fetchall() #retrieve the first row

    Student.objects.all().delete()
    
    for lastname, firstname, id, att_percent in student_list:
        if (att_percent>80):
            payment='YES'
        else:
            payment='NO'
        Student.objects.create(last_name=lastname, first_name=firstname, percentage=att_percent, payment=payment)
   
    
    db.close()
    
    table = StudentTable(Student.objects.all())
    RequestConfig(request).configure(table)
    #School_reponse = "School Name: %s<br>Address: %s<br>Phone number: %s" % (name, address, phone)
    
    #return render(request, 'mercycorps_app/student.html', {'table': Student.objects.all()})
    return render(request, 'mercycorps_app/student.html', {'table': table})

