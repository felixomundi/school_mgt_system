from django.contrib import admin
from users.models import User,Course,Session,Student ,Staff,Unit,Attendance,AttendanceReport,StudentResult
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 



class AdminUser(BaseUserAdmin):
    list_display=('email','last_login','is_active','is_student','is_parent','is_lecturer','is_admin','is_staff','is_superuser','date_registered','date_updated')
    search_fields=('email','last_login','is_active','is_student','is_parent','is_lecturer','is_admin','is_staff','is_superuser','date_registered','date_updated')
    readonly_fields=('date_registered','last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()
    add_fieldsets=(
        (None,{
            'classes':('wide'),        
            'fields':('email','first_name','last_name','role','password1','password2'),
        }),
    )
    ordering= ('email',)
    
admin.site.register(User,AdminUser)    


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','country','created_at','updated_at')  
#     ordering = ('-pk',)
#     search_fields = ('user','country','created_at','updated_at')
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name","created_at","updated_at")
    ordering = ("-pk",)  
    search_fields =  ("name","created_at","updated_at")

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name','start','end')  
    ordering = ('-pk',)
    search_fields = ('name','start','end')
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',"gender","course","year_of_study","created_at",'updated_at')  
    ordering = ('-pk',)
    search_fields = ('user',"gender","course","year_of_study","created_at",'updated_at')    
    
    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user',"gender","created_at",'updated_at')  
    ordering = ('-pk',)
    search_fields = ('user',"gender","created_at",'updated_at')        
    

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name","course",'staff',"created_at",'updated_at')  
    ordering = ('-pk',)
    search_fields = ("name","course",'staff',"created_at",'updated_at')            
    
    


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("unit",'session',"created_at",'updated_at')  
    ordering = ('-pk',)
    search_fields = ("unit",'session',"created_at",'updated_at')                
    
    
    

@admin.register(AttendanceReport)
class AttendanceReportAdmin(admin.ModelAdmin):
    list_display = ("attendance",'student',"created_at",'updated_at')  
    ordering = ('-pk',)
    search_fields = ("attendance",'student',"created_at",'updated_at')                
    
@admin.register(StudentResult)
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ("student","unit","unit_exam_marks","unit_assignment_marks","total_marks","created_at","updated_at")
    ordering = ["-pk"]
    search_fields = ["student","unit","unit_exam_marks","unit_assignment_marks","created_at","updated_at"]    