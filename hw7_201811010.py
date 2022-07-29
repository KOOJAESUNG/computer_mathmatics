import sympy as sp

x = sp.Symbol('x')
fx = 1/(x*(x+1))
print("F(x)=",sp.simplify(sp.integrate(fx,x)))


gx = (2*x-3)/(x**2-3*x+2)
print("G(x)=",sp.simplify(sp.integrate(gx,x)))

