from django.contrib import admin

from .models import Question, DayEntry, Exercise, Highlight, Lowlight

admin.site.register(DayEntry)
admin.site.register(Exercise)
admin.site.register(Question)
admin.site.register(Highlight)
admin.site.register(Lowlight)
