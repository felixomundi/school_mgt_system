from django.shortcuts import render,redirect
from .models import User,Student,Unit,Course,StudentResult,Attendance,AttendanceReport
import json
from django.http import HttpResponse
from .decorators import user_is_student
from django.contrib.auth.decorators import login_required

@login_required(login_url="/")
@user_is_student
def student_profile(request):
    user  = User.objects.filter(id = request.user.id).first()
    student = Student.objects.get(user = user)
    return render(request, 'student/student_profile.html', context = {"user":user,"student":student })

@login_required(login_url="/")
@user_is_student
def student_profile_update(request):
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    gender = data['gender']
    user = User.objects.get(id= request.user.id)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    student = Student.objects.get(user = user)
    student.gender = gender
    student.save()    
    return HttpResponse("Ok")

@login_required(login_url="/")
@user_is_student
def view_result(request):
    student = Student.objects.get(user = request.user.id)
    student_result = StudentResult.objects.filter(student=student.id)
    return render(request, 'student/view_result.html', context={"student_result":student_result})

@login_required(login_url="/")
@user_is_student
def student_units(request):
    student = Student.objects.get(user=request.user.id)
    course = Course.objects.get(id=student.course.id)
    units = Unit.objects.filter(course = course)
    
    return render(request, "student/student_units.html", context={ "units":units})


@login_required(login_url="/")
@user_is_student
def student_home(request):
    student = Student.objects.get(user=request.user.id)
    total_attendance = AttendanceReport.objects.filter(student=student).count()    
    # attendance_present = AttendanceReport.objects.filter(student=student, status=1).count()
  
    course = Course.objects.get(id=student.course.id)   
    total_units = Unit.objects.filter(course=course).count()
    units = Unit.objects.filter(course = course)
    
    """ Attendance chart """
    
    # subject_name = []
    # data_present = []
    
    # unit_data = Unit.objects.filter(course=student.course)
    # for unit in unit_data:
    #     attendance = Attendance.objects.filter(unit=unit.id)
    #     attendance_present_count = AttendanceReport.objects.filter(attendance__in=attendance, status=1, student=student.id).count()
    #     subject_name.append(unit.name)
    #     data_present.append(attendance_present_count)
    
    
    context ={
        "total_attendance":total_attendance,
        "total_units":total_units,
        "units":units,
        "course":course,
        # "attendance_present": attendance_present,
        # "subject_name": subject_name,
        # "data_present": data_present,
        
    }
    
    
    return render(request, "student/student_home.html",
                  context)
    