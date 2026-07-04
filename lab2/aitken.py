"""
Experiment 4: Aitken's Delta^2 Acceleration
=============================================
Solves all exercise problems from Section 6 (Exercise 4) of the lab manual.
Applies Aitken's process to the phi(x) iterations used in Experiment 3.
"""

import math


def aitken(phi, x0, tol=1e-4, N=100, verbose=True):
    x_hat = x0
    for n in range(N):
        x1 = phi(x0)
        x2 = phi(x1)
        denom = x2 - 2 * x1 + x0
        if denom == 0:
            return x2
        x_hat = x2 - (x2 - x1) ** 2 / denom
        if verbose:
            print(f"{n:>3} {x0:>10.6f} {x1:>10.6f} {x2:>10.6f} {x_hat:>12.6f}")
        if abs(x_hat - x0) < tol:
            return x_hat
        x0 = x_hat  # restart from the accelerated value
    return x_hat


def aitken_step(x0, x1, x2):
    """One Aitken step given three raw iterates (no phi needed)."""
    denom = x2 - 2 * x1 + x0
    return x2 - (x2 - x1) ** 2 / denom


if __name__ == "__main__":
    header = f"{'n':>3} {'x0':>10} {'x1':>10} {'x2':>10} {'x_hat':>12}"

    print("\n--- Q1: phi(x) = 0.5*(3+cos x), x0=1.5 ---")
    print(header)
    phi = lambda x: 0.5 * (3 + math.cos(x))
    root = aitken(phi, 1.5, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q2: phi(x) = e^-x, x0=0.5 (slow case, Ex 3.2) ---")
    print(header)
    phi = lambda x: math.exp(-x)
    root = aitken(phi, 0.5, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q3: phi(x) = cos(x), x0=0.5 ---")
    print(header)
    phi = lambda x: math.cos(x)
    root = aitken(phi, 0.5, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q4: phi(x) = 1/sqrt(1+x), x0=0.75 ---")
    print(header)
    phi = lambda x: 1 / math.sqrt(1 + x)
    root = aitken(phi, 0.75, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q5: phi(x) = sqrt(x+3), x0=2 ---")
    print(header)
    phi = lambda x: math.sqrt(x + 3)
    root = aitken(phi, 2, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q6: phi(x) = 0.5*sqrt(10-x^3), x0=1.5 ---")
    print(header)
    phi = lambda x: 0.5 * math.sqrt(10 - x**3)
    root = aitken(phi, 1.5, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q7: phi(x) = 1 + sin(x)/10, x0=1 ---")
    print(header)
    phi = lambda x: 1 + math.sin(x) / 10
    root = aitken(phi, 1, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q8: x^3+x^2-2=0, phi(x) = (2-x^2)^(1/3), x0=0.8 ---")
    print(header)
    phi = lambda x: (2 - x**2) ** (1 / 3)
    root = aitken(phi, 0.8, tol=1e-4)
    print("Accelerated root ~", round(root, 4))

    print("\n--- Q9: Given iterates 0.6, 0.69, 0.737 -> one Aitken step ---")
    result = aitken_step(0.6, 0.69, 0.737)
    print("Aitken estimate ~", round(result, 4))

    print("\n--- Q10: Given iterates 1.0, 0.9, 0.832 -> one Aitken step ---")
    result = aitken_step(1.0, 0.9, 0.832)
    print("Aitken estimate ~", round(result, 4))

    print("\n--- Q11: Ex 3.2 (xe^x=1, phi=e^-x, x0=0.5) - plain vs Aitken side by side ---")
    phi = lambda x: math.exp(-x)
    x0 = 0.5
    print(f"{'n':>3} {'plain x_n':>12} {'aitken x_hat':>14}")
    x_plain = x0
    x_acc = x0
    for n in range(8):
        x_plain_next = phi(x_plain)
        # one Aitken triple starting from current accelerated estimate
        a = x_acc
        b = phi(a)
        c = phi(b)
        denom = c - 2 * b + a
        x_acc_next = c - (c - b) ** 2 / denom if denom != 0 else c
        print(f"{n:>3} {x_plain_next:>12.6f} {x_acc_next:>14.6f}")
        x_plain = x_plain_next
        x_acc = x_acc_next
    print("Plain iteration needs ~19 steps (per manual); Aitken converges in ~2-3 triples.")