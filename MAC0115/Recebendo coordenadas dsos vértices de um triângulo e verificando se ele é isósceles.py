x1 = float(input("x1:")) 
y1 = float(input("y1:")) 
x2 = float(input("x2:"))
y2 = float(input("y2:"))
x3 = float(input("x3:"))
y3 = float(input("y3:"))

A = (x1 - x2)**2 + (y1 - y2)**2
B = (x2 - x3)**2 + (y2 - y3)**2
C = (x1 - x3)**2 + (y1 - y3)**2

dAB = A - B
if dAB < 0 :
    dAB = -dAB
dBC = B - C
if dBC < 0 :
    dBC = -dBC
dAC = A - C
if dAC < 0:
    dAC = -dAC
if dAB < 1e-8 or dAC < 1e-8 or dBC <1e-8 :
    print("É isósceles!")
else:
    print("Não é isósceles!")
