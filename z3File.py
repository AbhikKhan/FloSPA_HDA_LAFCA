from z3 import *

s = Optimize()

# Variable declaration
A_4_4_R2 = Int("A_4_4_R2")
A_4_4_R3 = Int("A_4_4_R3")
A_5_4_R2 = Int("A_5_4_R2")
A_5_4_R3 = Int("A_5_4_R3")
A_5_3_R2 = Int("A_5_3_R2")
A_5_3_R3 = Int("A_5_3_R3")
A_4_3_R2 = Int("A_4_3_R2")
A_4_3_R3 = Int("A_4_3_R3")

V_R2 = Int("V_R2")
V_R3 = Int("V_R3")

d_0_R2  = Int("d_0_R2")
d_0_R3  = Int("d_0_R3")
d_1_R2  = Int("d_1_R2")
d_1_R3  = Int("d_1_R3")
d_2_R2  = Int("d_2_R2")
d_2_R3  = Int("d_2_R3")

d_4_4_0_R2 = Int("d_4_4_0_R2")
d_4_4_1_R2 = Int("d_4_4_1_R2")
d_4_4_2_R2 = Int("d_4_4_2_R2")
d_4_4_0_R3 = Int("d_4_4_0_R3")
d_4_4_1_R3 = Int("d_4_4_1_R3")
d_4_4_2_R3 = Int("d_4_4_2_R3")
d_5_4_0_R2 = Int("d_5_4_0_R2")
d_5_4_1_R2 = Int("d_5_4_1_R2")
d_5_4_2_R2 = Int("d_5_4_2_R2")
d_5_4_0_R3 = Int("d_5_4_0_R3")
d_5_4_1_R3 = Int("d_5_4_1_R3")
d_5_4_2_R3 = Int("d_5_4_2_R3")
d_5_3_0_R2 = Int("d_5_3_0_R2")
d_5_3_1_R2 = Int("d_5_3_1_R2")
d_5_3_2_R2 = Int("d_5_3_2_R2")
d_5_3_0_R3 = Int("d_5_3_0_R3")
d_5_3_1_R3 = Int("d_5_3_1_R3")
d_5_3_2_R3 = Int("d_5_3_2_R3")
d_4_3_0_R2 = Int("d_4_3_0_R2")
d_4_3_1_R2 = Int("d_4_3_1_R2")
d_4_3_2_R2 = Int("d_4_3_2_R2")
d_4_3_0_R3 = Int("d_4_3_0_R3")
d_4_3_1_R3 = Int("d_4_3_1_R3")
d_4_3_2_R3 = Int("d_4_3_2_R3")

# Number of cells in the mixture filled with Rt reagent
s.add(And(A_4_4_R2>=0, A_4_4_R2<=1, A_4_4_R3>=0, A_4_4_R3<=1))
s.add(And(A_5_4_R2>=0, A_5_4_R2<=1, A_5_4_R3>=0, A_5_4_R3<=1))
s.add(And(A_5_3_R2>=0, A_5_3_R2<=1, A_5_3_R3>=0, A_5_3_R3<=1))
s.add(And(A_4_3_R2>=0, A_4_3_R2<=1, A_4_3_R3>=0, A_4_3_R3<=1))

s.add(A_4_4_R2 + A_5_4_R2 + A_5_3_R2 + A_4_3_R2 == V_R2)
s.add(A_4_4_R3 + A_5_4_R3 + A_5_3_R3 + A_4_3_R3 == V_R3)

# If a cell is filled with reagent Rt then no reagent Rk where k != t can be filled in that cell.
s.add(A_4_4_R2 + A_4_4_R3 == 1)
s.add(A_5_4_R2 + A_5_4_R3 == 1)
s.add(A_5_3_R2 + A_5_3_R3 == 1)
s.add(A_4_3_R2 + A_4_3_R3 == 1)

# To get traceability and connectivity.
s.add(If(And(A_4_4_R2 == 1, A_5_4_R2 + A_4_3_R2 == 0), (d_4_4_0_R2 == 1), (d_4_4_0_R2 == 0)))
s.add(If(And(A_5_4_R2 == 1, A_4_4_R2 + A_5_3_R2 == 0), (d_5_4_0_R2 == 1), (d_5_4_0_R2 == 0)))
s.add(If(And(A_5_3_R2 == 1, A_4_3_R2 + A_5_4_R2 == 0), (d_5_3_0_R2 == 1), (d_5_3_0_R2 == 0)))
s.add(If(And(A_4_3_R2 == 1, A_4_4_R2 + A_5_3_R2 == 0), (d_4_3_0_R2 == 1), (d_4_3_0_R2 == 0)))
s.add(If(And(A_4_4_R3 == 1, A_5_4_R3 + A_4_3_R3 == 0), (d_4_4_0_R3 == 1), (d_4_4_0_R3 == 0)))
s.add(If(And(A_5_4_R3 == 1, A_4_4_R3 + A_5_3_R3 == 0), (d_5_4_0_R3 == 1), (d_5_4_0_R3 == 0)))
s.add(If(And(A_5_3_R3 == 1, A_4_3_R3 + A_5_4_R3 == 0), (d_5_3_0_R3 == 1), (d_5_3_0_R3 == 0)))
s.add(If(And(A_4_3_R3 == 1, A_4_4_R3 + A_5_3_R3 == 0), (d_4_3_0_R3 == 1), (d_4_3_0_R3 == 0)))
s.add(If(And(A_4_4_R2 == 1, A_5_4_R2 + A_4_3_R2 == 1), (d_4_4_1_R2 == 1), (d_4_4_1_R2 == 0)))
s.add(If(And(A_5_4_R2 == 1, A_4_4_R2 + A_5_3_R2 == 1), (d_5_4_1_R2 == 1), (d_5_4_1_R2 == 0)))
s.add(If(And(A_5_3_R2 == 1, A_4_3_R2 + A_5_4_R2 == 1), (d_5_3_1_R2 == 1), (d_5_3_1_R2 == 0)))
s.add(If(And(A_4_3_R2 == 1, A_4_4_R2 + A_5_3_R2 == 1), (d_4_3_1_R2 == 1), (d_4_3_1_R2 == 0)))
s.add(If(And(A_4_4_R3 == 1, A_5_4_R3 + A_4_3_R3 == 1), (d_4_4_1_R3 == 1), (d_4_4_1_R3 == 0)))
s.add(If(And(A_5_4_R3 == 1, A_4_4_R3 + A_5_3_R3 == 1), (d_5_4_1_R3 == 1), (d_5_4_1_R3 == 0)))
s.add(If(And(A_5_3_R3 == 1, A_4_3_R3 + A_5_4_R3 == 1), (d_5_3_1_R3 == 1), (d_5_3_1_R3 == 0)))
s.add(If(And(A_4_3_R3 == 1, A_4_4_R3 + A_5_3_R3 == 1), (d_4_3_1_R3 == 1), (d_4_3_1_R3 == 0)))
s.add(If(And(A_4_4_R2 == 1, A_5_4_R2 + A_4_3_R2 == 2), (d_4_4_2_R2 == 1), (d_4_4_2_R2 == 0)))
s.add(If(And(A_5_4_R2 == 1, A_4_4_R2 + A_5_3_R2 == 2), (d_5_4_2_R2 == 1), (d_5_4_2_R2 == 0)))
s.add(If(And(A_5_3_R2 == 1, A_4_3_R2 + A_5_4_R2 == 2), (d_5_3_2_R2 == 1), (d_5_3_2_R2 == 0)))
s.add(If(And(A_4_3_R2 == 1, A_4_4_R2 + A_5_3_R2 == 2), (d_4_3_2_R2 == 1), (d_4_3_2_R2 == 0)))
s.add(If(And(A_4_4_R3 == 1, A_5_4_R3 + A_4_3_R3 == 2), (d_4_4_2_R3 == 1), (d_4_4_2_R3 == 0)))
s.add(If(And(A_5_4_R3 == 1, A_4_4_R3 + A_5_3_R3 == 2), (d_5_4_2_R3 == 1), (d_5_4_2_R3 == 0)))
s.add(If(And(A_5_3_R3 == 1, A_4_3_R3 + A_5_4_R3 == 2), (d_5_3_2_R3 == 1), (d_5_3_2_R3 == 0)))
s.add(If(And(A_4_3_R3 == 1, A_4_4_R3 + A_5_3_R3 == 2), (d_4_3_2_R3 == 1), (d_4_3_2_R3 == 0)))

s.add(d_4_4_0_R2 + d_5_4_0_R2 + d_5_3_0_R2 + d_4_3_0_R2 == d_0_R2)
s.add(d_4_4_1_R2 + d_5_4_1_R2 + d_5_3_1_R2 + d_4_3_1_R2 == d_1_R2)
s.add(d_4_4_2_R2 + d_5_4_2_R2 + d_5_3_2_R2 + d_4_3_2_R2 == d_2_R2)
s.add(d_4_4_0_R3 + d_5_4_0_R3 + d_5_3_0_R3 + d_4_3_0_R3 == d_0_R3)
s.add(d_4_4_1_R3 + d_5_4_1_R3 + d_5_3_1_R3 + d_4_3_1_R3 == d_1_R3)
s.add(d_4_4_2_R3 + d_5_4_2_R3 + d_5_3_2_R3 + d_4_3_2_R3 == d_2_R3)

s.add(Implies(V_R2 == 1, And(d_0_R2 == 1, d_1_R2 == 0, d_2_R2 == 0)))
s.add(Implies(V_R2 == 2, And(d_0_R2 == 0, d_1_R2 == 2, d_2_R2 == 0)))
s.add(Implies(V_R2 == 3, And(d_0_R2 == 0, d_1_R2 == 2, d_2_R2 == 1)))
s.add(Implies(V_R2 == 4, And(d_0_R2 == 0, d_1_R2 == 0, d_2_R2 == 4)))
s.add(Implies(V_R3 == 1, And(d_0_R3 == 1, d_1_R3 == 0, d_2_R3 == 0)))
s.add(Implies(V_R3 == 2, And(d_0_R3 == 0, d_1_R3 == 2, d_2_R3 == 0)))
s.add(Implies(V_R3 == 3, And(d_0_R3 == 0, d_1_R3 == 2, d_2_R3 == 1)))
s.add(Implies(V_R3 == 4, And(d_0_R3 == 0, d_1_R3 == 0, d_2_R3 == 4)))

s.add(And(V_R2 == 1, V_R3 == 3))

if s.check() == unsat:
	print("Not possible to create traceable graph for all reagents")
else:
	fp = open('output1.txt','w')
	values = s.model()
	if values[A_4_4_R2] == 1:
		fp.write("4,4,R2\n")
	if values[A_4_4_R3] == 1:
		fp.write("4,4,R3\n")
	if values[A_5_4_R2] == 1:
		fp.write("5,4,R2\n")
	if values[A_5_4_R3] == 1:
		fp.write("5,4,R3\n")
	if values[A_5_3_R2] == 1:
		fp.write("5,3,R2\n")
	if values[A_5_3_R3] == 1:
		fp.write("5,3,R3\n")
	if values[A_4_3_R2] == 1:
		fp.write("4,3,R2\n")
	if values[A_4_3_R3] == 1:
		fp.write("4,3,R3\n")
