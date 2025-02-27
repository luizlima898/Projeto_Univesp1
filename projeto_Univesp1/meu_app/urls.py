from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path,
include
urlpatterns = [path('', views, home, name = 'home'),]

 
urlpatterns = [
     path('admin/', admin.site.urls),
     path('',
include('projeto_Univesp1.urls')),]
