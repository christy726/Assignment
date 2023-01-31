import sympy as smp
from sympy import symbols 
x= smp.Symbol("x")
a= smp.Symbol("a")
f =(1/(smp.log(x)))
dfdx = smp.diff(f,x)
print ("Derivatives",dfdx)

