"""
Experiment 8: Ramanujan's Method (Smallest Root)
===================================================

For each polynomial/series f(x)=0, we first rewrite it in the standard form
    f(x) = 1 - (a1*x + a2*x^2 + a3*x^3 + ...)
by dividing through so the constant term is 1. The a-coefficients below are
derived from each equation as shown in the comments.
"""

import math


def ramanujan(a_coeffs, M=15, tol=1e-6, verbose=True):
    b = [0.0] * (M + 1)
    b[1] = 1.0
    for k in range(2, M + 1):
        s = 0.0
        for j in range(1, k):
            if j <= len(a_coeffs):
                s += a_coeffs[j - 1] * b[k - j]
        b[k] = s

    if verbose:
        print(f"{'n':>3} {'b_n':>14} {'convergent c_n':>16}")
        print(f"{1:>3} {b[1]:>14.6f} {'':>16}")

    c_prev, root = None, None
    for i in range(2, M + 1):
        if b[i] == 0:
            continue
        c = b[i - 1] / b[i]
        if verbose:
            print(f"{i:>3} {b[i]:>14.6f} {c:>16.6f}")
        if c_prev is not None and abs(c - c_prev) < tol:
            root = c
            break
        c_prev = c
        root = c
    return root


if __name__ == "__main__":

    print("\n--- Q1: x^3-9x^2+26x-24=0 (roots 2,3,4) ---")
    # divide by -24: f(x) = 1 - (13/12 x - 3/8 x^2 + 1/24 x^3)
    a = [13 / 12, -3 / 8, 1 / 24]
    root = ramanujan(a, M=25, tol=1e-5)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q2: x*e^x = 1 (expand e^x as a series) ---")
    # x*e^x - 1 = 0  =>  x*e^x = x + x^2 + x^3/2! + x^4/3! + ...
    # f(x) = 1 - (x + x^2 + x^3/2 + x^4/6 + x^5/24 + ...)
    a = [1, 1, 1 / 2, 1 / 6, 1 / 24, 1 / 120, 1 / 720]
    root = ramanujan(a, M=10, tol=1e-5)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q3: 3x - cos(x) - 1 = 0 ---")
    # (from cos x series) f(x) = 1 - (3/2 x + 1/4 x^2 + 0*x^3 - 1/48 x^4 + ...)
    a = [3 / 2, 1 / 4, 0, -1 / 48]
    root = ramanujan(a, M=10, tol=1e-5)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q4: 1 - x + x^2/(2!)^2 - x^3/(3!)^2 + ... = 0 ---")
    a = [1, -1 / 4, 1 / 36, -1 / 576, 1 / 14400]
    root = ramanujan(a, M=10, tol=1e-5)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q5: x^2 - 5x + 6 = 0 (roots 2, 3) ---")
    # divide by 6: f(x) = 1 - (5/6 x - 1/6 x^2)
    a = [5 / 6, -1 / 6]
    root = ramanujan(a, M=25, tol=1e-6)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q6: x^3 - 6x^2 + 11x - 6 = 0 (roots 1, 2, 3) ---")
    # divide by -6: f(x) = 1 - (11/6 x - x^2 + 1/6 x^3)
    a = [11 / 6, -1, 1 / 6]
    root = ramanujan(a, M=25, tol=1e-6)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q7: 2x^2 - 8x + 3 = 0 ---")
    # divide by 3: f(x) = 1 - (8/3 x - 2/3 x^2)
    a = [8 / 3, -2 / 3]
    root = ramanujan(a, M=12, tol=1e-6)
    print("Smallest root ~", round(root, 4))
    exact = (8 - math.sqrt(40)) / 4
    print("Exact value (8 - sqrt(40))/4 =", round(exact, 4))

    print("\n--- Q8: x^3 - 4x^2 + 5x - 2 = 0, (x-1)^2(x-2) ---")
    # divide by -2: f(x) = 1 - (5/2 x - 2x^2 + 1/2 x^3)
    a = [5 / 2, -2, 1 / 2]
    root = ramanujan(a, M=25, tol=1e-6)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q9: x^3 - 2x^2 - 5x + 6 = 0 (roots 1, 3, -2) ---")
    # divide by 6: f(x) = 1 - (5/6 x + 1/3 x^2 - 1/6 x^3)
    a = [5 / 6, 1 / 3, -1 / 6]
    root = ramanujan(a, M=25, tol=1e-6)
    print("Smallest root (magnitude) ~", round(root, 4))

    print("\n--- Q10: 6x^3 - 11x^2 + 6x - 1 = 0 (roots 1, 1/2, 1/3) ---")
    # divide by -1: f(x) = 1 - (6x - 11x^2 + 6x^3)
    a = [6, -11, 6]
    root = ramanujan(a, M=25, tol=1e-6)
    print("Smallest root ~", round(root, 4))

    print("\n--- Q11: Verify Q7 result against exact value ---")
    print("Exact smallest root of 2x^2-8x+3=0 is (8 - sqrt(40))/4 =", round(exact, 4))
    print("Ramanujan convergent from Q7 above should match this closely.")