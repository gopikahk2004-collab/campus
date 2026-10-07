from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('submit/', views.submit_request, name='submit_request'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('update/<int:pk>/', views.update_request, name='update_request'),
    path('delete/<int:pk>/', views.delete_request, name='delete_request'),
    
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('staff/update/<int:pk>/', views.update_request_status, name='update_request_status'),
]
