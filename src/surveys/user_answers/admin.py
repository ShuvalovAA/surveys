from django.contrib import admin

from .models import UserAnswer

@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    pass
