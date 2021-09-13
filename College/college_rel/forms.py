from django import forms
from .models import Student,Department,Lecturer

Department_choice=(('abc','Select Department Name>>>>>>'),('Mechanical Engineering','Mechanical Engineering'),('Electrical Engineering','Electrical Engineering'),
            ('Civil Engineering','Civil Engineering'),('Chemical Engineering','Chemical Engineering'),
            ('Computer Science Engineering','Computer Science Engineering'),('IT Engineering','IT Engineering'),
            ('Electronics Engineering','Electronics Engineering'),('Instrumentation Engineering','Instrumentation Engineering'),
            ('Aeronautical Engineering','Aeronautical Engineering'),('Mining Engineering','Mining Engineering'),
            ('Petrochemical Engineering','Petrochemical Engineering'),('Polymer Science Engineering','Polymer Science Engineering'),
            ('Information Engineering','Information Engineering'))
Department_intake=(('','Select Department Intake>>>>>>'),(30,30),(60,60),(80,80),(120,120),(180,180))

class Departmentform(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
        # widgets={
        #     'depname':forms.Select(choices=Department_choice,attrs={'placeholder':'Select'}),
        #     'depintake':forms.Select(choices=Department_intake)
        # }
        labels={
            "depname":"Department Name",
            'depintake':'Department Intake'
        }



class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        labels={
            'department':'Department Name',
            'stuname':'Student Name',
            'sturollno':'Student Roll No.',
            'stuaddress':'Student Address',
            'stumarks':'Student Marks'
        }

class Lecturerform(forms.ModelForm):
    class Meta:
        model=Lecturer
        fields='__all__'
        widgets={
            'department':forms.CheckboxSelectMultiple()
        }
        labels={
            'department':'Department Name',
            'lecname':'Lecturer Name',
            'lecsal':'Lecturer Salary',
            'lecsub':'Lecturer Subject'
        }