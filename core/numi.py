from __future__ import division

from django.utils.translation import ugettext_lazy as _
from methods import METHODS
from parser import parse_function

import logging
import math
import random
import traceback


def integrate(function_string, lower_limit=0, upper_limit=1,
              subintervals_number=100):
#    logging.info('funcion_string: %s, limits: [%s, %s], subs number: %s' %
#                 (function_string, lower_limit, upper_limit,
#                  subintervals_number))
    errors = []
    methods_results = []

    try:
        function = parse_function(function_string)
        for Method in METHODS:
            method = Method(function, lower_limit, upper_limit)
            result = method.integrate(subintervals_number)
            methods_results += [{
                                  'name': method.name,
                                  'description': method.desc,
                                  'result': result
                                }]
    except SyntaxError:
        errors.append(_('Failed to parse the function'))
    except NameError:
        errors.append(_('The function contains some undefined functions and/or '
                      'variables'))
    except ValueError:
        errors.append(_('The function is not defined on this interval'))
    except ZeroDivisionError:
        errors.append(_('The function is not defined on this interval '
                      '(zero division occured)'))
    except Exception, e:
        errors.append(_('Sorry, integration failed for unknown reason'))
        logging.error('Integration error: f="%s", lower_limit=%2.2e, '
                      'upper_limit=%2.2e, subintervals_number=%d' %
                      (function_string, lower_limit, upper_limit,
                       subintervals_number))
        logging.error(traceback.format_exc(e))

    return methods_results, errors

