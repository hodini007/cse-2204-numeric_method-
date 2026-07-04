'''experiment 1 : bisection method
    all example solved '''

import math


def bisection(f, a, b, tol=1e-4, N=100, verbose=True):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    if verbose:
        print(f"{'n':>3} {'a':>10} {'b':>10} {'x':>12} {'f(x)':>12}")

    x = a
    for n in range(1, N + 1):
        x = (a + b) / 2
        fx = f(x)
        if verbose:
            print(f"{n:>3} {a:>10.6f} {b:>10.6f} {x:>12.6f} {fx:>12.6f}")
        if abs(fx) < 1e-12 or (b - a) / 2 < tol:
            return x
        if fa * fx < 0:
            b = x
        else:
            a, fa = x, fx
    return x


if __name__ == "__main__":

    print("\n--- Q1: x^3 - x - 1 = 0 in [1, 2] ---")
    f = lambda x: x**3 - x - 1
    root = bisection(f, 1, 2, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q2: x^3 - 2x - 5 = 0 in [2, 3] (3 d.p.) ---")
    f = lambda x: x**3 - 2 * x - 5
    root = bisection(f, 2, 3, tol=1e-3)
    print("Root ~", round(root, 3))

    print("\n--- Q3: x^3 + x^2 + x + 7 = 0 in [-3, -2] (3 d.p.) ---")
    f = lambda x: x**3 + x**2 + x + 7
    root = bisection(f, -3, -2, tol=1e-3)
    print("Root ~", round(root, 3))

    print("\n--- Q4: x^3 - 4x - 9 = 0 in [2, 3] ---")
    f = lambda x: x**3 - 4 * x - 9
    root = bisection(f, 2, 3, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q5: x^4 - x - 10 = 0 in [1, 2] ---")
    f = lambda x: x**4 - x - 10
    root = bisection(f, 1, 2, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q6: x - cos(x) = 0 in [0, 1] ---")
    f = lambda x: x - math.cos(x)
    root = bisection(f, 0, 1, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q7: x*e^x - 1 = 0 in [0, 1] ---")
    f = lambda x: x * math.exp(x) - 1
    root = bisection(f, 0, 1, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q8: 3x - cos(x) - 1 = 0 in [0, 1] ---")
    f = lambda x: 3 * x - math.cos(x) - 1
    root = bisection(f, 0, 1, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q9: e^x - 3x = 0 : root in [0,1] ---")
    f = lambda x: math.exp(x) - 3 * x
    root1 = bisection(f, 0, 1, tol=1e-4)
    print("Root 1 ~", round(root1, 4))
    print("\n--- Q9: e^x - 3x = 0 : root in [1,2] ---")
    root2 = bisection(f, 1, 2, tol=1e-4)
    print("Root 2 ~", round(root2, 4))

    print("\n--- Q10: x*sin(x) - 1 = 0 in [1, 2] ---")
    f = lambda x: x * math.sin(x) - 1
    root = bisection(f, 1, 2, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q11: ln(x) - x + 2 = 0 in [3, 4] ---")
    f = lambda x: math.log(x) - x + 2
    root = bisection(f, 3, 4, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q12 (Application): h^3 - 3h^2 + 2.4 = 0 in [1, 2] (3 d.p.) ---")
    f = lambda h: h**3 - 3 * h**2 + 2.4
    root = bisection(f, 1, 2, tol=1e-3)
    print("Submerged depth h ~", round(root, 3), "m")