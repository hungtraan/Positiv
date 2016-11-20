from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^diary', views.diary, name='diary'),
    url(r'^graphs', views.graphs, name='graphs'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^reflection1', views.reflection1, name='reflection1'),
    url(r'^reflection2', views.reflection2, name='reflection2'),
    url(r'^reflection3', views.reflection3, name='reflection3'),
    url(r'^reflection4', views.reflection4, name='reflection4'),
]