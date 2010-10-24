from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from core import numi

def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))

def integrate(request):
    errors = []

    function_string = request.POST['function']

    try:
        lower_limit = float(request.POST['lowerLimit'])
        upper_limit = float(request.POST['upperLimit'])
    except ValueError:
        errors.append('integration limits should be float numbers')

    try:
        subintervals_number = int(request.POST['subintervalsNumber'])
        if subintervals_number <= 0:
            raise ValueError
    except ValueError:
        errors.append('number of subintervals should be positive integer')

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
