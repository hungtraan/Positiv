from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^setRating', views.setRating, name='setRating'),
	url(r'^getEntry', views.getEntry, name='getEntry'),
	url(r'^testconn', views.test_conn),
	url(r'^testget', views.test_get),
]
