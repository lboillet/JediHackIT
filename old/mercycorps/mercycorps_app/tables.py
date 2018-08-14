import django_tables2 as tables
from .models import Student

class StudentTable(tables.Table):
    class Meta:
        model = Student
        template_name = 'django_tables2/bootstrap.html'
