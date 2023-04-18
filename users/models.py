from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# from twilio.rest import Client
# from decouple import config

from django.core.mail import EmailMessage, send_mail
from django.conf import settings

gender = [
    ("male","male"),
    ("female","female"),
    ("other", "other")
]   
 
 
academic = [
    ("I","I"),
    ("II","II"),
    ("III", "III"),
     ("IV", "IV"),
      ("V", "V")
]   

class UserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,role,password=None,is_student=False,is_lecturer=False):
        if not email:
            raise ValueError('Email address is required')
       
        if not first_name:
            raise ValueError("First Name required")
        if not last_name:
            raise ValueError("Last Name is required")
        if not role:
            raise ValueError("Role is required")
        
        user=self.model(
            email =self.normalize_email(email),
            first_name=first_name,
            last_name =last_name,
            role=role,
            is_student=is_student,
            is_lecturer=is_lecturer,
           
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,first_name,last_name,role,password:None):
        if not email:
            raise ValueError('Email address is required')
       
        if not first_name:
            raise ValueError("First Name required")
        if not last_name:
            raise ValueError("Last Name is required")
        if not role:
            raise ValueError("Role is required")
        user=self.model(
            email =self.normalize_email(email),           
             first_name=first_name,
            last_name =last_name,
            role=role,
            
        )
        user.set_password(password)
        user.is_admin =True
        user.is_superuser= True
        user.is_staff = True
        user.save(using=self._db)
        return user

ROLES = [
    ('is_student', 'Student'),
    # ('is_parent', 'Parent'),
    ('is_lecturer', 'Lecturer'),
    ('is_admin', 'Admin'),
   
]

class User(AbstractBaseUser,PermissionsMixin):
    
    email =models.EmailField(verbose_name="email address",unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15) 
    is_admin = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)     
    is_student= models.BooleanField(default=False)
    is_parent= models.BooleanField(default=False)
    is_lecturer= models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)      
    date_registered = models.DateTimeField(auto_now_add=True)
    
    date_updated = models.DateTimeField(auto_now=True)
    last_login =models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True) 
    role = models.CharField(
        max_length = 40,
        choices = ROLES
        )
    
    objects = UserManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ["first_name","last_name", "role"]
    
    def __str__(self):
        return str(self.email)
    def has_perm(self,perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    

  
    
class Session(models.Model):    
    name = models.CharField(max_length=50)
    start = models.DateField()
    end = models.DateField()
    
    def __str__(self):
        return self.name     
    

class Course(models.Model):
   
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.name
    
 
 
class Student(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                limit_choices_to={ 'role': "is_student"},
                                )
    gender = models.CharField(max_length=10,choices= gender)    
    course = models.ForeignKey(Course,on_delete=models.PROTECT)
    year_of_study = models.CharField(choices=academic, max_length=5)   
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return str(self.user.email )
    

class Staff(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                limit_choices_to={ 'role': "is_lecturer"},)
    gender = models.CharField(max_length=10,choices= gender)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.user.email     
    
    

class Admin(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10,choices= gender)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.user.email     
    
    
    
class Unit(models.Model):
      
    name = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course,  on_delete=models.PROTECT)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    
    
    
class Attendance(models.Model):
      
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)    
    session = models.ForeignKey(Session,on_delete=models.DO_NOTHING)
    attendance_date = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.unit.name
    
    
class AttendanceReport(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)    
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.student.user.email
    def save(self,*args, **kwargs):        
        # account_sid = config('TWILIO_ACCOUNT_SID')    
        # auth_token = config('TWILIO_AUTH_TOKEN')
        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #                 .create(
        #                     body=f"Your attendance for {self.attendance.attendance_date}  and {self.attendance.unit.name} was added successfully",
        #                     from_='+12764004442',
        #                     to=['+254745566505']
        #                 )
                
        # return super().save(*args, **kwargs)
        subject = 'Record of your attendance'
        mesagge = f"Your attendance for {self.attendance.unit.name} on {self.attendance.attendance_date} was added successfully"
        from_email = settings.EMAIL_HOST_USER
        to_list = ["fomundi34@gmail.com"] 
        send_mail(subject, mesagge, from_email, to_list, fail_silently=False)
        return super().save(*args, **kwargs)
        
        
            
class StudentResult(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    unit_exam_marks = models.FloatField(default=0)
    unit_assignment_marks = models.FloatField(default=0)
    total_marks = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student.user.email 
    
    @property
    def total(self):
        return self.unit_assignment_marks + self.unit_exam_marks
    
    def save(self, *args, **kwargs):        
        # account_sid = config('TWILIO_ACCOUNT_SID')    
        # auth_token = config('TWILIO_AUTH_TOKEN')
        # client = Client(account_sid, auth_token)
        # message = client.messages \
        #                 .create(
        #                     body=f"Your marks for {self.unit.name} was added successfully",
        #                     from_='+12764004442',
        #                     to=['+254745566505']
        #                 )
                
        # return super().save(*args, **kwargs)
        subject = 'Record of your marks'
        mesagge = f'Marks for {self.unit.name} was added successfully'
        from_email = settings.EMAIL_HOST_USER
        to_list = ["fomundi34@gmail.com"] 
        send_mail(subject, mesagge, from_email, to_list, fail_silently=False)
        return super().save(*args, **kwargs)
        
        
  
             
