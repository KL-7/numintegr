from __future__ import division


class NumericalIntegrationMethod(object):

    name = ''

    desc = ''

    def __init__(self, function, lower_limit, upper_limit):
        self.function = function
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def subinterval_size(self, subinterval_number):
        return (self.upper_limit - self.lower_limit) / subinterval_number

    def calculate(self, subinervals_number, subinterval_size):
        raise NotImplementedError("Calculate method should be implemented.")

    def integrate(self, subintervals_number):
        return self.calculate(subintervals_number,
                              self.subinterval_size(subintervals_number))


class RectanglesMethod(NumericalIntegrationMethod):

    name = 'Rectangles'

    desc = '''Computes an approximation to a definite integral, made
by finding the area of a collection of rectangles whose heights are determined
by the values of the function.'''

    ALPHA = 0

    def calculate(self, n, h):
        xk = [self.lower_limit + h * (i + self.ALPHA) for i in xrange(0, n)]
#        import logging
#        logging.info('%s: %s, %s' % (self.name, ['%2.2f' % x for x in xk],
#                                     ['%2.2f' % self.function(x) for x in xk]))
        return h * sum((self.function(x) for x in xk))


class LeftRectanglesMethod(RectanglesMethod):

    name = 'Left Rectangles'

    desc = '''Approximate function f on subinterval [a, b] with constant
function equal to f(a) on [a, b].'''


class RightRectanglesMethod(RectanglesMethod):

    name = 'Right Rectangles'

    desc = '''Approximate function f on subinterval [a, b] with constant
function equal to f(b) on [a, b].'''

    ALPHA = 1


class InnerRectanglesMethod(RectanglesMethod):

    name = 'Inner Rectangles'

    desc = '''Approximate function f on subinterval [a, b] with constant
function equal to f((a + b) / 2) on [a, b].'''

    ALPHA = 0.5


METHODS = [LeftRectanglesMethod, InnerRectanglesMethod, RightRectanglesMethod]



