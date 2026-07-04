"""
Experiment 3: Fixed-Point Iteration Method
"""

import math


def fixed_point(phi, x0, tol=1e-4, N=100, verbose=True):
    if verbose:
        print(f"{'n':>3} {'x_n':>12} {'x_(n+1)':>12} {'|diff|':>12}")

    x1 = x0
    for n in range(N):
        x1 = phi(x0)
        diff = abs(x1 - x0)
        if verbose:
            print(f"{n:>3} {x0:>12.6f} {x1:>12.6f} {diff:>12.6f}")
        if diff < tol:
            return x1
        x0 = x1
    return x1


def estimate_k(phi, root, h=1e-5):
    """Numerically estimate k = |phi'(root)| (central difference)."""
    return abs((phi(root + h) - phi(root - h)) / (2 * h))


def predict_iterations(k, tol=1e-4, x0_err=1.0):
    """Rough iteration count predicted from linear convergence: k^n * err0 < tol."""
    if k <= 0 or k >= 1:
        return None
    return math.ceil(math.log(tol / x0_err) / math.log(k))


if __name__ == "__main__":

    print("\n--- Q1: x^3 + x^2 - 1 = 0, phi(x) = 1/sqrt(1+x), x0=0.75 ---")
    phi = lambda x: 1 / math.sqrt(1 + x)
    root = fixed_point(phi, 0.75, tol=1e-4)
    print("Root ~", round(root, 4), " k=|phi'(root)| ~", round(estimate_k(phi, root), 4))

    print("\n--- Q2: 2x - 3 = cos(x), phi(x) = 0.5*(3+cos x), x0=1.5 ---")
    phi = lambda x: 0.5 * (3 + math.cos(x))
    root = fixed_point(phi, 1.5, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q3: x*e^x = 1, phi(x) = e^-x, x0=0.5 ---")
    phi = lambda x: math.exp(-x)
    root = fixed_point(phi, 0.5, tol=1e-4, N=50)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q4: sin(x) = 10(x-1), phi(x) = 1 + sin(x)/10, x0=1 ---")
    phi = lambda x: 1 + math.sin(x) / 10
    root = fixed_point(phi, 1, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q5: x = cos(x), phi(x) = cos(x), x0=0.5 ---")
    phi = lambda x: math.cos(x)
    root = fixed_point(phi, 0.5, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q6: x^2 - x - 3 = 0, phi(x) = sqrt(x+3), x0=2 ---")
    phi = lambda x: math.sqrt(x + 3)
    root = fixed_point(phi, 2, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q7: x^2 - 2x - 5 = 0, phi(x) = sqrt(2x+5), x0=3 ---")
    phi = lambda x: math.sqrt(2 * x + 5)
    root = fixed_point(phi, 3, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q8: x^3 + 4x^2 - 10 = 0, phi(x) = 0.5*sqrt(10-x^3), x0=1.5 ---")
    phi = lambda x: 0.5 * math.sqrt(10 - x**3)
    root = fixed_point(phi, 1.5, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q9: x^3 - 3x + 1 = 0 (root in [0,1]), phi(x) = (x^3+1)/3, x0=0.5 ---")
    phi = lambda x: (x**3 + 1) / 3
    root = fixed_point(phi, 0.5, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q10: e^-x = x, phi(x) = e^-x, x0=0.5 ---")
    phi = lambda x: math.exp(-x)
    root = fixed_point(phi, 0.5, tol=1e-4, N=50)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q11: tan(x) = x near 4.5, phi(x) = pi + atan(x), x0=4.5 ---")
    phi = lambda x: math.pi + math.atan(x)
    root = fixed_point(phi, 4.5, tol=1e-4)
    print("Root ~", round(root, 4), " k ~", round(estimate_k(phi, root), 4))

    print("\n--- Q12: k = max|phi'| and predicted iterations for eps=1e-4 ---")
    problems = [
        ("Q1", lambda x: 1 / math.sqrt(1 + x), 0.7549),
        ("Q2", lambda x: 0.5 * (3 + math.cos(x)), 1.5237),
        ("Q3", lambda x: math.exp(-x), 0.5671),
        ("Q4", lambda x: 1 + math.sin(x) / 10, 1.0),
        ("Q5", lambda x: math.cos(x), 0.7391),
        ("Q6", lambda x: math.sqrt(x + 3), 2.3028),
        ("Q7", lambda x: math.sqrt(2 * x + 5), 3.7016),
        ("Q8", lambda x: 0.5 * math.sqrt(10 - x**3), 1.3652),
        ("Q9", lambda x: (x**3 + 1) / 3, 0.3473),
        ("Q10", lambda x: math.exp(-x), 0.5671),
        ("Q11", lambda x: math.pi + math.atan(x), 4.4934),
    ]
    print(f"{'Problem':>8} {'k=|phi_prime|':>15} {'Predicted n':>13}")
    for name, phi, root in problems:
        k = estimate_k(phi, root)
        n_pred = predict_iterations(k)
        print(f"{name:>8} {k:>15.4f} {str(n_pred):>13}")