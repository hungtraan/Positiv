import json
import datetime, operator
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import DayEntry, ExerciseType, Keyword, Highlight, Lowlight, Question

dateFormat = '%Y-%m-%d'

def index(request):
	return JsonResponse({'greeting':'Hello!'})
	
@csrf_exempt
def setRating(request):
	rawJSON = request.body.decode()
	jsonData = json.loads(rawJSON)

	date = datetime.datetime.strptime(jsonData['date'], dateFormat)
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

	date = datetime.datetime.strptime(jsonData['date'], dateFormat)
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
			ex['type'] = exercise.exerciseType.exerciseType
			ex['questions'] = []
			for qa in exercise.questionanswer_set.all():
				q = {}
				q['prompt'] = qa.question.prompt
				q['needResponse'] = qa.question.needResponse
				q['response'] = qa.response
				ex['questions'].append(q)

			#for highlight in exercise.highlight_set.all():
			#	response['highlights'].append(highlight.key)
			#for lowlight in exercise.lowlight_set.all():
			#	response['lowlights'].append(lowlight.key)

			response['exercises'].append(ex)
	except Exception:
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

@csrf_exempt
def getExercises(request):
	response = {}
	response['exercises'] = []

	for ex in ExerciseType.objects.all():
		response['exercises'].append(ex.exerciseType)

	jsonResponse = json.dumps(response)

	return HttpResponse(jsonResponse, content_type='application/json')


@csrf_exempt
def getQuestions(request):
	response = {}
	response['questions'] = []

	rawJSON = request.body.decode()
	jsonData = json.loads(rawJSON)
	
	exerciseType = jsonData['exercise']
	exercise = ExerciseType.objects.get(exerciseType__exact=exerciseType)
	questionSet = exercise.question_set.all()
	id_list = []
	prompt_list = []

	for question in questionSet:
		id_list.append(question.question_id)
		prompt_list.append(question.prompt)
	
	id_list_sorted, prompt_list_sorted = zip(*sorted(zip(id_list, prompt_list),
											 key=operator.itemgetter(0)))
	
	for i in range(len(id_list)):
		qDict = {id_list_sorted[i]:prompt_list_sorted[i]}
		response['questions'].append(qDict)

	jsonResponse = json.dumps(response)

	return HttpResponse(jsonResponse, content_type='application/json')


@csrf_exempt
def doExercise(request):
	rawJSON = request.body.decode()
	jsonData = json.loads(rawJSON)

	doDate = datetime.datetime.strptime(jsonData['date'], dateFormat)
	year = doDate.year
	day = doDate.day
	month = doDate.month

	try:
		requestEntry = DayEntry.objects.get(date__year=year,
											date__month=month,
											date__day=day)
	except Exception:
		requestDate = datetime.date(year, month, day)
		requestEntry = DayEntry(date=requestDate, score=requestScore, faceID=requestFace)
		requestEntry.save()

	exerciseType = ExerciseType.objects.get(exerciseType__exact=jsonData['exerciseType'])
	questionSet = exerciseType.question_set.all()
	answerList = jsonData['answers']
	exercise = requestEntry.exercise_set.create(exerciseType=exerciseType)

	for answer in answerList:
		q_id = list(answer.keys())[0]
		question = None
		for q in questionSet:
			if q.question_id == int(q_id):
				print("found")
				question = q
				break
		
		if question != None:
			print(answer[q_id]) 
			exercise.questionanswer_set.create(question=question, response=answer[q_id])

	print("done")
	exercise.save()
	requestEntry.save()

@csrf_exempt
def adf(request):
	pass




