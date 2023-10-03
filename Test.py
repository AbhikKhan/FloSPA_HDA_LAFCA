'''
Created on 26-Jul-2017
@author: sukanta
'''

import sys
import time
sys.path.append("/home/sukanta/App/z3/bin")
from z3 import *

S=Solver()

w, s, t  = Ints('w s t')

S.add(w == 2, s == 1, t == If(w > 0, If(w > s, w, s),0))

print S.check()
lst = S.model()
for i in lst:
    print str(i) + " = " + str(S.model()[i]) + '\n'