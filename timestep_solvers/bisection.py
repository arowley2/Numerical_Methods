from math import *
import matplotlib.pyplot as plt
import math

from helper_functions import *

def bisection(f, a, b, zero_tol=1e-8, max_iters=100):
    """
    Find a root of f(x) in the interval [a,b] using Newton's method.
    Requires [a,b] contains exactly one root that passes through the x-intersection
    """

    fa = f(a)
    fb = f(b)

    x_list = []

    # solve for the root
    for n in range(0, max_iters):
        mid = (a+b)/2
        fmid = f(mid)
        
        x_list.append(mid)

        if abs(fmid) < zero_tol:
            return mid, x_list

        if fmid*fa < 0:
            b = mid
            fb = f(b)
        elif fmid*fb < 0:
            a = mid
            fa = f(a)
    
    print(mid)
    print(x_list)
    return mid, x_list


def truncated_bisection(f, a, b, dps=4, zero_tol=1e-8, max_iters=100):
    """
    Find a root of f(x) in the interval [a,b] using Newton's method.
    Requires [a,b] contains exactly one root that passes through the x-intersection
    """

    fa = truncate(f(a), dps) 
    fb = truncate(f(b), dps)

    x_list = []

    # solve for the root
    for n in range(0, max_iters):
        mid = truncate((a+b)/2, dps)
        fmid = truncate(f(mid), dps)
        
        x_list.append(mid)

        if abs(fmid) < zero_tol:
            print(n)
            return mid, x_list

        if fmid*fa < 0:
            b = mid
            fb = truncate(f(b), dps)
        elif fmid*fb < 0:
            a = mid
            fa = truncate(f(a), dps)
    
    print(mid)
    print(x_list)
    return mid, x_list


# --------------------------
# Test to find Dottie number
# --------------------------

f = lambda x: (cos(x) - x)

# guess interval that the root lies in
a = 0.2
b = 1

# list to check tolerance
tol_list = []
err_list = []
for i in range(3,18):
    tol = 10**(-i)
    zero, _ = bisection(f, a, b, tol)
    error = abs(f(zero))

    tol_list.append(tol)
    err_list.append(error)

plt.figure()
plt.loglog(tol_list, err_list, "-o")
plt.gca().invert_xaxis()

plt.xlabel("tolerance")
plt.ylabel("error")
plt.tight_layout()
plt.show()


# --------------------------
# Test Error Plotting (with Quadratic Root)
# --------------------------

f = lambda x: x**2 - 2

# guess interval that the root lies in
a = 0
b = 6

zero, x_list = bisection(f, a, b)
print(zero)
error_plots(f, zero, x_list, math.sqrt(2))

zero, x_list = truncated_bisection(f, a, b, 4)
print(zero)
error_plots(f, zero, x_list, math.sqrt(2))