from django.conf.urls import url
from . import views


app_name = 'dev_sig'
urlpatterns = [
    #/dev_sig/
    url(r'^', views.index, name='index'),
    #/dev_sig/1/
    url(r'^(?P<sig_id>[0-9]+)/$', views.detail, name='detail'),
]
