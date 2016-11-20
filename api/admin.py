from django.contrib import admin

from .models import Question, DayEntry, ExerciseType, Highlight, Lowlight, QuestionAnswer, Exercise

admin.site.register(DayEntry)
admin.site.register(ExerciseType)
admin.site.register(Exercise)
admin.site.register(Question)
admin.site.register(QuestionAnswer)
admin.site.register(Highlight)
admin.site.register(Lowlight)
