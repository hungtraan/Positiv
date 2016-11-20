import requests, json
from django.test import TestCase
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Create your tests here.

base_url = 'http://localhost:8000/api/'

@csrf_exempt
def test_setRating(request):
	data = {'date':'2016-11-14', 'score':'80', 'faceID':'4'}
	url = base_url + 'setRating'
	content = json.dumps(data)

	r = requests.post(url, data=content)

	return HttpResponse("Done!")

@csrf_exempt
def test_getEntry(request):
	data = {'date':'2016-11-19'}

	url = base_url + 'getEntry'
	content = json.dumps(data)

	r = requests.post(url, data=content)
	#jsonData = json.loads(r.content)

	return HttpResponse(str(r.content))

@csrf_exempt
def test_graph_7days(request):
	url = base_url + "graph_7days"
	r = requests.get(url)
	
	return HttpResponse(str(r.content))

@csrf_exempt
def test_getExercises(request):
	url = base_url + "getExercises"
	r = requests.get(url)

	return HttpResponse(str(r.content))

@csrf_exempt
def test_getQuestions(request):
	data = {'exercise': 'Reflection'}
	url = base_url + "getQuestions"
	content = json.dumps(data)

	r = requests.post(url, data=content)

	return HttpResponse(str(r.content))

@csrf_exempt
def test_doExercise(request):
	data = {'date':'2016-11-19', 'exerciseType':'Reflection',
			'answers': [{'1': 'Great!'}, {'2': 'Work, Academic. All are good, I\'m the best.'}, 
						{'3': 'Money. I lost everything.'}, {'4': 'Since I\'m stupid'}]}
	url = base_url + 'doExercise'
	content = json.dumps(data)

	r = requests.post(url, data=content)

	return HttpResponse("Done!")




