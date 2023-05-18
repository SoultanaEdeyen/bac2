from django.urls import path
from .import views

urlpatterns = [
    path('etudiant/', views.getEtudiants),  
    path('etudiant/create/', views.createEtudiant),
    path('etudiant/<str:pk>/update/', views.updateEtudiant), 
    path('etudiant/<str:pk>/delete/', views.deleteEtudiant),  
    path('etudiant/<str:pk>/', views.getEtudiants),  
    path('prop/', views.getProps), 
    path('prop/create/', views.createProp), 
    path('prop/<str:pk>/update/', views.updateProp), 
    path('prop/<str:pk>/delete/', views.deleteProp),  
    path('prop/<str:pk>/', views.getProps), 
    path('anno/', views.getAnnos), 
    path('anno/create/', views.createAnno), 
    path('anno/<str:pk>/update/', views.updateAnno), 
    path('anno/<str:pk>/delete/', views.deleteAnno),  
    path('anno/<str:pk>/', views.getAnnos), 
      

]


         
   
