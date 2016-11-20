from django.conf.urls import url

from . import views, tests

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^setRating', views.setRating, name='setRating'),
	url(r'^getEntry', views.getEntry, name='getEntry'),
	url(r'^graph_7days', views.graph_7days, name='graph_7days'),
	url(r'^getExercises', views.getExercises, name='getExercises'),
	url(r'^getQuestions', views.getQuestions, name='getQuestions'),
	url(r'^doExercise', views.doExercise, name='doExercise'),
	url(r'^test_setRating', tests.test_setRating),
	url(r'^test_getEntry', tests.test_getEntry),
	url(r'^test_graph_7days', tests.test_graph_7days),
	url(r'^test_getExercises', tests.test_getExercises),
	url(r'^test_getQuestions', tests.test_getQuestions),
	url(r'^test_doExercise', tests.test_doExercise),
]
