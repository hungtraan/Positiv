from django.db import models
from django.utils import timezone

class DayEntry(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	score = models.IntegerField(default = -1)
	faceID = models.IntegerField(default = -1)

	def getDate(self):
		return self.date.strftime('%m-%d-%Y')

class Exercise(models.Model):
	time = models.DateTimeField(auto_now=False, auto_now_add=False)
	exerciseType = models.CharField(max_length=100)
	dayEntry = models.ManyToManyField(DayEntry)

class Keyword(models.Model):
	word = models.CharField(max_length=100)
	exercise = models.ManyToManyField(Exercise)

class Highlight(models.Model):
	key = models.CharField(max_length=100)
	exercise = models.ManyToManyField(Exercise)

class Lowlight(models.Model):
	key = models.CharField(max_length=100)
	exercise = models.ManyToManyField(Exercise)

class Question(models.Model):
	prompt = models.CharField(max_length=1000)
	response = models.TextField()
	needResponse = models.BooleanField(default=False)
	exercise = models.ManyToManyField(Exercise)

	
