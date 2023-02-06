from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import staff
urlpatterns = [
     path("",views.home, name="home"),
     path('login',views.loginuser, name='login'),
     path('logout',views.logoutuser,name='logout'),    
     path('change-password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html',
     success_url = '/'
     ), name='change-password'),
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password"),
     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"), 
     path("take_attendance", views.take_attendance, name="take_attendance"),
     path ('units', views.units, name="units"),
     path ('add_course', views.add_course, name="add_course"),
     path ('courses', views.courses, name="courses"),     
     path('edit_course/<str:pk>/',views.edit_course, name="edit_course"),
     path('students',views.students, name="students"),     
     path("add_student",views.add_student, name="add_student"),     
     path("edit_student/<slug:pk>",views.edit_student, name="edit_student"),
     path('staff',views.staff, name="staff"),
     path('add_staff',views.add_staff, name="add_staff"),
     path('add_unit',views.add_unit, name="add_unit"),
     path('admin_units',views.admin_units, name="admin_units"),
     path('edit_unit/<slug:pk>',views.edit_unit, name="edit_unit"),
     path('add_session',views.add_session, name="add_session"),
     path('admin_sessions',views.admin_sessions, name="admin_sessions"),
     path('edit_session/<slug:pk>',views.edit_session, name="edit_session"),
     
     ### Staff
     path('get_students',staff.get_students, name="get_students"),
     path("save_attendance_data", staff.save_attendance_data, name="save_attendance_data"),
     path("update_attendance", staff.update_attendance, name="update_attendance"),
  ]
