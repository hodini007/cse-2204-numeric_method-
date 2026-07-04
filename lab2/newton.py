"""
Experiment 5: Newton-Raphson Method
"""

import math


def newton_raphson(f, fprime, x0, tol=1e-6, N=100, verbose=True):
    if verbose:
        print(f"{'n':>3} {'x_n':>12} {'f(x_n)':>14} {'f_prime(x_n)':>14}")

    x1 = x0
    for n in range(N):
        fx0 = f(x0)
        fpx0 = fprime(x0)
        if fpx0 == 0:
            raise ZeroDivisionError("Zero derivative - choose another x0")
        x1 = x0 - fx0 / fpx0
        if verbose:
            print(f"{n:>3} {x0:>12.6f} {fx0:>14.6f} {fpx0:>14.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x1


if __name__ == "__main__":

    print("\n--- Q1: x^3 - 2x - 5 = 0, x0=2 ---")
    f = lambda x: x**3 - 2 * x - 5
    fp = lambda x: 3 * x**2 - 2
    root = newton_raphson(f, fp, 2, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q2: x*sin(x) + cos(x) = 0, x0=pi ---")
    f = lambda x: x * math.sin(x) + math.cos(x)
    fp = lambda x: x * math.cos(x)
    root = newton_raphson(f, fp, math.pi, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q3: x*e^x - 1 = 0, x0=1 ---")
    f = lambda x: x * math.exp(x) - 1
    fp = lambda x: math.exp(x) * (1 + x)
    root = newton_raphson(f, fp, 1, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q4: sin(x) = x/2, x0=pi/2 (root in [pi/2, pi]) ---")
    f = lambda x: math.sin(x) - x / 2
    fp = lambda x: math.cos(x) - 0.5
    root = newton_raphson(f, fp, math.pi / 2, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q5: 4*e^-x*sin(x) - 1 = 0, x0=0.2 ---")
    f = lambda x: 4 * math.exp(-x) * math.sin(x) - 1
    fp = lambda x: 4 * math.exp(-x) * (math.cos(x) - math.sin(x))
    root = newton_raphson(f, fp, 0.2, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q6: x^3 - x - 1 = 0, x0=1.5 ---")
    f = lambda x: x**3 - x - 1
    fp = lambda x: 3 * x**2 - 1
    root = newton_raphson(f, fp, 1.5, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q7: cos(x) - x*e^x = 0, x0=0.5 ---")
    f = lambda x: math.cos(x) - x * math.exp(x)
    fp = lambda x: -math.sin(x) - math.exp(x) * (1 + x)
    root = newton_raphson(f, fp, 0.5, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q8: x^4 - x - 10 = 0, x0=2 ---")
    f = lambda x: x**4 - x - 10
    fp = lambda x: 4 * x**3 - 1
    root = newton_raphson(f, fp, 2, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q9: e^x - 3x = 0, x0=0.5 ---")
    f = lambda x: math.exp(x) - 3 * x
    fp = lambda x: math.exp(x) - 3
    root1 = newton_raphson(f, fp, 0.5, tol=1e-5)
    print("Root 1 ~", round(root1, 4))
    print("\n--- Q9: e^x - 3x = 0, x0=1.5 ---")
    root2 = newton_raphson(f, fp, 1.5, tol=1e-5)
    print("Root 2 ~", round(root2, 4))

    print("\n--- Q10: x - tan(x) = 0, smallest positive root, x0=4.5 ---")
    f = lambda x: x - math.tan(x)
    fp = lambda x: 1 - 1 / math.cos(x) ** 2
    root = newton_raphson(f, fp, 4.5, tol=1e-5)
    print("Root ~", round(root, 4))

    print("\n--- Q11: sqrt(24.5) via x^2 - 24.5 = 0, x0=5 ---")
    f = lambda x: x**2 - 24.5
    fp = lambda x: 2 * x
    root = newton_raphson(f, fp, 5, tol=1e-6)
    print("Root ~", round(root, 4), " (check: math.sqrt(24.5) =", round(math.sqrt(24.5), 4), ")")

    print("\n--- Q12: cube root of 17 via x^3 - 17 = 0, x0=2.5 ---")
    f = lambda x: x**3 - 17
    fp = lambda x: 3 * x**2
    root = newton_raphson(f, fp, 2.5, tol=1e-6)
    print("Root ~", round(root, 4), " (check: 17**(1/3) =", round(17 ** (1 / 3), 4), ")")