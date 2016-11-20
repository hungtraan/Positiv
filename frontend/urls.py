from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^diary', views.diary, name='diary'),
    url(r'^graphs', views.graphs, name='graphs'),
    url(r'^profile', views.profile, name='profile'),
]