from django.contrib import admin
from . import models


@admin.register(models.Question)
class questionAdmin(admin.ModelAdmin):

    list_display =(
       'message',

    )

@admin.register(models.Question_set)
class question_setAdmin(admin.ModelAdmin):

    list_display = (
        'question_list',

    )
