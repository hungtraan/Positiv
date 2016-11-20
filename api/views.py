import json
import datetime
import requests
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import DayEntry, Exercise, Keyword, Highlight, Lowlight, Question

def index(request):
	return JsonResponse({'greeting':'Hello!'})
	

@csrf_exempt
def setRating(request):
	rawJSON = request.body.decode()
	jsonData = json.loads(rawJSON)

	date = datetime.datetime.strptime(jsonData['date'], '%m-%d-%Y')
	year = date.year
	day = date.day
	month = date.month

	result = None

	try:
		requestEntry = DayEntry.objects.get(date__year=year,
											date__month=month,
											date__day=day)
		requestEntry.score = int(jsonData['score'])
		requestEntry.faceID = int(jsonData['faceID'])
		requestEntry.save()
	except Exception:
		requestDate = datetime.date(year, month, day)
		requestScore = int(jsonData['score'])
		requestFace = int(jsonData['faceID'])
		newEntry = DayEntry(date=requestDate, score=requestScore, faceID=requestFace)
		newEntry.save()

@csrf_exempt
def getEntry(request):
	response = {}
	rawJSON = request.body.decode()
	jsonData = json.loads(rawJSON)

	date = datetime.datetime.strptime(jsonData['date'], '%m-%d-%Y')
	year = date.year
	month = date.month
	day = date.day

	try:
		entry = DayEntry.objects.get(date__year=year,
											date__month=month,
											date__day=day)
		response['date'] = str(entry.date)
		response['score'] = str(entry.score)
		response['faceID'] = str(entry.faceID)
		response['exercises'] = []
		response['highlights'] = []
		response['lowlights'] = []
			
		for exercise in entry.exercise_set.all():
			ex = {}
			ex['type'] = exercise.exerciseType
			ex['questions'] = []
			for question in exercise.question_set.all():
				q = {}
				q['prompt'] = question.prompt
				q['needResponse'] = question.needResponse
				q['response'] = question.response
				ex['questions'].append(q)

			for highlight in exercise.highlight_set.all():
				response['highlights'].append(highlight.key)
			for lowlight in exercise.lowlight_set.all():
				response['lowlights'].append(lowlight.key)

			response['exercises'].append(ex)
	except Exception:
		print("lola")
		pass

	jsonResponse = json.dumps(response)

	return HttpResponse(jsonResponse, content_type='application/json')

@csrf_exempt
def graph_7days(request):
	response = {}
	response['data'] = []
	today = datetime.datetime.today()

	for daysAgo in range(7):
		dayBefore = today - datetime.timedelta(days=daysAgo)
		print(str(dayBefore))
		dayDataDict = {}
		dayDataDict['date'] = str(dayBefore.year) + "/" + str(dayBefore.month)\
							  + "/" + str(dayBefore.day)
		try:
			dayData = DayEntry.objects.get(date__year=dayBefore.year,
										   date__month=dayBefore.month,
										   date__day=dayBefore.day)
			score = dayData.score
			faceID = dayData.faceID
		except Exception:
			score = 0
			faceID = 0
		
		dayDataDict['score'] = score
		dayDataDict['faceID'] = faceID
		response['data'].append(dayDataDict)

	jsonResponse = json.dumps(response)

	return HttpResponse(jsonResponse, content_type='application/json')

#@csrf_exempt





