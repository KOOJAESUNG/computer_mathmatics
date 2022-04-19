import sympy as sp

def f(x): return sp.exp(2 * x) * sp.sin(3 * x)
def fd(x): return sp.diff(f(x),x)
def f2d(x): return sp.diff(f(x),x,2)

x, k = sp.symbols('x k')

gx = f2d(x)+k*fd(x)+13*f(x)
print(sp.solve(gx,k,dict=True))
