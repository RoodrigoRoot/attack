from django.contrib import admin
from .models import *
# Register your models here.


class CardAdmin(admin.ModelAdmin):

    readonly_fields = ("created", "updated")

admin.site.register(Card, CardAdmin)


class QuestionAdmin(admin.ModelAdmin):

    readonly_fields = ("created", "updated")

admin.site.register(Question, QuestionAdmin)
