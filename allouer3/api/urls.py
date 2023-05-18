from django.contrib import admin
from django.urls import path,include
from .views import EtudiantSignupView, ProprietaireSignupView #LoginView


urlpatterns = [
    path('signupEtudiant/', EtudiantSignupView.as_view(), name="signup"),
    path('signupProprietaire/', ProprietaireSignupView.as_view(), name="signup"),
    #path('login/', LoginView.as_view(), name="login"),

    
]

