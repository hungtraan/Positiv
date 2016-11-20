import requests
from django.test import TestCase
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse

# Create your tests here.

@csrf_exempt
def test_conn(request):
	data = {'date':'11-13-2016', 'score':'83', 'faceID':'4'}
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
def test_graph_7days(request):
	url = 'http://localhost:8000/api/graph_7days'
	r = requests.get(url)
	
	return HttpResponse(str(r.content))
