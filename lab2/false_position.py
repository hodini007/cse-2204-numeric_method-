"""
Experiment 2: Method of False Position

"""

import math


def false_position(f, a, b, tol=1e-4, N=100, verbose=True):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    if verbose:
        print(f"{'n':>3} {'a':>10} {'b':>10} {'x':>12} {'f(x)':>12}")

    x = a
    for n in range(1, N + 1):
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        if verbose:
            print(f"{n:>3} {a:>10.6f} {b:>10.6f} {x:>12.6f} {fx:>12.6f}")
        if abs(fx) < tol:
            return x
        if fa * fx < 0:
            b, fb = x, fx
        else:
            a, fa = x, fx
    return x


if __name__ == "__main__":

    print("\n--- Q1: x^3 - 2x - 5 = 0 in [2, 3] ---")
    f = lambda x: x**3 - 2 * x - 5
    root = false_position(f, 2, 3, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q2: x^2.2 - 69 = 0 in [5, 8] ---")
    f = lambda x: x**2.2 - 69
    root = false_position(f, 5, 8, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q3: 2x - log10(x) - 7 = 0 in [3, 4] ---")
    f = lambda x: 2 * x - math.log10(x) - 7
    root = false_position(f, 3, 4, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q4: 4*e^-x*sin(x) - 1 = 0 in [0, 0.5] ---")
    f = lambda x: 4 * math.exp(-x) * math.sin(x) - 1
    root = false_position(f, 0, 0.5, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q5: x^3 - x - 1 = 0 in [1, 2] ---")
    f = lambda x: x**3 - x - 1
    root = false_position(f, 1, 2, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q6: cos(x) - x*e^x = 0 in [0, 1] ---")
    f = lambda x: math.cos(x) - x * math.exp(x)
    root = false_position(f, 0, 1, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q7: x*log10(x) - 1.2 = 0 in [2, 3] ---")
    f = lambda x: x * math.log10(x) - 1.2
    root = false_position(f, 2, 3, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q8: x^3 + x^2 - 3x - 3 = 0 in [1, 2] ---")
    f = lambda x: x**3 + x**2 - 3 * x - 3
    root = false_position(f, 1, 2, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q9: ln(x) - x + 2 = 0 in [3, 4] ---")
    f = lambda x: math.log(x) - x + 2
    root = false_position(f, 3, 4, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q10: x - e^-x = 0 in [0, 1] ---")
    f = lambda x: x - math.exp(-x)
    root = false_position(f, 0, 1, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q11: e^-x - sin(x) = 0 in [0, 1] ---")
    f = lambda x: math.exp(-x) - math.sin(x)
    root = false_position(f, 0, 1, tol=1e-4)
    print("Root ~", round(root, 4))

    print("\n--- Q12 (Application): catenary c*sinh(4/c) - 5 = 0 in [3, 4] ---")
    f = lambda c: c * math.sinh(4 / c) - 5
    root = false_position(f, 3, 4, tol=1e-4)
    print("Catenary parameter c ~", round(root, 4))