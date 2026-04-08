from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.layout, name='layout'),
    path('patient/', views.patient_form, name='patient_form'),
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('toggle/<int:id>/', views.toggle_status, name='toggle_status'),
    path('patient/<int:id>/', views.patient_detail, name='patient_detail'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/logout/', views.doctor_logout, name='doctor_logout'),
]