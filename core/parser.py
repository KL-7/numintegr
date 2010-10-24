from __future__ import division

import math


eval_globals = {
    '__builtins__': None,

    'pi'     : math.pi,
    'e'      : math.e,

    'cos'    : math.cos,
    'sin'    : math.sin,
    'tg'     : math.tan,
    'ctg'    : lambda x: 1 / math.tan(x),

    'arccos' : math.acos,
    'arcsin' : math.asin,
    'arctg'  : math.atan,
    'arcctg' : lambda x: math.pi / 2 - math.atan(x),

    'ch'     : math.cosh,
    'sh'     : math.sinh,
    'th'     : math.tanh,
    'cth'    : lambda x: 1 / math.tanh(x),

#    'arcch'  : math.acosh,
#    'arcsh'  : math.asinh,
#    'arcth'  : math.atanh,
#    'arccth' : lambda x: 1 / math.atanh(x),

    'abs'    : abs,
    'pow'    : pow,
    'exp'    : math.exp,
    'log'    : math.log,    # log(x, base)
    'ln'     : math.log,
    'log10'  : math.log10,
    'sqrt'   : math.sqrt
}

def parse_function(function_string):
    return eval('lambda x: ' + function_string, eval_globals)

