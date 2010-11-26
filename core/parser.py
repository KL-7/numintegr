from __future__ import division

from django.utils.translation import ugettext_lazy as _

import math


functions = [
    { 'local': 'pi','name': 'pi',
      'desc': _('pi constant (3.14159)'), 'impl' : math.pi },
    { 'local': 'e', 'name': 'e',
      'desc': _('e costant (2.71828)'), 'impl' : math.e },

    { 'name': 'x ** y', 'desc': _('x raised to the power of y') },

    { 'local': 'cos', 'name': 'cos(x)',
      'desc': _('trigonometric cosine of x'), 'impl' : math.cos },
    { 'local': 'sin', 'name': 'sin(x)',
      'desc': _('trigonometric sine of x'), 'impl' : math.sin },
    { 'local': 'tg', 'name': 'tg(x)',
      'desc': _('trigonometric tangent of x'), 'impl' : math.tan },
    { 'local': 'ctg', 'name': 'ctg(x)',
      'desc': _('trigonometric cotangent of x'), 'impl' : lambda x: 1 / math.tan(x) },

    { 'local': 'arccos', 'name': 'arccos(x)',
      'desc': _('arc cosine of x'), 'impl' : math.acos },
    { 'local': 'arcsin', 'name': 'arcsin(x)',
      'desc': _('arc sine of x'), 'impl' : math.asin },
    { 'local': 'arctg', 'name': 'arctg(x)',
      'desc': _('arc tangent of x'), 'impl' : math.atan },
    { 'local': 'arcctg', 'name': 'arctg(x)',
      'desc': _('arc cotangent of x'),
                  'impl': lambda x: math.pi / 2 - math.atan(x) },

    { 'local': 'ch', 'name': 'ch(x)',
      'desc': _('hyperbolic cosine of x'), 'impl' : math.cosh },
    { 'local': 'sh', 'name': 'sh(x)',
      'desc': _('hyperbolic sine of x'), 'impl' : math.sinh },
    { 'local': 'th', 'name': 'th(x)',
      'desc': _('hyperbolic tangent of x'), 'impl' : math.tanh },
    { 'local': 'cth', 'name': 'cth(x)',
      'desc': _('hyperbolic cotangent of x'),
                  'impl': lambda x: 1 / math.tanh(x) },

    { 'local': 'abs', 'name': 'abs(x)',
      'desc': _('absolute value of x'), 'impl' : abs },
    { 'local': 'pow', 'name': 'pow(x, y)',
      'desc': _('x raised to the power of y'), 'impl' : pow },
    { 'local': 'exp', 'name': 'exp(x)',
      'desc': _('e raised to the power of x'), 'impl' : math.exp },
    { 'local': 'log', 'name': 'log(x, base)',
      'desc': _('logarithm of x to the given base'), 'impl' : math.log },
    { 'local': 'ln', 'name': 'ln(x)',
      'desc': _('natural logarithm (base e) of x'), 'impl' : math.log },
    { 'local': 'log10', 'name': 'log10(x)',
      'desc': _('base 10 logarithm of x'), 'impl' : math.log10 },
    { 'local': 'sqrt', 'name': 'sqrt(x)',
      'desc': _('square root of x'), 'impl' : math.sqrt },
]

eval_globals = {
    '__builtins__': None,
}

for function in functions:
    if 'local' in function and 'impl' in function:
        eval_globals[function['local']] = function['impl']


def parse_function(function_string):
    return eval('lambda x: ' + function_string, eval_globals)

