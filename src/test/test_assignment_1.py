import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.main.assignment_1 import *


Approximate(1.5, .000001)
print("\n")

print(Bisect(1,100,5,.000001))
print("\n")








