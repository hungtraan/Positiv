from django.views.decorators.csrf import csrf_exempt
import requests
import json

@csrf_exempt
def test_conn(request):
	data = {'date':'11-19-2016', 'score':'80', 'faceID':'4'}
	data.encode('utf-8')
	url = 'http://localhost:8000/api/setRating'
	content = json.dumps(data)

	r = requests.post(url, data=content)



test_conn()
