from django.urls import include, path
from . import views


urlpatterns = [
    path('createAccount/', views.createAccount),
    path('getDoctors/', views.getDoctorsInformation),
    path('getPatients/', views.getPatientsInformation),
    path('getEmployees/', views.getEmployeesInformation),
    path('delUser/', views.delUser),
    path('updateDoc/', views.updateDoc),
    path('updatePat/', views.updatePat),
    path('updateEmp/', views.updateEmp),
    path('createReservation/', views.createReservation),
    path('getReservations/', views.getReservations),
    path('updateRes/', views.updateRes),
    path('deleteRes/', views.delRes),
]
