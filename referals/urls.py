from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('sign_up/', views.signUpView, name='sign-up'),
    path('<str:ref_code>/', views.ref_sign_up, name='ref_sign_up'),
]