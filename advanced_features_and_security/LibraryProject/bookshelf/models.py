from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
(None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
class CustomUserManager(BaseUserManager):", "create_user", "create_superuser
can_create , can_delete