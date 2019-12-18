import math
import sympy as sp
sp.init_printing()



def newton(f, df, x0, eps, max_iter):
    x = x0
    for n in range(max_iter):
        fx = f(x)
        if abs(fx) < eps:
            print('Found solution after', n, 'iterations.')
            return x
        dfx = df(x)
        if dfx == 0:
            print('Zero derivative. No solution found.')
            return None
        x = x - fx / dfx
    print('Exceeded maximum iterations. No solution found.')
    return None


x = sp.Symbol('x')
f = sp.Rational(1, 2) + sp.Rational(1, 4) * x * x - x * sp.sin(x) - sp.Rational(1, 2) * sp.cos(2 * x)
f