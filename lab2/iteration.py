"""
Experiment 9: Iteration Method for Systems of Nonlinear Equations
====================================================================
Solves all exercise problems from Section 11 (Exercise 9) of the lab manual.

For each system f(x,y)=0, g(x,y)=0, we rearrange it as x=F(x,y), y=G(x,y)
choosing the branch/form that keeps |Fx|+|Fy|<1 and |Gx|+|Gy|<1 near the
root, as required by the manual's convergence condition.
"""

import math


def iteration_system(F, G, x0, y0, tol=1e-4, N=200, verbose=True):
    if verbose:
        print(f"{'n':>3} {'x_n':>10} {'y_n':>10}")
        print(f"{0:>3} {x0:>10.6f} {y0:>10.6f}")

    x1, y1 = x0, y0
    for n in range(1, N + 1):
        x1 = F(x0, y0)
        y1 = G(x0, y0)
        if verbose:
            print(f"{n:>3} {x1:>10.6f} {y1:>10.6f}")
        if abs(x1 - x0) < tol and abs(y1 - y0) < tol:
            return x1, y1
        x0, y0 = x1, y1
    return x1, y1


if __name__ == "__main__":

    print("\n--- Q1: y^2-5y+4=0, 3yx^2-10x+7=0; start (0.5, 0.5) ---")
    F = lambda x, y: (3 * y * x**2 + 7) / 10
    G = lambda x, y: (y**2 + 4) / 5
    x_r, y_r = iteration_system(F, G, 0.5, 0.5, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q2: x^2+y^2-4=0, xy-1=0; start (1.9, 0.5) ---")
    F = lambda x, y: math.sqrt(4 - y**2)
    G = lambda x, y: 1 / x
    x_r, y_r = iteration_system(F, G, 1.9, 0.5, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q3: x^2-2x-y+0.5=0, x^2+4y^2-4=0; start (0, 1) ---")
    F = lambda x, y: 1 - math.sqrt(max(0.0, y + 0.5))
    G = lambda x, y: math.sqrt(max(0.0, (4 - x**2) / 4))
    x_r, y_r = iteration_system(F, G, 0, 1, tol=1e-4, N=500)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q4: x^2+y^2-1=0, y-x^2=0; start (0.8, 0.6) ---")
    F = lambda x, y: math.sqrt(max(0.0, y))
    G = lambda x, y: math.sqrt(max(0.0, 1 - x**2))
    x_r, y_r = iteration_system(F, G, 0.8, 0.6, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q5: x=(x^2+y^2+8)/10, y=(xy^2+x+8)/10; start (0, 0) ---")
    F = lambda x, y: (x**2 + y**2 + 8) / 10
    G = lambda x, y: (x * y**2 + x + 8) / 10
    x_r, y_r = iteration_system(F, G, 0, 0, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q6: sin(x)+y^2-1=0, x+cos(y)-1.2=0; start (0.5, 0.5) ---")
    F = lambda x, y: 1.2 - math.cos(y)
    G = lambda x, y: math.sqrt(max(0.0, 1 - math.sin(x)))
    x_r, y_r = iteration_system(F, G, 0.5, 0.5, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q7: x=0.5+0.2*sin(x+y), y=1+0.1*cos(x-y); start (0.5, 1) ---")
    F = lambda x, y: 0.5 + 0.2 * math.sin(x + y)
    G = lambda x, y: 1 + 0.1 * math.cos(x - y)
    x_r, y_r = iteration_system(F, G, 0.5, 1, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q8: 2x^2-xy-5x+1=0, x+3log10(x)-y^2=0; start (3.5, 2.2) ---")
    F = lambda x, y: ((y + 5) + math.sqrt(max(0.0, (y + 5) ** 2 - 8))) / 4
    G = lambda x, y: math.sqrt(max(0.0, x + 3 * math.log10(x)))
    x_r, y_r = iteration_system(F, G, 3.5, 2.2, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q9: x^2+y-11=0, x+y^2-7=0; start (3.5, 1.8) ---")
    F = lambda x, y: math.sqrt(max(0.0, 11 - y))
    G = lambda x, y: math.sqrt(max(0.0, 7 - x))
    x_r, y_r = iteration_system(F, G, 3.5, 1.8, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})  (exact root is (3, 2))")

    print("\n--- Q10: x^2-y-1=0, x-y^2+1=0; start (1.5, 1.5) ---")
    F = lambda x, y: math.sqrt(max(0.0, y + 1))
    G = lambda x, y: math.sqrt(max(0.0, x + 1))
    x_r, y_r = iteration_system(F, G, 1.5, 1.5, tol=1e-4)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q11: convergence-condition check (numeric partials) at each start ---")

    def check_condition(F, G, x0, y0, h=1e-5):
        Fx = (F(x0 + h, y0) - F(x0 - h, y0)) / (2 * h)
        Fy = (F(x0, y0 + h) - F(x0, y0 - h)) / (2 * h)
        Gx = (G(x0 + h, y0) - G(x0 - h, y0)) / (2 * h)
        Gy = (G(x0, y0 + h) - G(x0, y0 - h)) / (2 * h)
        okF = abs(Fx) + abs(Fy) < 1
        okG = abs(Gx) + abs(Gy) < 1
        return Fx, Fy, Gx, Gy, okF and okG

    # Example check for Q1's F, G at its starting point
    F1 = lambda x, y: (3 * y * x**2 + 7) / 10
    G1 = lambda x, y: (y**2 + 4) / 5
    Fx, Fy, Gx, Gy, ok = check_condition(F1, G1, 0.5, 0.5)
    print(f"Q1 at (0.5,0.5): |Fx|+|Fy|={abs(Fx)+abs(Fy):.4f}, "
          f"|Gx|+|Gy|={abs(Gx)+abs(Gy):.4f} -> condition holds: {ok}")