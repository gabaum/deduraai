from django.conf.urls.defaults import patterns, url, include
from haystack.views import search_view_factory

from search.forms import SearchForm


urlpatterns = patterns('',

        url(r'^',
            search_view_factory(form_class=SearchForm),
            name='search'),

)
