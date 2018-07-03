from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('sig/', views.sig, name='sig'),
    path('<int:sig_id>/', views.sig_details, name='detail')
]
