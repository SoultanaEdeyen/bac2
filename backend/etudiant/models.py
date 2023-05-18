from django.db import models

# Create your models here.

class Prop(models.Model):
    
    nom_user = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    mot_pass = models.CharField(max_length=10)
    
    

class Etudiant(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    mot_pass = models.CharField(max_length=10)
    carte_etud = models.TextField()


class Anno(models.Model):
    description = models.TextField()
    photo = models.TextField()
    etat =  models.CharField(max_length=30)
    prix = models.FloatField(max_length=20)
    add = models.CharField(max_length=30)
    numTel = models.CharField(max_length=30)


    

    



































