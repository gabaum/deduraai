from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
	url(r'^problems/$', 'problems.views.index'),
	url(r'^problems/(?P<problem_id>\d+)/$', 'problems.views.detail'),

)
