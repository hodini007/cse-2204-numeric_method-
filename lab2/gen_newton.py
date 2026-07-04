"""
Experiment 6: Generalized Newton's Method (Multiple Roots)
"""


def generalized_newton(f, fprime, p, x0, tol=1e-6, N=100, verbose=True):
    if verbose:
        print(f"{'n':>3} {'x_n':>12} {'f(x_n)':>14} {'x_(n+1)':>12}")

    x1 = x0
    for n in range(N):
        fx0 = f(x0)
        if abs(fx0) < 1e-12:
            if verbose:
                print(f"{n:>3} {x0:>12.6f} {fx0:>14.6f} {x0:>12.6f}  (already at root)")
            return x0
        fpx0 = fprime(x0)
        if fpx0 == 0:
            raise ZeroDivisionError("Zero derivative - choose another x0")
        x1 = x0 - p * fx0 / fpx0
        if verbose:
            print(f"{n:>3} {x0:>12.6f} {fx0:>14.6f} {x1:>12.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x1


def newton_raphson(f, fprime, x0, tol=1e-6, N=100, verbose=False):
    """Plain Newton (p=1), used for Q11 comparison."""
    x1 = x0
    for n in range(N):
        fx0 = f(x0)
        fpx0 = fprime(x0)
        x1 = x0 - fx0 / fpx0
        if verbose:
            print(f"{n:>3} {x0:>12.6f}")
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x1


if __name__ == "__main__":

    print("\n--- Q1: x^3-x^2-x+1=0, (x-1)^2(x+1), p=2, x0=0.8 ---")
    f = lambda x: x**3 - x**2 - x + 1
    fp = lambda x: 3 * x**2 - 2 * x - 1
    root = generalized_newton(f, fp, 2, 0.8, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q2: x^3-3x+2=0, (x-1)^2(x+2), p=2, x0=1.2 ---")
    f = lambda x: x**3 - 3 * x + 2
    fp = lambda x: 3 * x**2 - 3
    root = generalized_newton(f, fp, 2, 1.2, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q3: x^3-5x^2+8x-4=0, (x-1)(x-2)^2, p=2, x0=1.8 ---")
    f = lambda x: x**3 - 5 * x**2 + 8 * x - 4
    fp = lambda x: 3 * x**2 - 10 * x + 8
    root = generalized_newton(f, fp, 2, 1.8, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q4: x^3-x^2-8x+12=0, (x-2)^2(x+3), p=2, x0=1.8 ---")
    f = lambda x: x**3 - x**2 - 8 * x + 12
    fp = lambda x: 3 * x**2 - 2 * x - 8
    root = generalized_newton(f, fp, 2, 1.8, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q5: x^3+3x^2+3x+1=0, (x+1)^3, p=3, x0=-0.7 ---")
    f = lambda x: x**3 + 3 * x**2 + 3 * x + 1
    fp = lambda x: 3 * x**2 + 6 * x + 3
    root = generalized_newton(f, fp, 3, -0.7, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q6: x^3-6x^2+12x-8=0, (x-2)^3, p=3, x0=1.7 ---")
    f = lambda x: x**3 - 6 * x**2 + 12 * x - 8
    fp = lambda x: 3 * x**2 - 12 * x + 12
    root = generalized_newton(f, fp, 3, 1.7, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q7: x^4-4x^3+6x^2-4x+1=0, (x-1)^4, p=4, x0=1.3 ---")
    f = lambda x: x**4 - 4 * x**3 + 6 * x**2 - 4 * x + 1
    fp = lambda x: 4 * x**3 - 12 * x**2 + 12 * x - 4
    root = generalized_newton(f, fp, 4, 1.3, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q8: x^4-2x^2+1=0, (x^2-1)^2, p=2 (root +1), x0=1.2 ---")
    f = lambda x: x**4 - 2 * x**2 + 1
    fp = lambda x: 4 * x**3 - 4 * x
    root = generalized_newton(f, fp, 2, 1.2, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q9: x^4-8x^2+16=0, (x^2-4)^2, p=2 (root +2), x0=1.8 ---")
    f = lambda x: x**4 - 8 * x**2 + 16
    fp = lambda x: 4 * x**3 - 16 * x
    root = generalized_newton(f, fp, 2, 1.8, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q10: x^4+2x^3-3x^2-4x+4=0, (x-1)^2(x+2)^2, p=2, x0=0.7 ---")
    f = lambda x: x**4 + 2 * x**3 - 3 * x**2 - 4 * x + 4
    fp = lambda x: 4 * x**3 + 6 * x**2 - 6 * x - 4
    root = generalized_newton(f, fp, 2, 0.7, tol=1e-6)
    print("Root ~", round(root, 4))

    print("\n--- Q11: Q1 revisited - plain Newton (p=1) vs generalized Newton (p=2) ---")
    f = lambda x: x**3 - x**2 - x + 1
    fp = lambda x: 3 * x**2 - 2 * x - 1
    print("Plain Newton (p=1) iterates:")
    x0 = 0.8
    for i in range(8):
        x1 = x0 - f(x0) / fp(x0)
        print(f"  n={i}: x = {x0:.6f}")
        x0 = x1
    print(f"  (converging slowly toward 1.0 -- linear convergence at a double root)")
    print("\nGeneralized Newton (p=2):")
    root = generalized_newton(f, fp, 2, 0.8, tol=1e-8, verbose=True)
    print("Root ~", round(root, 6), " -- converges quadratically, in far fewer steps.")