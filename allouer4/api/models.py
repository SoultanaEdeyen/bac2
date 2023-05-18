from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=30, default='student')

    objects = UserManager()
    

    class Meta:
        abstract = True

class Proprietaire(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    
    # Ajoutez les attributs spécifiques aux propriétaires ici
    pass

class Etudiant(User):
    etudiant_id = models.AutoField(primary_key=True)
    # Ajoutez les attributs spécifiques aux étudiants ici
    pass
