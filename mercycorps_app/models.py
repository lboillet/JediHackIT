from django.db import models

# Create your models here.

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20,  blank=True)
    email = models.EmailField('email',  blank=True)
    
    def __str__(self):
        return self.name 

class Student(models.Model):
    male = 'M'
    female = 'F'
    
    choice_gender = (
                    (male, 'Male'),
                    (female, 'Female'),
                    )
    
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    nationalid = models.CharField(max_length=30)
    phone = models.CharField(max_length=20, blank=True)
    email  = models.EmailField('e-mail', blank=True)
    address = models.CharField(max_length=200)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name ='School Name')
    
    gender = models.CharField(
        max_length=1,
        choices=choice_gender,
        default=female,
    )
    dob = models.DateTimeField('date of birth')

    def __str__(self):
        name = '%s %s' % (self.lastname, self.firstname)
        return name

class Legal_Rep(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)


class Payment(models.Model):
    
    cash = 'C'
    electronic = 'E'
    
    payment_method = (
                     (cash, 'cash'),
                     (electronic, 'electronic'),
                     )
    
    value = models.IntegerField(default=0)
    currency = models.CharField(max_length=10)
    
    method = models.CharField(
        max_length=1,
        choices=payment_method,
        default=cash,
    )
    
    payment_made = models.DateTimeField('date when payment made to legal rep')
    
class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name ='Student Name')
    start_lessons = models.DateTimeField('date/time started lessions', blank=True)
    finish_lessions = models.DateTimeField('date/time finished lessions', blank=True)
     