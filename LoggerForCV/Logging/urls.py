from django.conf.urls import url
from Logging.views import Logg, Test1, Test2

urlpatterns = [
	url(r'^$', Logg, name='Logging'),
	url(r'^test1/$', Test1, name='Test1'),
	url(r'^test2/$', Test2, name='Test2'),
]