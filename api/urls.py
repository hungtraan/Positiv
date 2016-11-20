from django.conf.urls import url

from . import views, tests

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^setRating', views.setRating, name='setRating'),
	url(r'^getEntry', views.getEntry, name='getEntry'),
	url(r'^graph_7days', views.graph_7days, name='graph_7days'),
	url(r'^testconn', tests.test_conn),
	url(r'^testget', tests.test_get),
	url(r'^testgraph_7days', tests.test_graph_7days),
]
