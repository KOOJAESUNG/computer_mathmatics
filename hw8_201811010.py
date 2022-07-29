import sympy as sp

# (a)
x = sp.Symbol('x')
f1x = sp.exp(2 * x) / (sp.exp(x) + 1)
f2x = 1 / (sp.exp(x) + 1)
print("The answer is ", sp.integrate(f1x, (x, 0, 2)) - sp.integrate(f2x, (x, 0, 2)))

# (b)
fx = sp.Abs(sp.sin(x))
print("The answer is ", sp.integrate(fx, (x, -sp.pi, sp.pi)))

# (c)
fx = x * sp.sqrt(x ** 2 + 2)
print("The answer is ", sp.integrate(fx, (x, 1, 3)))

# (d)
fx = sp.exp(x) * sp.sin(x)
print("The answer is ", sp.integrate(fx, (x, 0, sp.pi / 2)))
