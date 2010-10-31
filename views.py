from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from core import numi


MAX_SUBINTERVALS_NUMBER = 100000

def index(request):
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
