from django.conf.urls import url
from demo import views

urlpatterns = [
                url(r'^$', views.index, name='index'),
                url(r'fatec', views.fatec, name='fatec'),
                url(r'seti', views.seti, name='seti')
              ]
