from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _

import uuid

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        self.password = user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, role=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        # Set the role for the superuser if a role argument is provided
        if role is not None:
            extra_fields['role'] = role

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    ROLE = (
        (1, _('Admin')),
        (2, _('Recruiter')),
        (3, _('Candidate'))
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=254, blank=True, default='')
    last_name = models.CharField(max_length=254, blank=True, default='')
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE, default=3)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # Personal Information
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    linkedin = models.URLField(max_length=254, blank=True, null=True)
    website = models.URLField(max_length=254, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_avatar(self):
        if self.avatar:
            return settings.MEDIA_URL + self.avatar.name
        else:
            return settings.STATIC_URL + 'img/blank_avatar.png'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)


    @property
    def is_admin(self):
        return self.role == 1

    @property
    def is_recruiter(self):
        return self.role == 2

    @property
    def is_candidate(self):
        return self.role == 3



