from django.db import models
from django.utils import timezone

class DayEntry(models.Model):
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	score = models.IntegerField(default = -1)
	faceID = models.IntegerField(default = -1)

	def __str__(self):
		year = self.date.year
		month = self.date.month
		day = self.date.day
		currentDate = str(year) + "/" + str(month) + "/" + str(day)
		return currentDate + " " + str(self.score) + " " + str(self.faceID)

	def getDate(self):
		return self.date.strftime('%m-%d-%Y')

class ExerciseType(models.Model):
	exerciseType = models.CharField(max_length=100)

	def __str__(self):
		return self.exerciseType

class Exercise(models.Model):
	exerciseType = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, null=True)
	dayEntry = models.ForeignKey(DayEntry, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.exerciseType.exerciseType + " - " \
			+ self.dayEntry.date.strftime('%m-%d-%Y')

class Keyword(models.Model):
	word = models.CharField(max_length=100)
	exercise = models.ManyToManyField(ExerciseType, blank=True)

	def __str__(self):
		return self.word

class Highlight(models.Model):
	key = models.CharField(max_length=100)
	exercise = models.ManyToManyField(ExerciseType, blank=True)

	def __str__(self):
		return self.key

class Lowlight(models.Model):
	key = models.CharField(max_length=100)
	exercise = models.ManyToManyField(ExerciseType, blank=True)

	def __str__(self):
		return self.key

class Question(models.Model):
	question_id = models.IntegerField(default=-1)
	prompt = models.CharField(max_length=1000)
	needResponse = models.BooleanField(default=False)
	exercise = models.ForeignKey(ExerciseType, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return str(self.question_id) + ". " + self.prompt

class QuestionAnswer(models.Model):
	response = models.TextField()
	exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.question.prompt + " - " + self.response

