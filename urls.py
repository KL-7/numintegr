import settings
import views

from django.conf.urls.defaults import *


# main logic urls
urlpatterns = patterns('',
    ('^$', views.index),
    ('^integrate/$', views.integrate),
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

# 500 error handler
handler500 = views.server_error

# add /500 and /404 urls for testing
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^500/$', handler500),
        (r'^404/$', handler404)
    )
