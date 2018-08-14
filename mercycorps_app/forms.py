from django import forms


from .models import Student, Attendance, School


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ('firstname', 'lastname', 'address', 'nationalid', 'phone', 'email', 'dob','school_id',)


        
    def is_duplicate_record(self):
        
        is_duplicate = True
        
        firstname = self.cleaned_data.get('firstname')
        lastname = self.cleaned_data.get('lastname')
        dob = self.cleaned_data.get('dob')
        
        found_records =  Student.objects.filter(firstname__contains = firstname).filter(lastname__contains = lastname)
        
        if not found_records:
            is_duplicate = False

        
        return is_duplicate
        
        
class SchoolForm(forms.ModelForm):
    
    class Meta:
        model = School
        fields = ('name', 'address', 'phone', 'email',)

    def is_duplicate_record(self):
        
        is_duplicate = True
        
        name = self.cleaned_data.get('name')
        address = self.cleaned_data.get('address')
        
        found_records =  School.objects.filter(name__contains = name).filter(address__contains = address)
        
        if not found_records:
            is_duplicate = False

        
        return is_duplicate
    


class AttendanceForm(forms.ModelForm):
    

    
    date = forms.DateField(widget=forms.widgets.SelectDateWidget)
    
    start_time = forms.TimeField(widget = forms.widgets.TimeInput)
    
    #end_time = forms.widgets.DateTime()
    
    class Meta:
        model = Attendance
        
        fields = ('student_id',)

