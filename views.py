from django import http
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.template import loader
from django.template import RequestContext

from core import methods
from core import numi
from core import parser


MAX_SUBINTERVALS_NUMBER = 100000

def index(request):
    import logging
#    logging.info(request.LANGUAGE_CODE)
#    logging.info(request.COOKIES.get('django_language', 'none'))
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

def integrate(request):
    errors = []

    function_string = request.REQUEST['function']

    try:
        lower_limit = float(request.REQUEST['lowerLimit'])
        upper_limit = float(request.REQUEST['upperLimit'])
    except ValueError:
        errors.append('integration limits should be float numbers')

    try:
        subintervals_number = int(request.REQUEST['subintervalsNumber'])
        if subintervals_number <= 0:
            raise ValueError
    except ValueError:
        errors.append('number of subintervals should be positive integer')

    if subintervals_number > MAX_SUBINTERVALS_NUMBER:
        errors.append('number of subintervals should be not greater than %d' %
                      MAX_SUBINTERVALS_NUMBER)

    if not errors:
        methods_results, methods_errors = numi.integrate(function_string,
                                                         lower_limit,
                                                         upper_limit,
                                                         subintervals_number)
        errors += methods_errors
    else:
        methods_results = []

    return render_to_response('results.html',
                              { 'methods_results': methods_results,
                                'errors': errors },
                              RequestContext(request))

def about(request):
    return render_to_response('about.html', { 'methods' : methods.METHODS },
                              RequestContext(request))

def help(request):
    functions = []
    for function in parser.functions:
        if 'name' in function:
            functions.append({
                'name': function['name'],
                'desc': function.get('desc', 'No description')
            })

    return render_to_response('help.html', { 'functions' : functions },
                              RequestContext(request))


def server_error(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context:
        MEDIA_URL
            Path of static media (e.g. "media.example.org")
    """
    t = loader.get_template(template_name) # Requeres 500.html template.
    return http.HttpResponseServerError(t.render(RequestContext(request)))
