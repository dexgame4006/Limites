import sympy as sp
from sympy import cos,sin, log, oo
import math

x= sp.Symbol("x")
z=input("Equação que se pretende calcular o limite:")
v=input("Para que valor de x pretende que tende a equação:")
limite = sp.limit(z,x,v)
print("A equação tende para",limite)
