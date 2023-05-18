
from django.contrib import admin
from django.urls import path,include
#from api.views import SignupView, LoginView

from django.urls import path
from api .views import ProprietaireSignupView, EtudiantSignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),

    
]

