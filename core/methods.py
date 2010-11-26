from __future__ import division

from django.utils.translation import ugettext_lazy as _


class NumericalIntegrationMethod(object):

    name = ''

    desc = ''

    def __init__(self, function, lower_limit, upper_limit):
        self.function = function
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def subinterval_size(self, subinterval_number):
        return (self.upper_limit - self.lower_limit) / subinterval_number

    def _calculate(self, subinervals_number, subinterval_size):
        raise NotImplementedError("Calculate method should be implemented.")

    def integrate(self, subintervals_number):
        return self._calculate(subintervals_number,
                               self.subinterval_size(subintervals_number))


class RectanglesMethod(NumericalIntegrationMethod):

    name = 'Rectangles rule'

    desc = '''Computes an approximation to a definite integral, made
by finding the area of a collection of rectangles whose heights are determined
by the values of the function.'''

    ALPHA = 0

    def _calculate(self, n, h):
        xk = [self.lower_limit + h * (i + self.ALPHA) for i in xrange(n)]
#        import logging
#        logging.info('%s: %s, %s' % (self.name, ['%2.2f' % x for x in xk],
#                                     ['%2.2f' % self.function(x) for x in xk]))
        return h * sum(map(self.function, xk))


class LeftRectanglesMethod(RectanglesMethod):

    name = _('Left rectangles rule')

    desc = _('''Approximate function f on subinterval [a, b] with constant a
function equal to f(a) on [a, b].''')


class RightRectanglesMethod(RectanglesMethod):

    name = _('Right rectangles rule')

    desc = _('''Approximate function f on subinterval [a, b] with constant a
function equal to f(b) on [a, b].''')

    ALPHA = 1


class InnerRectanglesMethod(RectanglesMethod):

    name = _('Inner rectangles rule')

    desc = _('''Approximate function f on subinterval [a, b] with constant a
function equal to f((a + b) / 2) on [a, b].''')

    ALPHA = 0.5


class TrapezoidalMethod(NumericalIntegrationMethod):

    name = _('Trapezoidal rule')

    desc = _('''Approximate function f on subinterval [a, b] with a polynomial
of degree 1 which  passes through the points (a, f(a)) and (b, f(b)).''')

    def _calculate(self, n, h):
        fa = self.function(self.lower_limit)
        fb = self.function(self.upper_limit)
        xk = (self.lower_limit + k * h for k in xrange(1, n))
        return h * ((fa + fb) / 2 + sum(map(self.function, xk)))


class SimpsonMethod(NumericalIntegrationMethod):

    name = _("Simpson's rule")

    desc = _('''Approximate function f on subinterval [a, b] with a polynomial
of degree 2 which  passes through the points (a, f(a)),
((a+b) /2, f((a+b) / 2)) and (b, f(b)).''')

    def _calculate(self, n, h):
        fa = self.function(self.lower_limit)
        fb = self.function(self.upper_limit)
        xk = [self.lower_limit + k * h / 2 for k in xrange(1, 2 * n)]
        return h / 6 * (fa + 4 * sum(map(self.function, xk[::2])) +
                         2 * sum(map(self.function, xk[1::2])) + fb)


METHODS = [
    LeftRectanglesMethod,
    InnerRectanglesMethod,
    RightRectanglesMethod,
    TrapezoidalMethod,
    SimpsonMethod
]



