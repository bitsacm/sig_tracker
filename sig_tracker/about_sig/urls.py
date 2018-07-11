from django.conf.urls import url
from . import views

app_name = 'about_sig'
urlpatterns = [
    #/about_sig/
    url(r'^', views.index, name='index'),
    #/about_sig/1/
    url(r'^(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
]
