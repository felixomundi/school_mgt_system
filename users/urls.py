from django.urls import path
from django.contrib.auth import views as auth_views
from . import staff, student, views,superuser

urlpatterns = [     
     
     # auth views
     path('',views.loginuser, name='login'),
     path('logout',views.logoutuser,name='logout'),    
     path('change-password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html',
     success_url = '/change-password/done'
     ), name='change-password'),
     path('change-password/done', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_done.html')),

     path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password"),
     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"), 
    
    
    
    # admin views 
     path("home",superuser.home, name="home"),
     path ('add_course', superuser.add_course, name="add_course"),
     path ('courses', superuser.courses, name="courses"),     
     path('edit_course/<str:pk>/',superuser.edit_course, name="edit_course"),
     path('delete_course/<slug:pk>',superuser.delete_course, name="delete_course"),
     path('students',superuser.students, name="students"),     
     path("add_student",superuser.add_student, name="add_student"),     
    #  path("edit_student/<slug:pk>",superuser.edit_student, name="edit_student"),
     path("delete_student/<slug:pk>",superuser.delete_student, name="delete_student"),
     path('staff',superuser.staff, name="staff"),
     path('add_staff',superuser.add_staff, name="add_staff"),
     path('delete_staff/<slug:pk>',superuser.delete_staff, name="delete_staff"),     
     path('add_unit',superuser.add_unit, name="add_unit"),
     path('delete_unit/<slug:pk>',superuser.delete_unit, name="delete_unit"),
     path('admin_units',superuser.admin_units, name="admin_units"),
     path('edit_unit/<slug:pk>',superuser.edit_unit, name="edit_unit"),
     path('add_session',superuser.add_session, name="add_session"),
     path('admin_sessions',superuser.admin_sessions, name="admin_sessions"),
     path('delete_session/<slug:pk>',superuser.delete_session, name="delete_session"),
     path('edit_session/<slug:pk>',superuser.edit_session, name="edit_session"),
     path('admin_profile',superuser.admin_profile, name="admin_profile"),
     path('admin_profile_update',superuser.admin_profile_update, name="admin_profile_update"),
     
     
     # staff views
     path("staff_home", staff.staff_home, name="staff_home"),
     path('get_students',staff.get_students, name="get_students"),
     path("save_attendance_data", staff.save_attendance_data, name="save_attendance_data"),
     path("update_attendance", staff.update_attendance, name="update_attendance"),
     path("get_attendance_dates", staff.get_attendance_dates, name="get_attendance_dates"),
     path("get_attendance_student", staff.get_attendance_student, name="get_attendance_student"),
     path("add_marks", staff.add_marks, name="add_marks"),
     path("save_marks", staff.save_marks, name="save_marks"),
     path("take_attendance", staff.take_attendance, name="take_attendance"),
     path ('units', staff.units, name="units"),
     path ('staff_profile', staff.staff_profile, name="staff_profile"),
     path ('staff_profile_update', staff.staff_profile_update, name="staff_profile_update"),
     
     # student
      path ('student_home', student.student_home, name="student_home"),
      path ('student_profile', student.student_profile, name="student_profile"),
      path ('student_profile_update', student.student_profile_update, name="student_profile_update"),
      path ('view_result', student.view_result, name="view_result"),
      path ('student_units', student.student_units, name="student_units"),
     
  ]
