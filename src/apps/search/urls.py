from django.conf.urls.defaults import patterns, url, include


ulrlpatterns = patterns('',
    (r'^',include('haystack.urls')), #just redirects everything to haystack

)
