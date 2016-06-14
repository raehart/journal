from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.entries_list, name='list'),
    url(r'^(?P<pk>\d+)$', views.entry_detail, name='detail')
]