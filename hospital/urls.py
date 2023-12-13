from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('doctors/', views.doctor_list_view, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('', views.inicio, name='inicio'),
    
    #crud
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('accounts/profile/', views.profile_view, name='profile'),
    #test
    path('forms/', views.forms, name='forms'),
    path('cita_list/', views.cita_list, name='cita_list'),
    path('eliminar_cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
