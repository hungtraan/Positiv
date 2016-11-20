import json
import datetime
import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import DayEntry, Exercise, Keyword, Highlight, Lowlight, Question

def index(request):
	return JsonResponse({'greeting':'Hello!'})
	
@csrf_exempt
def test_conn(request):
	data = {'date':'11-19-2016', 'score':'85', 'faceID':'4'}
	url = 'http://localhost:8000/api/setRating'
	content = json.dumps(data)

	r = requests.post(url, data=content)

@csrf_exempt
def test_get(request):
	data = {'date':'11-19-2016'}

	url = 'http://localhost:8000/api/getEntry'
	content = json.dumps(data)

	r = requests.post(url, data=content)
	#jsonData = json.loads(r.content)

	return HttpResponse(str(r.content))

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
		print("lololala")
		pass

	jsonResponse = json.dumps(response)

	return HttpResponse(jsonResponse, content_type='application/json')
