from django.conf.urls.defaults import patterns, url
from app.views import list

urlpatterns = patterns('app.views',
   url(r'^list/$', list, name='list'),
)
