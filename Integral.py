def one_function(x):
   return x**2 + 2*x

def another_function(x):
    return x + 5


def integral(func, x0, x1, points):
    '''
    Approximate the integral for a function, using a selected number of points
    :param func:  any function that takes an numeric parameters
    :param x0:    lower limit of the interval
    :param x1:    upper limit
    :param points:  number of points
    :return:        approximation of the integral
    '''
    if x0 > x1:
        print "Wrong choice for the integral's interval:", x0, x1
        return None

    delta=float(x1-x0)/points
    x = x0
    result = 0.0
    while x<x1:
        result = result + delta * func(x)
        x = x + delta
    return result




print "First integral: ", integral(one_function, 0, 10, 50)

print "Second integral: ", integral(another_function, 0, 10, 50)

