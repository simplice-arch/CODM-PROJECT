from django.contrib import admin
from .models import Utilisateur

# Register your models here.
@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'created_at')
    list_filter = ('email', )
    search_fields = ('username',)