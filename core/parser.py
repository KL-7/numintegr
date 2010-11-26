from __future__ import division

import math

functions = [
    { 'local': 'pi','name': 'pi',
      'desc': 'pi constant (3.14159)', 'impl' : math.pi },
    { 'local': 'e', 'name': 'e',
      'desc': 'e costant (2.71828)', 'impl' : math.e },

    { 'name': 'x ** y', 'desc': 'x raised to the power of y' },

    { 'local': 'cos', 'name': 'cos(x)',
      'desc': 'trigonometric cosine of x', 'impl' : math.cos },
    { 'local': 'sin', 'name': 'sin(x)',
      'desc': 'trigonometric sine of x', 'impl' : math.sin },
    { 'local': 'tg', 'name': 'tg(x)',
      'desc': 'trigonometric tangent of x', 'impl' : math.tan },
    { 'local': 'ctg', 'name': 'ctg(x)',
      'desc': 'trigonometric cotangent of x', 'impl' : lambda x: 1 / math.tan(x) },

    { 'local': 'arccos', 'name': 'arccos(x)',
      'desc': 'arc cosine of x', 'impl' : math.acos },
    { 'local': 'arcsin', 'name': 'arcsin(x)',
      'desc': 'arc sine of x', 'impl' : math.asin },
    { 'local': 'arctg', 'name': 'arctg(x)',
      'desc': 'arc tangent of x', 'impl' : math.atan },
    { 'local': 'arcctg', 'name': 'arctg(x)',
      'desc': 'arc cotangent of x',
                  'impl': lambda x: math.pi / 2 - math.atan(x) },

    { 'local': 'ch', 'name': 'ch(x)',
      'desc': 'hyperbolic cosine of x', 'impl' : math.cosh },
    { 'local': 'sh', 'name': 'sh(x)',
      'desc': 'hyperbolic sine of x', 'impl' : math.sinh },
    { 'local': 'th', 'name': 'th(x)',
      'desc': 'hyperbolic tangent of x', 'impl' : math.tanh },
    { 'local': 'cth', 'name': 'cth(x)',
      'desc': 'hyperbolic cotangent of x',
                  'impl': lambda x: 1 / math.tanh(x) },

    { 'local': 'abs', 'name': 'abs(x)',
      'desc': 'absolute value of x', 'impl' : abs },
    { 'local': 'pow', 'name': 'pow(x, y)',
      'desc': 'x raised to the power of y', 'impl' : pow },
    { 'local': 'exp', 'name': 'exp(x)',
      'desc': 'e raised to the power of x', 'impl' : math.exp },
    { 'local': 'log', 'name': 'log(x, base)',
      'desc': 'logarithm of x to the given base', 'impl' : math.log },
    { 'local': 'ln', 'name': 'ln(x)',
      'desc': 'natural logarithm (base e) of x', 'impl' : math.log },
    { 'local': 'log10', 'name': 'log10(x)',
      'desc': 'base 10 logarithm of x', 'impl' : math.log10 },
    { 'local': 'sqrt', 'name': 'sqrt(x)',
      'desc': 'square root of x', 'impl' : math.sqrt },
]

eval_globals = {
    '__builtins__': None,
}

for function in functions:
    if 'local' in function and 'impl' in function:
        eval_globals[function['local']] = function['impl']


def parse_function(function_string):
    return eval('lambda x: ' + function_string, eval_globals)

