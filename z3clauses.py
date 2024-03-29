import sys
import time
sys.path.append("/home/sukanta/App/z3-master/build")
from z3 import *

s = Optimize()
R_1_1_1, R_1_1_2, R_1_1_3, R_1_1_4, R_1_1_5  = Ints('R_1_1_1 R_1_1_2 R_1_1_3 R_1_1_4 R_1_1_5')
r_1_1_1, r_1_1_2, r_1_1_3, r_1_1_4, r_1_1_5, s_1_1  = Ints('r_1_1_1 r_1_1_2 r_1_1_3 r_1_1_4 r_1_1_5 s_1_1')# Added reagent variables
R_2_1_1, R_2_1_2, R_2_1_3, R_2_1_4, R_2_1_5  = Ints('R_2_1_1 R_2_1_2 R_2_1_3 R_2_1_4 R_2_1_5')
r_2_1_1, r_2_1_2, r_2_1_3, r_2_1_4, r_2_1_5, s_2_1  = Ints('r_2_1_1 r_2_1_2 r_2_1_3 r_2_1_4 r_2_1_5 s_2_1')# Added reagent variables
R_2_2_1, R_2_2_2, R_2_2_3, R_2_2_4, R_2_2_5  = Ints('R_2_2_1 R_2_2_2 R_2_2_3 R_2_2_4 R_2_2_5')
r_2_2_1, r_2_2_2, r_2_2_3, r_2_2_4, r_2_2_5, s_2_2  = Ints('r_2_2_1 r_2_2_2 r_2_2_3 r_2_2_4 r_2_2_5 s_2_2')# Added reagent variables
R_3_1_1, R_3_1_2, R_3_1_3, R_3_1_4, R_3_1_5  = Ints('R_3_1_1 R_3_1_2 R_3_1_3 R_3_1_4 R_3_1_5')
r_3_1_1, r_3_1_2, r_3_1_3, r_3_1_4, r_3_1_5, s_3_1  = Ints('r_3_1_1 r_3_1_2 r_3_1_3 r_3_1_4 r_3_1_5 s_3_1')# Added reagent variables
R_3_2_1, R_3_2_2, R_3_2_3, R_3_2_4, R_3_2_5  = Ints('R_3_2_1 R_3_2_2 R_3_2_3 R_3_2_4 R_3_2_5')
r_3_2_1, r_3_2_2, r_3_2_3, r_3_2_4, r_3_2_5, s_3_2  = Ints('r_3_2_1 r_3_2_2 r_3_2_3 r_3_2_4 r_3_2_5 s_3_2')# Added reagent variables
R_4_1_1, R_4_1_2, R_4_1_3, R_4_1_4, R_4_1_5  = Ints('R_4_1_1 R_4_1_2 R_4_1_3 R_4_1_4 R_4_1_5')
r_4_1_1, r_4_1_2, r_4_1_3, r_4_1_4, r_4_1_5, s_4_1  = Ints('r_4_1_1 r_4_1_2 r_4_1_3 r_4_1_4 r_4_1_5 s_4_1')# Added reagent variables
R_4_2_1, R_4_2_2, R_4_2_3, R_4_2_4, R_4_2_5  = Ints('R_4_2_1 R_4_2_2 R_4_2_3 R_4_2_4 R_4_2_5')
r_4_2_1, r_4_2_2, r_4_2_3, r_4_2_4, r_4_2_5, s_4_2  = Ints('r_4_2_1 r_4_2_2 r_4_2_3 r_4_2_4 r_4_2_5 s_4_2')# Added reagent variables
w_2_1_1_1, w_2_2_1_1, w_3_1_2_1, w_3_2_2_2, w_4_1_3_1, w_4_2_3_2  = Ints('w_2_1_1_1 w_2_2_1_1 w_3_1_2_1 w_3_2_2_2 w_4_1_3_1 w_4_2_3_2')# Added edgeVariables

t776 = Int('t776')
t777 = Int('t777')
t778 = Int('t778')
t779 = Int('t779')
t780 = Int('t780')
t781 = Int('t781')
t782 = Int('t782')
t783 = Int('t783')
t784 = Int('t784')
t785 = Int('t785')
s.add(64*r_1_1_1 + 1*t776 + 1*t777  == R_1_1_1)
s.add(64*r_1_1_2 + 1*t778 + 1*t779  == R_1_1_2)
s.add(64*r_1_1_3 + 1*t780 + 1*t781  == R_1_1_3)
s.add(64*r_1_1_4 + 1*t782 + 1*t783  == R_1_1_4)
s.add(64*r_1_1_5 + 1*t784 + 1*t785  == R_1_1_5)

s.add(Implies((w_2_1_1_1 == 0), (t776 == 0)))
s.add(Implies((w_2_1_1_1 == 1), (t776 == 1*R_2_1_1)))
s.add(Implies((w_2_1_1_1 == 2), (t776 == 2*R_2_1_1)))
s.add(Implies((w_2_1_1_1 == 3), (t776 == 3*R_2_1_1)))

s.add(Implies((w_2_2_1_1 == 0), (t777 == 0)))
s.add(Implies((w_2_2_1_1 == 1), (t777 == 1*R_2_2_1)))
s.add(Implies((w_2_2_1_1 == 2), (t777 == 2*R_2_2_1)))
s.add(Implies((w_2_2_1_1 == 3), (t777 == 3*R_2_2_1)))

s.add(Implies((w_2_1_1_1 == 0), (t778 == 0)))
s.add(Implies((w_2_1_1_1 == 1), (t778 == 1*R_2_1_2)))
s.add(Implies((w_2_1_1_1 == 2), (t778 == 2*R_2_1_2)))
s.add(Implies((w_2_1_1_1 == 3), (t778 == 3*R_2_1_2)))

s.add(Implies((w_2_2_1_1 == 0), (t779 == 0)))
s.add(Implies((w_2_2_1_1 == 1), (t779 == 1*R_2_2_2)))
s.add(Implies((w_2_2_1_1 == 2), (t779 == 2*R_2_2_2)))
s.add(Implies((w_2_2_1_1 == 3), (t779 == 3*R_2_2_2)))

s.add(Implies((w_2_1_1_1 == 0), (t780 == 0)))
s.add(Implies((w_2_1_1_1 == 1), (t780 == 1*R_2_1_3)))
s.add(Implies((w_2_1_1_1 == 2), (t780 == 2*R_2_1_3)))
s.add(Implies((w_2_1_1_1 == 3), (t780 == 3*R_2_1_3)))

s.add(Implies((w_2_2_1_1 == 0), (t781 == 0)))
s.add(Implies((w_2_2_1_1 == 1), (t781 == 1*R_2_2_3)))
s.add(Implies((w_2_2_1_1 == 2), (t781 == 2*R_2_2_3)))
s.add(Implies((w_2_2_1_1 == 3), (t781 == 3*R_2_2_3)))

s.add(Implies((w_2_1_1_1 == 0), (t782 == 0)))
s.add(Implies((w_2_1_1_1 == 1), (t782 == 1*R_2_1_4)))
s.add(Implies((w_2_1_1_1 == 2), (t782 == 2*R_2_1_4)))
s.add(Implies((w_2_1_1_1 == 3), (t782 == 3*R_2_1_4)))

s.add(Implies((w_2_2_1_1 == 0), (t783 == 0)))
s.add(Implies((w_2_2_1_1 == 1), (t783 == 1*R_2_2_4)))
s.add(Implies((w_2_2_1_1 == 2), (t783 == 2*R_2_2_4)))
s.add(Implies((w_2_2_1_1 == 3), (t783 == 3*R_2_2_4)))

s.add(Implies((w_2_1_1_1 == 0), (t784 == 0)))
s.add(Implies((w_2_1_1_1 == 1), (t784 == 1*R_2_1_5)))
s.add(Implies((w_2_1_1_1 == 2), (t784 == 2*R_2_1_5)))
s.add(Implies((w_2_1_1_1 == 3), (t784 == 3*R_2_1_5)))

s.add(Implies((w_2_2_1_1 == 0), (t785 == 0)))
s.add(Implies((w_2_2_1_1 == 1), (t785 == 1*R_2_2_5)))
s.add(Implies((w_2_2_1_1 == 2), (t785 == 2*R_2_2_5)))
s.add(Implies((w_2_2_1_1 == 3), (t785 == 3*R_2_2_5)))

t786 = Int('t786')
t787 = Int('t787')
t788 = Int('t788')
t789 = Int('t789')
t790 = Int('t790')
s.add(16*r_2_1_1 + 1*t786  == R_2_1_1)
s.add(16*r_2_1_2 + 1*t787  == R_2_1_2)
s.add(16*r_2_1_3 + 1*t788  == R_2_1_3)
s.add(16*r_2_1_4 + 1*t789  == R_2_1_4)
s.add(16*r_2_1_5 + 1*t790  == R_2_1_5)

s.add(Implies((w_3_1_2_1 == 0), (t786 == 0)))
s.add(Implies((w_3_1_2_1 == 1), (t786 == 1*R_3_1_1)))
s.add(Implies((w_3_1_2_1 == 2), (t786 == 2*R_3_1_1)))
s.add(Implies((w_3_1_2_1 == 3), (t786 == 3*R_3_1_1)))

s.add(Implies((w_3_1_2_1 == 0), (t787 == 0)))
s.add(Implies((w_3_1_2_1 == 1), (t787 == 1*R_3_1_2)))
s.add(Implies((w_3_1_2_1 == 2), (t787 == 2*R_3_1_2)))
s.add(Implies((w_3_1_2_1 == 3), (t787 == 3*R_3_1_2)))

s.add(Implies((w_3_1_2_1 == 0), (t788 == 0)))
s.add(Implies((w_3_1_2_1 == 1), (t788 == 1*R_3_1_3)))
s.add(Implies((w_3_1_2_1 == 2), (t788 == 2*R_3_1_3)))
s.add(Implies((w_3_1_2_1 == 3), (t788 == 3*R_3_1_3)))

s.add(Implies((w_3_1_2_1 == 0), (t789 == 0)))
s.add(Implies((w_3_1_2_1 == 1), (t789 == 1*R_3_1_4)))
s.add(Implies((w_3_1_2_1 == 2), (t789 == 2*R_3_1_4)))
s.add(Implies((w_3_1_2_1 == 3), (t789 == 3*R_3_1_4)))

s.add(Implies((w_3_1_2_1 == 0), (t790 == 0)))
s.add(Implies((w_3_1_2_1 == 1), (t790 == 1*R_3_1_5)))
s.add(Implies((w_3_1_2_1 == 2), (t790 == 2*R_3_1_5)))
s.add(Implies((w_3_1_2_1 == 3), (t790 == 3*R_3_1_5)))

t791 = Int('t791')
t792 = Int('t792')
t793 = Int('t793')
t794 = Int('t794')
t795 = Int('t795')
s.add(16*r_2_2_1 + 1*t791  == R_2_2_1)
s.add(16*r_2_2_2 + 1*t792  == R_2_2_2)
s.add(16*r_2_2_3 + 1*t793  == R_2_2_3)
s.add(16*r_2_2_4 + 1*t794  == R_2_2_4)
s.add(16*r_2_2_5 + 1*t795  == R_2_2_5)

s.add(Implies((w_3_2_2_2 == 0), (t791 == 0)))
s.add(Implies((w_3_2_2_2 == 1), (t791 == 1*R_3_2_1)))
s.add(Implies((w_3_2_2_2 == 2), (t791 == 2*R_3_2_1)))
s.add(Implies((w_3_2_2_2 == 3), (t791 == 3*R_3_2_1)))

s.add(Implies((w_3_2_2_2 == 0), (t792 == 0)))
s.add(Implies((w_3_2_2_2 == 1), (t792 == 1*R_3_2_2)))
s.add(Implies((w_3_2_2_2 == 2), (t792 == 2*R_3_2_2)))
s.add(Implies((w_3_2_2_2 == 3), (t792 == 3*R_3_2_2)))

s.add(Implies((w_3_2_2_2 == 0), (t793 == 0)))
s.add(Implies((w_3_2_2_2 == 1), (t793 == 1*R_3_2_3)))
s.add(Implies((w_3_2_2_2 == 2), (t793 == 2*R_3_2_3)))
s.add(Implies((w_3_2_2_2 == 3), (t793 == 3*R_3_2_3)))

s.add(Implies((w_3_2_2_2 == 0), (t794 == 0)))
s.add(Implies((w_3_2_2_2 == 1), (t794 == 1*R_3_2_4)))
s.add(Implies((w_3_2_2_2 == 2), (t794 == 2*R_3_2_4)))
s.add(Implies((w_3_2_2_2 == 3), (t794 == 3*R_3_2_4)))

s.add(Implies((w_3_2_2_2 == 0), (t795 == 0)))
s.add(Implies((w_3_2_2_2 == 1), (t795 == 1*R_3_2_5)))
s.add(Implies((w_3_2_2_2 == 2), (t795 == 2*R_3_2_5)))
s.add(Implies((w_3_2_2_2 == 3), (t795 == 3*R_3_2_5)))

t796 = Int('t796')
t797 = Int('t797')
t798 = Int('t798')
t799 = Int('t799')
t800 = Int('t800')
s.add(4*r_3_1_1 + 1*t796  == R_3_1_1)
s.add(4*r_3_1_2 + 1*t797  == R_3_1_2)
s.add(4*r_3_1_3 + 1*t798  == R_3_1_3)
s.add(4*r_3_1_4 + 1*t799  == R_3_1_4)
s.add(4*r_3_1_5 + 1*t800  == R_3_1_5)

s.add(Implies((w_4_1_3_1 == 0), (t796 == 0)))
s.add(Implies((w_4_1_3_1 == 1), (t796 == 1*R_4_1_1)))
s.add(Implies((w_4_1_3_1 == 2), (t796 == 2*R_4_1_1)))
s.add(Implies((w_4_1_3_1 == 3), (t796 == 3*R_4_1_1)))

s.add(Implies((w_4_1_3_1 == 0), (t797 == 0)))
s.add(Implies((w_4_1_3_1 == 1), (t797 == 1*R_4_1_2)))
s.add(Implies((w_4_1_3_1 == 2), (t797 == 2*R_4_1_2)))
s.add(Implies((w_4_1_3_1 == 3), (t797 == 3*R_4_1_2)))

s.add(Implies((w_4_1_3_1 == 0), (t798 == 0)))
s.add(Implies((w_4_1_3_1 == 1), (t798 == 1*R_4_1_3)))
s.add(Implies((w_4_1_3_1 == 2), (t798 == 2*R_4_1_3)))
s.add(Implies((w_4_1_3_1 == 3), (t798 == 3*R_4_1_3)))

s.add(Implies((w_4_1_3_1 == 0), (t799 == 0)))
s.add(Implies((w_4_1_3_1 == 1), (t799 == 1*R_4_1_4)))
s.add(Implies((w_4_1_3_1 == 2), (t799 == 2*R_4_1_4)))
s.add(Implies((w_4_1_3_1 == 3), (t799 == 3*R_4_1_4)))

s.add(Implies((w_4_1_3_1 == 0), (t800 == 0)))
s.add(Implies((w_4_1_3_1 == 1), (t800 == 1*R_4_1_5)))
s.add(Implies((w_4_1_3_1 == 2), (t800 == 2*R_4_1_5)))
s.add(Implies((w_4_1_3_1 == 3), (t800 == 3*R_4_1_5)))

t801 = Int('t801')
t802 = Int('t802')
t803 = Int('t803')
t804 = Int('t804')
t805 = Int('t805')
s.add(4*r_3_2_1 + 1*t801  == R_3_2_1)
s.add(4*r_3_2_2 + 1*t802  == R_3_2_2)
s.add(4*r_3_2_3 + 1*t803  == R_3_2_3)
s.add(4*r_3_2_4 + 1*t804  == R_3_2_4)
s.add(4*r_3_2_5 + 1*t805  == R_3_2_5)

s.add(Implies((w_4_2_3_2 == 0), (t801 == 0)))
s.add(Implies((w_4_2_3_2 == 1), (t801 == 1*R_4_2_1)))
s.add(Implies((w_4_2_3_2 == 2), (t801 == 2*R_4_2_1)))
s.add(Implies((w_4_2_3_2 == 3), (t801 == 3*R_4_2_1)))

s.add(Implies((w_4_2_3_2 == 0), (t802 == 0)))
s.add(Implies((w_4_2_3_2 == 1), (t802 == 1*R_4_2_2)))
s.add(Implies((w_4_2_3_2 == 2), (t802 == 2*R_4_2_2)))
s.add(Implies((w_4_2_3_2 == 3), (t802 == 3*R_4_2_2)))

s.add(Implies((w_4_2_3_2 == 0), (t803 == 0)))
s.add(Implies((w_4_2_3_2 == 1), (t803 == 1*R_4_2_3)))
s.add(Implies((w_4_2_3_2 == 2), (t803 == 2*R_4_2_3)))
s.add(Implies((w_4_2_3_2 == 3), (t803 == 3*R_4_2_3)))

s.add(Implies((w_4_2_3_2 == 0), (t804 == 0)))
s.add(Implies((w_4_2_3_2 == 1), (t804 == 1*R_4_2_4)))
s.add(Implies((w_4_2_3_2 == 2), (t804 == 2*R_4_2_4)))
s.add(Implies((w_4_2_3_2 == 3), (t804 == 3*R_4_2_4)))

s.add(Implies((w_4_2_3_2 == 0), (t805 == 0)))
s.add(Implies((w_4_2_3_2 == 1), (t805 == 1*R_4_2_5)))
s.add(Implies((w_4_2_3_2 == 2), (t805 == 2*R_4_2_5)))
s.add(Implies((w_4_2_3_2 == 3), (t805 == 3*R_4_2_5)))

s.add(1*r_4_1_1  == R_4_1_1)
s.add(1*r_4_1_2  == R_4_1_2)
s.add(1*r_4_1_3  == R_4_1_3)
s.add(1*r_4_1_4  == R_4_1_4)
s.add(1*r_4_1_5  == R_4_1_5)

s.add(1*r_4_2_1  == R_4_2_1)
s.add(1*r_4_2_2  == R_4_2_2)
s.add(1*r_4_2_3  == R_4_2_3)
s.add(1*r_4_2_4  == R_4_2_4)
s.add(1*r_4_2_5  == R_4_2_5)

s.add(Or(r_1_1_1 + r_1_1_2 + r_1_1_3 + r_1_1_4 + r_1_1_5 + w_2_1_1_1 + w_2_2_1_1  == 4, r_1_1_1 + r_1_1_2 + r_1_1_3 + r_1_1_4 + r_1_1_5 + w_2_1_1_1 + w_2_2_1_1  == 0))
s.add(Or(r_2_1_1 + r_2_1_2 + r_2_1_3 + r_2_1_4 + r_2_1_5 + w_3_1_2_1  == 4, r_2_1_1 + r_2_1_2 + r_2_1_3 + r_2_1_4 + r_2_1_5 + w_3_1_2_1  == 0))
s.add(w_2_1_1_1  <= 4)
s.add(Or(r_2_2_1 + r_2_2_2 + r_2_2_3 + r_2_2_4 + r_2_2_5 + w_3_2_2_2  == 4, r_2_2_1 + r_2_2_2 + r_2_2_3 + r_2_2_4 + r_2_2_5 + w_3_2_2_2  == 0))
s.add(w_2_2_1_1  <= 4)
s.add(Or(r_3_1_1 + r_3_1_2 + r_3_1_3 + r_3_1_4 + r_3_1_5 + w_4_1_3_1  == 4, r_3_1_1 + r_3_1_2 + r_3_1_3 + r_3_1_4 + r_3_1_5 + w_4_1_3_1  == 0))
s.add(w_3_1_2_1  <= 4)
s.add(Or(r_3_2_1 + r_3_2_2 + r_3_2_3 + r_3_2_4 + r_3_2_5 + w_4_2_3_2  == 4, r_3_2_1 + r_3_2_2 + r_3_2_3 + r_3_2_4 + r_3_2_5 + w_4_2_3_2  == 0))
s.add(w_3_2_2_2  <= 4)
s.add(Or(r_4_1_1 + r_4_1_2 + r_4_1_3 + r_4_1_4 + r_4_1_5  == 4, r_4_1_1 + r_4_1_2 + r_4_1_3 + r_4_1_4 + r_4_1_5  == 0))
s.add(w_4_1_3_1  <= 4)
s.add(Or(r_4_2_1 + r_4_2_2 + r_4_2_3 + r_4_2_4 + r_4_2_5  == 4, r_4_2_1 + r_4_2_2 + r_4_2_3 + r_4_2_4 + r_4_2_5  == 0))
s.add(w_4_2_3_2  <= 4)
s.add(And(r_1_1_1 >= 0, r_1_1_1 <= 3, r_1_1_2 >= 0, r_1_1_2 <= 3, r_1_1_3 >= 0, r_1_1_3 <= 3, r_1_1_4 >= 0, r_1_1_4 <= 3, r_1_1_5 >= 0, r_1_1_5 <= 3))
s.add(And(r_2_1_1 >= 0, r_2_1_1 <= 3, r_2_1_2 >= 0, r_2_1_2 <= 3, r_2_1_3 >= 0, r_2_1_3 <= 3, r_2_1_4 >= 0, r_2_1_4 <= 3, r_2_1_5 >= 0, r_2_1_5 <= 3))
s.add(And(r_2_2_1 >= 0, r_2_2_1 <= 3, r_2_2_2 >= 0, r_2_2_2 <= 3, r_2_2_3 >= 0, r_2_2_3 <= 3, r_2_2_4 >= 0, r_2_2_4 <= 3, r_2_2_5 >= 0, r_2_2_5 <= 3))
s.add(And(r_3_1_1 >= 0, r_3_1_1 <= 3, r_3_1_2 >= 0, r_3_1_2 <= 3, r_3_1_3 >= 0, r_3_1_3 <= 3, r_3_1_4 >= 0, r_3_1_4 <= 3, r_3_1_5 >= 0, r_3_1_5 <= 3))
s.add(And(r_3_2_1 >= 0, r_3_2_1 <= 3, r_3_2_2 >= 0, r_3_2_2 <= 3, r_3_2_3 >= 0, r_3_2_3 <= 3, r_3_2_4 >= 0, r_3_2_4 <= 3, r_3_2_5 >= 0, r_3_2_5 <= 3))
s.add(And(r_4_1_1 >= 0, r_4_1_1 <= 3, r_4_1_2 >= 0, r_4_1_2 <= 3, r_4_1_3 >= 0, r_4_1_3 <= 3, r_4_1_4 >= 0, r_4_1_4 <= 3, r_4_1_5 >= 0, r_4_1_5 <= 3))
s.add(And(r_4_2_1 >= 0, r_4_2_1 <= 3, r_4_2_2 >= 0, r_4_2_2 <= 3, r_4_2_3 >= 0, r_4_2_3 <= 3, r_4_2_4 >= 0, r_4_2_4 <= 3, r_4_2_5 >= 0, r_4_2_5 <= 3))
s.add(And(w_2_1_1_1 >= 0, w_2_1_1_1 <= 3, w_2_2_1_1 >= 0, w_2_2_1_1 <= 3, w_3_1_2_1 >= 0, w_3_1_2_1 <= 3, w_3_2_2_2 >= 0, w_3_2_2_2 <= 3, w_4_1_3_1 >= 0, w_4_1_3_1 <= 3, w_4_2_3_2 >= 0, w_4_2_3_2 <= 3))
s.add(And(w_2_1_1_1< 3, w_2_2_1_1< 3)) # Added constraint to limit the edge weight weight

s.add(And(R_1_1_1 == 5, R_1_1_2 == 2, R_1_1_3 == 168, R_1_1_4 == 52, R_1_1_5 == 29))


totalReagents = s.minimize(r_1_1_1 + r_1_1_2 + r_1_1_3 + r_1_1_4 + r_1_1_5 + r_2_1_1 + r_2_1_2 + r_2_1_3 + r_2_1_4 + r_2_1_5 + r_2_2_1 + r_2_2_2 + r_2_2_3 + r_2_2_4 + r_2_2_5 + r_3_1_1 + r_3_1_2 + r_3_1_3 + r_3_1_4 + r_3_1_5 + r_3_2_1 + r_3_2_2 + r_3_2_3 + r_3_2_4 + r_3_2_5 + r_4_1_1 + r_4_1_2 + r_4_1_3 + r_4_1_4 + r_4_1_5 + r_4_2_1 + r_4_2_2 + r_4_2_3 + r_4_2_4 + r_4_2_5 )
startTime = time.time()
if s.check() == sat:
	print("Total reagents = ", totalReagents.value())
	fp = open('z3opFile','w')
	lst = s.model()
	for i in lst:
	    fp.write(str(i) + " = " + str(s.model()[i]) + '\n')
else:
	print('unsat')
endTime = time.time()
executionTime = endTime - startTime
print("Execution Time = ",executionTime)
