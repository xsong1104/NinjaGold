from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.getMoney),
    url(r'^reset$', views.reset)
]
