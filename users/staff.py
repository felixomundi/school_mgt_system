
from django.shortcuts import render,redirect,get_object_or_404
from users.forms import *

from django.contrib.auth.decorators import login_required

from .models import *
from django.views.decorators.csrf import csrf_exempt
from .decorators import user_is_superuser
from django.http import HttpResponse,JsonResponse
import json
from django.forms.models import model_to_dict


# from json import JSONEncoder
# from uuid import UUID

# old_default = JSONEncoder.default

# def new_default(self, obj):
#     if isinstance(obj, UUID):
#         return str(obj)
#     return old_default(self, obj)

# JSONEncoder.default = new_default

@login_required(login_url="/login")
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
    

@login_required(login_url="/login")
def staff_students(request):
    
    return render(request, "staff/students.html")


@login_required(login_url="/login")
def save_attendance_data(request):
    data = json.loads(request.body)
    unitId = data['unit']
    attendanceDate = data['attendance']
    sessionId = data['session']
    studentIds = data['student_data']
    session = Session.objects.get(id = sessionId)
    unit = Unit.objects.get(id =unitId)  
    
    # try:
        #  save attendance
    attendance = Attendance(unit=unit, attendance_date=attendanceDate, session=session)
    attendance.save()  
    for stud in studentIds:
        student = Student.objects.get(user=stud['id'])
        print(student)
        attendance_report = AttendanceReport(student=student, attendance=attendance, status=stud['status'])
        attendance_report.save()
        return HttpResponse("Attendance saved successfully")
    # except:
        # return HttpResponse("Error in saving attendance data")

@login_required(login_url="/login")  
def update_attendance(request):
    return render(request, "staff/update_attendance.html")