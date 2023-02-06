from django.shortcuts import render,redirect,get_object_or_404
from users.forms import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from .models import *
from django.views.decorators.csrf import csrf_exempt
from .decorators import user_is_superuser
from django.http import HttpResponse


def loginuser(request):
    if request.user.is_authenticated:
        messages.warning(request, f' You are already logged in !!')
        return redirect('/')
    else:        
        if request.method == 'POST':            
            email = request.POST['email']
            password = request.POST['password']
           
            user = authenticate(request, email = email, password = password)
            if user is not None:
                form = login(request, user)                
                messages.success(request, f' welcome {email} !')
                path_redirect = request.get_full_path().split('?next=',1)
                if '?next=' in request.get_full_path():
                    return redirect(path_redirect[1])
                else:
                    return redirect('/')                     
                
            else:
                messages.error(request, f'Invalid details, please enter correct details or sign up!')
        form = LoginForm()       
    return render(request, 'accounts/login.html', {'form':form})


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect('/')


@login_required(login_url="/login")
def home(request):
    staffs = Staff.objects.all().count()
    students = Student.objects.all().count()
    units = Unit.objects.all().count()
    courses = Course.objects.all().count()
    users = User.objects.all().count()
        
    return render(request, "dashboard.html",
                  context ={"staffs":staffs,
                            "students":students,
                            "units":units,
                            "courses":courses,
                            "users":users,  })



@login_required(login_url="/login")
def take_attendance(request):
    staffId = Staff.objects.get(user = request.user.id)
    units = Unit.objects.filter(staff=staffId)
    sessions = Session.objects.all()
    context={"units":units, "sessions":sessions, }
    return render(request, 'staff/take_attendance.html', context)


@login_required(login_url="/login")    
def units(request):
    user = request.user.id
    staff = Staff.objects.get(user = user)
    counts = Unit.objects.filter(staff = staff)    
    return render(request, "staff/view-units.html", context={"counts":counts})



"""HOD VIEWS
"""
@user_is_superuser
def add_course(request):
    if request.method =="POST":
       form = AddCourseForm(request.POST)
       if form.is_valid():
            name = form.cleaned_data["name"]
            form.save()
            messages.success(request, "Course added successfully")
                
    else:
        form = AddCourseForm()          
    return render(request, "admin/add_course.html", context={"form":form})


@user_is_superuser
def courses(request):
    courses =Course.objects.all().order_by("-created_at")
    return render(request,"admin/courses.html", context={"courses":courses})

@user_is_superuser
def edit_course(request, pk):                                         
    data = get_object_or_404(Course, id=pk)
    form = EditCourseForm(instance=data)                                                               

    if request.method == "POST":
        form = EditCourseForm(request.POST, instance=data)
        if form.is_valid():
            name = form.cleaned_data['name']
            data.name = name
            data.save()
            messages.success(request, "Course updated successfully")
            return redirect ('home')
    context = {
        "form":form
    }
    return render(request, 'admin/edit_course.html', context)

@user_is_superuser
def students(request):
    students = Student.objects.all()
    return render(request, "admin/students.html",
    context ={"students":students})
    
    
@user_is_superuser
def add_student(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            role = form.cleaned_data['role']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            session_year_id = form.cleaned_data['session']
            course_id = form.cleaned_data['course']
            year_of_study = form.cleaned_data['year_of_study']
            gender = form.cleaned_data['gender']
            # print("first_name",first_name)
            # print("last_name",last_name)
            # print("role",role)
            # print("email",email)
            # print("password",password)
            # print("session_year",session_year_id)
            # print("course_id",course_id)
            # print("year_of_study",year_of_study)
            # print("gender",gender)
            
            course_obj = Course.objects.get(id=course_id)                    
            session_year_obj = Session.objects.get(id=session_year_id)
            # try:
                
            email_taken = User.objects.filter(email=email).exists()
            if email_taken:
                messages.error(request, "Email already taken")
            else:    
                is_student =True
                user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, role=role, password=password, is_student=is_student)
                
                
                student = Student.objects.create(user=user, course= course_obj, 
                                                    session = session_year_obj,gender=gender, 
                                                    year_of_study=year_of_study)
                
                messages.success(request, "Student Added Successfully!")
                return redirect('/students')
           
        else:
            return redirect('add_student')    
    else:
        form = UserRegistrationForm()    
    return render(request, "admin/add_student.html", context = {"form":form})
   

@user_is_superuser
def edit_student(request, pk):    
    student = get_object_or_404(Student, id=pk)
    form = EditStudentForm(instance=student)                                                               

    if request.method == "POST":
        form = EditStudentForm(request.POST, instance= student)
        if form.is_valid():          
            
            session_year_id = form.cleaned_data['session']
            course_id = form.cleaned_data['course']
            year_of_study = form.cleaned_data['year_of_study']
            gender = form.cleaned_data['gender']
            # course_obj = Course.objects.get(id=course_id)                    
            session_year_obj = Session.objects.get(id=session_year_id)
            
            
                 
            new_student = Student.objects.get(id = student)
            course =  Course.objects.get(id=course_id)   
            new_student.course = course
            new_student.session = session_year_obj
            new_student.gender = gender
            new_student.year_of_study = year_of_study
            new_student.save()
            
            
            messages.success(request, "Student updated Successfully!")
            return redirect('/students')
           
        else:
            return redirect('add_student')   
    context={"form":form}     
    return render(request, "admin/edit_student.html",context)   

  
@user_is_superuser  
def staff(request):
    staffs=Staff.objects.all()
    return render(request, "admin/staff.html", context={"staffs":staffs})

@user_is_superuser
def add_staff(request):
    if request.method == "POST":
        form = AddStaffForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            role = form.cleaned_data['role']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']            
            gender = form.cleaned_data['gender']            
            email_taken = User.objects.filter(email=email).exists()
            if email_taken:
                messages.error(request, "Email already taken")
            else:    
                is_lecturer = True
                user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, role=role, password=password, is_lecturer=is_lecturer)
                
                
                Staff.objects.create(user=user, gender=gender)
                
                messages.success(request, "Staff Added Successfully!")
                return redirect('/staff')
           
        else:
            return redirect('add_staff')    
    else:
        form = AddStaffForm()    
    return render(request, "admin/add_staff.html", context={"form":form})


@user_is_superuser
def edit_staff(request):
    return render(request, "admin/edit_staff.html")

@user_is_superuser
def add_unit(request):
    if request.method == "POST":
        form = AddUnitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Unit added successfully")
            return redirect('/admin_units')
    else:
        form =AddUnitForm()        
    return render(request ,"admin/add_unit.html", context={"form":form})

@user_is_superuser
def admin_units(request):
    units = Unit.objects.all().order_by("-created_at")
    return render(request ,"admin/all_units.html", context={"units":units})

@user_is_superuser
def edit_unit(request, pk):
    data = get_object_or_404(Unit, id=pk)
    form = AddUnitForm(instance=data)                                                               

    if request.method == "POST":
        form = AddUnitForm(request.POST, instance=data)
        if form.is_valid():
            data.save()
            messages.success(request, "Course updated successfully")
            return redirect ('/admin_units')
   
    return render(request ,"admin/add_unit.html", context={"form":form})

@user_is_superuser
def add_session(request):
    if request.method == "POST":
        form =  AddSessionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Session added successfully")
            return redirect('/admin_sessions')
    else:
        form =AddSessionForm()     
    return render(request, "admin/add_session.html", context={"form":form})

@user_is_superuser
def admin_sessions(request):
    sessions= Session.objects.all()
    return render(request, "admin/sessions.html",context={"sessions":sessions} )

def edit_session(request,pk):
    data = get_object_or_404(Session, id=pk)
    form = AddSessionForm(instance=data)                                                               

    if request.method == "POST":
        form = AddSessionForm(request.POST, instance=data)
        if form.is_valid():
            data.save()
            messages.success(request, "Session updated successfully")
            return redirect ('/admin_sessions')
   
    return render(request,"admin/edit_session.html", context={"form":form})