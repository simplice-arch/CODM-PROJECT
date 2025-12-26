from django.contrib import admin
from .models import Utilisateur

# Register your models here.
@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'date_joined', 'is_active', 'is_superuser', 'is_staff')
    list_filter = ('email', )
    search_fields = ('username',)