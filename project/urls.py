from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('users.urls')), 
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "" 

handler404="helpers.views.handle_not_found"
