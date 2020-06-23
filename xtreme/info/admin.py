from django.contrib import admin
from .models import Tech
# Register your models here.

class TechAdmin(admin.ModelAdmin):
    
    readonly_fields = ("created", "updated")

admin.site.register(Tech, TechAdmin)
