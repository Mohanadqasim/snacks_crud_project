from django.contrib import admin
from .models import Snack
# Register your models here.

class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'purchaser')
    list_filter = ('purchaser',)
    search_fields = ('name', 'description')

admin.site.register(Snack, SnackAdmin)