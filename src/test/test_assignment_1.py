import sys
import os
# Use below for trig functions
import math

# For using functions from assignment_1 to test in test_assignment_1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.main.assignment_1 import *


Approximate(1.5, .000001)
print("\n")

def f(x):
    return (x*x*x + 4*x*x - 10)

Bisect(f,1,2,100,.001)

print("\n")

def g(x):
    return (x - x*x*x - 4*x*x + 10)

FixedPoint(g,1.5,.000001,50)

print("\n")


def h(x):
    return math.cos(x) - x
def h_p(x):
    return -1 * math.sin(x) - 1

Newton(h,h_p,1,.000001,100)










