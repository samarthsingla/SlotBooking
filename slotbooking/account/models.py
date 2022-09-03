from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, name,type, password=None):
        if not email:
            raise ValueError("Must have an email address")
        if not username:
            raise ValueError("Must have an email address")
        if not name:
            raise ValueError("Must have a name")

        user = self.model(
            email = self.normalize_email(email), 
            username = username, 
            name = name, 
            type = type
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password, type):

        user = self.create_user(
            email = self.normalize_email(email), 
            username = username, 
            name = name, 
            password = password,
            type = type
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    TYPE_CHOICES = [
        ('student', 'Student'), 
        ('staff', "Staff"),
        ('admin', "Admin"),
    ]
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # is_instructor = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =  ['email', 'name', 'type']

    objects = MyAccountManager()
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
        
    def basicInfo(self):
        obj = {}
        obj['name'] = self.name
        obj['username'] = self.username
        # obj['is_instructor'] = self.is_instructor
        obj['type'] = self.type
        return obj

    




