
#from django.db import models

#from django.contrib.auth.models import User, AbstractUser, BaseUserManager
#
# from django_resized import ResizedImageField

# Create your models here.
#def upload_to(inst, filename):
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

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

class Proprietaire(User):
    user_permissions = models.ManyToManyField(Permission, related_name="proprietaire_user_permissions")

class Etudiant(User):
    groups = models.ManyToManyField(Group, related_name="etudiant_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="etudiant_user_permissions")


class LogEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ...
    pass
    # Autres champs du modèle LogEntry


    # Ajoutez les attributs spécifiques aux étudiants ici

    # Ajoutez les attributs spécifiques aux étudiants ici



"""class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('proprietaire', 'Propriétaire'),
        ('etudiant', 'Étudiant'),
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Étudiant')
    
    # autres champs de votre modèle User

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()"""




