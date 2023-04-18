
from django.shortcuts import render,redirect,get_object_or_404
from users.forms import *

from django.contrib.auth.decorators import login_required

from .models import *
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse,JsonResponse
import json
from .decorators import user_is_lecturer


@login_required(login_url="/")
@user_is_lecturer
def get_students(request):
    unitId = request.POST.get("unit")
    sessionId = request.POST.get("session")
    
    # get staff units
    unit =  Unit.objects.get(id = unitId)    
    session_model =Session.objects.get(id = sessionId)
    students = Student.objects.filter(course = unit.course, session = session_model)    
    list_data = []
    for student in students:
        # data_small={"id":student.user.id, "name":student.user.first_name+" "+student.user.last_name}
        data_small = {'id':student.user.id, 'name':student.user.first_name+" "+student.user.last_name,}
        list_data.append(data_small)
    # return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)
    return JsonResponse(json.dumps(list_data),content_type="application/json", safe=False)
    
    
@login_required(login_url="/")
@user_is_lecturer
def save_attendance_data(request):
    data = json.loads(request.body)
    unitId = data['unit']
    attendanceDate = data['attendance']
    sessionId = data['session']
    studentIds = data['student_data']
    session = Session.objects.get(id = sessionId)
    unit = Unit.objects.get(id =unitId)  
    attendance = Attendance(unit=unit, attendance_date=attendanceDate, session=session)
    attendance.save()  
    student = Student.objects.get(user=studentIds)
               
    attendance_report = AttendanceReport(student=student, attendance=attendance, status=1)
    attendance_report.save()
    return HttpResponse("Attendance saved successfully")

@login_required(login_url="/")  
@user_is_lecturer
def update_attendance(request):
    staf = request.user.staff.id
    units = Unit.objects.filter(staff=staf)    
    sessions = Session.objects.all()
    context = {
        "units": units,
        "sessions": sessions
    }
    return render(request, "staff/update_attendance.html", context)

@login_required(login_url="/")
@user_is_lecturer
def get_attendance_dates(request):
    data = json.loads(request.body)
    unitId = data["unit"]
    sessionId = data["session"]
    # find session based on sessionId
    new_session = Session.objects.get(id=sessionId)
    # find unit based on unitId
    unit = Unit.objects.get(id= unitId)
    
    attendance = Attendance.objects.filter(session=new_session, unit =unit)
      # Passing Student Id and Student Name Only
    list_data = []

    for attendance_single in attendance:
        data_small={"id":attendance_single.id, "attendance_date":str(attendance_single.attendance_date), "session":attendance_single.session.id}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

@login_required(login_url="/")
@user_is_lecturer
def get_attendance_student(request):
    attendance = request.POST.get("attendance_date")
    print(attendance)
    return HttpResponse("ok")

@login_required(login_url="/")
@user_is_lecturer
def add_marks(request):
    user = request.user.id
    staff = Staff.objects.get(user = user)
    units = Unit.objects.filter(staff=staff)
    sessions = Session.objects.all()
   
    return render(request, "staff/add_marks.html",  context = {
        "units": units,
        "sessions": sessions,
    })
    
@login_required(login_url="/")  
@user_is_lecturer
def save_marks(request):
    data = json.loads(request.body)
    unitId = data['unit']
    studentId = data['student']
    assignment_marks = data['assignment_marks']
    exam_marks = data['exam_marks']   
    # find StudentById    
    student = Student.objects.get(user=studentId) 
    # find unitById
    unit = Unit.objects.get(id=unitId)
    # Check if Students Result Already Exists or not
    check_exist = StudentResult.objects.filter(unit=unit, student=student).exists()
    if check_exist:
        result = StudentResult.objects.get(unit=unit, student=student)
        result.unit_assignment_marks = assignment_marks
        result.unit_exam_marks = exam_marks
        result.save()
        return HttpResponse("Updated")
    else:
        result = StudentResult(student=student, unit=unit, unit_exam_marks=exam_marks, unit_assignment_marks=assignment_marks)
        result.save()        
        return HttpResponse("Ok")

@login_required(login_url="/")
@user_is_lecturer
def take_attendance(request):
    staffId = Staff.objects.get(user = request.user.id)
    units = Unit.objects.filter(staff=staffId)
    sessions = Session.objects.all()
    context={"units":units, "sessions":sessions, }
    return render(request, 'staff/take_attendance.html', context)


@login_required(login_url="/")  
@user_is_lecturer  
def units(request):
    user = request.user.id
    staff = Staff.objects.get(user = user)
    counts = Unit.objects.filter(staff = staff)    
    return render(request, "staff/view-units.html", context={"counts":counts})

@login_required(login_url="/")
@user_is_lecturer
def staff_home(request):
    user = request.user.id
    staff = Staff.objects.get(user = user)
    unit_count = Unit.objects.filter(staff = staff).count()
    
    units = Unit.objects.filter(staff=staff) 
    
    course_id_list = []
    for unit in units:
        course = Course.objects.get(id=unit.course.id)
        course_id_list.append(course.id)
    
    final_course = []
    
    # Removing Duplicate Course Id
    for course_id in course_id_list:
        if course_id not in final_course:
            final_course.append(course_id)
    
    students_count = Student.objects.filter(course__in=final_course).count()
    
    context={"unit_count":unit_count,
             "students_count":students_count
             }
    return render(request, "staff/staff_home.html", context)


@login_required(login_url="/")
@user_is_lecturer
def staff_profile(request):
    user = User.objects.get(id = request.user.id)
    staff = Staff.objects.filter(user = user).first()
    return render(request, 'staff/staff_profile.html', 
    context ={"staff":staff, "user":user })
    

@login_required(login_url="/")
@user_is_lecturer
def staff_profile_update(request):
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    gender = data['gender']
    user = User.objects.filter(id = request.user.id).first()
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    staff = Staff.objects.filter(user = user).first()
    staff.gender = gender
    staff.save()    
    return HttpResponse("Ok")