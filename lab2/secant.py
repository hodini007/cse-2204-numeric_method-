"""
Experiment 7: Secant Method
"""

import math


def secant(f, x0, x1, tol=1e-6, N=100, verbose=True):
    f0, f1 = f(x0), f(x1)
    if verbose:
        print(f"{'n':>3} {'x_n':>12} {'f(x_n)':>14}")

    x2 = x1
    for n in range(N):
        if f1 - f0 == 0:
            raise ZeroDivisionError("Division by zero in secant formula")
        x2 = (x0 * f1 - x1 * f0) / (f1 - f0)
        f2 = f(x2)
        if verbose:
            print(f"{n:>3} {x2:>12.6f} {f2:>14.6f}")
        if abs(x2 - x1) < tol:
            return x2
        x0, f0 = x1, f1
        x1, f1 = x2, f2
    return x2


if __name__ == "__main__":

    print("\n--- Q1: x^3 - 2x - 5 = 0, x0=2, x1=3 ---")
    f = lambda x: x**3 - 2 * x - 5
    root = secant(f, 2, 3, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q2: x*e^x - 1 = 0, x0=0, x1=1 ---")
    f = lambda x: x * math.exp(x) - 1
    root = secant(f, 0, 1, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q3: x^3 - x - 1 = 0, x0=1, x1=2 ---")
    f = lambda x: x**3 - x - 1
    root = secant(f, 1, 2, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q4: cos(x) - x*e^x = 0, x0=0, x1=1 ---")
    f = lambda x: math.cos(x) - x * math.exp(x)
    root = secant(f, 0, 1, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q5: x - cos(x) = 0, x0=0, x1=1 ---")
    f = lambda x: x - math.cos(x)
    root = secant(f, 0, 1, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q6: x^2.2 - 69 = 0, x0=5, x1=8 ---")
    f = lambda x: x**2.2 - 69
    root = secant(f, 5, 8, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q7: x^4 - x - 10 = 0, x0=1, x1=2 ---")
    f = lambda x: x**4 - x - 10
    root = secant(f, 1, 2, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q8: e^x - 3x = 0, x0=0, x1=1 ---")
    f = lambda x: math.exp(x) - 3 * x
    root = secant(f, 0, 1, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q9: ln(x) - x + 2 = 0, x0=3, x1=4 ---")
    f = lambda x: math.log(x) - x + 2
    root = secant(f, 3, 4, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q10: x*sin(x) - 1 = 0, x0=1, x1=2 ---")
    f = lambda x: x * math.sin(x) - 1
    root = secant(f, 1, 2, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q11: tan(x) - x = 0, x0=4.4, x1=4.6 ---")
    f = lambda x: math.tan(x) - x
    root = secant(f, 4.4, 4.6, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q12 (Application): Colebrook friction factor, f0=0.01, f1=0.03 ---")

    def colebrook(fr):
        return 1 / math.sqrt(fr) + 2 * math.log10(
            1e-4 / 3.7 + 2.51 / (1e5 * math.sqrt(fr))
        )

    root = secant(colebrook, 0.01, 0.03, tol=1e-6)
    print("Friction factor f ~", round(root, 5))