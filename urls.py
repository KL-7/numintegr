import settings

from django.conf.urls.defaults import *
from views import index, integrate


# main logic urls
urlpatterns = patterns('',
    ('^$', index),
    ('^integrate/$', integrate),
)

# static files urls
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
)

# static pages urls
urlpatterns += patterns('django.views.generic.simple',
    (r'^about/$', 'direct_to_template', { 'template': 'about.html' }),
    (r'^help/$',  'direct_to_template', { 'template': 'help.html' }),
)
