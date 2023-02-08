from django import forms
from .models import *
from django.contrib.auth import authenticate

ROLES = [
    ('is_student', 'Student'),
    # ('is_parent', 'Parent'),
    ('is_lecturer', 'Lecturer'),
     ('is_admin', 'Admin'),
   
]


gender = [
    ("male","Male"),
    ("female","Female"),
    ("other", "Other")
]   
 

courses =   Course.objects.all()
course_list = []
for item in courses:
    single_item = (item.id, str(item.name))
    course_list.append(single_item)
    

staffs =   Staff.objects.all()
staff_list = []
for item in staffs:
    single_staff = (item.id, str(item.gender))
    staff_list.append(single_staff)

sessions = Session.objects.all()
session_list = []
for session_year in sessions:
    single_session_year = (session_year.id, str(session_year.name))
    session_list.append(single_session_year)
        
   


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'15','placeholder':'First Name'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'15','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','minlength':'10','maxlength':'40','placeholder':'Email Address'}))  
    role= forms.CharField(widget=forms.HiddenInput(attrs={"value":"is_student","class":"form-control"}))    
    gender = forms.ChoiceField(label="Gender", choices=gender, widget=forms.Select(attrs={"class":"form-control"}))
    course = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))   
    session = forms.ChoiceField(label="Session", choices=session_list, widget=forms.Select(attrs={"class":"form-control"}))
    year_of_study = forms.ChoiceField(label="Year of Study",choices= [("I","I"), ("II","II"),
                    ("III", "III"),
                    ("IV", "IV"),
                    ("V", "V")
                ]
                ,widget=forms.Select(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    

class LoginForm(forms.ModelForm):
    password = forms.CharField(
        
                               widget=forms.PasswordInput
                               (attrs={'placeholder':'Enter your Password','class':'form-control'}))
    email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your email address','class':'form-control'}))
 
    class Meta:
        model = User
        fields= ('email', 'password')
        def clean(self):
            if(self.is_valid)():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email,password=password):
                    raise forms.ValidationError('Invalid credentials')
                
                
class AddCourseForm(forms.ModelForm):
    name =  forms.TextInput(attrs={'class': 'form-control'}),
    class Meta:
        model = Course
        fields= ['name']
        

class EditCourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "name"
    }))
    class Meta:
        model = Course
        fields= ('name',)    
        
        
    
class AddStaffForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'15','placeholder':'First Name'}))
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'15','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','minlength':'10','maxlength':'40','placeholder':'Email Address'}))  
    role= forms.CharField(widget=forms.HiddenInput(attrs={"value":"is_lecturer","class":"form-control"}))    
    gender = forms.ChoiceField(label="Gender", choices=gender, widget=forms.Select(attrs={"class":"form-control"}))    
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    
class AddUnitForm(forms.ModelForm):
    course = forms.Select( choices=course_list,attrs={"class":"form-select"})
    staff = forms.Select( choices=staff_list,attrs={"class":"form-select"})
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'40','placeholder':'Enter Unit Name'}))
    class Meta:
        model = Unit
        fields =["name","course","staff"]    
        
class AddSessionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','minlength':'3','maxlength':'15','placeholder':'Session Name'}))
    start = forms.CharField(widget=forms.DateInput(format = '%Y-%m-%d',attrs={'class':'form-control',"type":"date"}))
    end = forms.CharField(widget=forms.DateInput(format = '%Y-%m-%d',attrs={'class':'form-control',"type":"date"}))
    class Meta:
        model = Session
        fields=["name","start","end"]
        
        
            