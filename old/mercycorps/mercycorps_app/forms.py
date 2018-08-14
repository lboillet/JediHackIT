from django import forms
import sqlite3

class NewStudent(forms.Form):
    first_name = forms.CharField(label='first_name', max_length=100)
    last_name = forms.CharField(label='last_name', max_length=100)
    att_percent = forms.CharField(label='att_percent', max_length=100)
    
    def doesRecordExit(self):
    
          cd = self.cleaned_data

          
          db = sqlite3.connect('../db/MercyCorps.db')

          # Get a cursor object
          cursor = db.cursor()
    
          cursor.execute('''SELECT lastname, firstname, Person.id FROM Person WHERE lastname = ? AND firstname = ?''', (cd['last_name'], cd['first_name']))

          student_list = cursor.fetchall() #retrieve the first row

          db.close()

          if len(student_list) == 0:
              return False
    
          return True
          
          
    def addStudent(self):
        db = sqlite3.connect('../db/MercyCorps.db')
        cursor = db.cursor()
        
        cd = self.cleaned_data
        
        cursor.execute('''INSERT INTO Person( firstname, lastname, att_percent, payment) VALUES(?,?,?,?)''', (cd['first_name'], cd['last_name'], cd['att_percent'], 'No'))
        
        cursor.execute('''SELECT id FROM Person WHERE lastname = ?  and firstname =? ''', (cd['last_name'], cd['first_name']))
        
        new_student = cursor.fetchone()
        print(new_student)
        personid = new_student[0]
        
        cursor.execute('''INSERT INTO Student( 'personid') VALUES(?)''', (new_student))
        db.commit()
        db.close()
