from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import StudentForm, AttendanceForm, SchoolForm

@login_required
def home(request):

        return render(request, 'mercycorps_app/home.html')

@login_required
def add_student(request):
        
    if request.method == 'POST':
        
        form = StudentForm(request.POST)
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ..
            # redirect to a new URL:
            
            if form.is_duplicate_record() == False:
                form.save()
                
                return HttpResponseRedirect('/thanks/')
        
            else:
                return render(request, 'mercycorps_app/addstudent.html', {'form': form})

        
    else:
        form = StudentForm()
        
    return render(request, 'mercycorps_app/addstudent.html', {'form': form})

@login_required
def add_school(request):
    
    if request.method == 'POST':
        
        form = SchoolForm(request.POST)
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ..
            # redirect to a new URL:
            
            if form.is_duplicate_record() == False:
                form.save()
                
                return HttpResponseRedirect('/thanks/')
        
            else:
                return render(request, 'mercycorps_app/addschool.html', {'form': form})

        
    else:
        form = SchoolForm()
        
    return render(request, 'mercycorps_app/addschool.html', {'form': form})

@login_required
def attendance(request):
    
    if request.method == 'POST':
        
        form = AttendanceForm(request.POST)
        
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ..
            # redirect to a new URL:
            
            if form.is_duplicate_record() == False:
                form.save()
                
                return render(request, 'mercycorps_app/attendance.html', {'form': form})
        
            else:
                return render(request, 'mercycorps_app/attendance.html', {'form': form})

        
    else:
        form = AttendanceForm()
        
    return render(request, 'mercycorps_app/attendance.html', {'form': form})

@login_required
def data_analysis(request):
        return render(request, 'mercycorps_app/dataAnalysis.html')
