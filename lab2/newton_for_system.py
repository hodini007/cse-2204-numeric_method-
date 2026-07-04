"""
Experiment 10: Newton-Raphson Method for Systems

For each system f(x,y)=0, g(x,y)=0, the four partial derivatives
fx, fy, gx, gy are listed and used in the Newton/Jacobian update.
"""

import math


def newton_system(f, g, fx, fy, gx, gy, x0, y0, tol=1e-6, N=100, verbose=True):
    if verbose:
        print(f"{'n':>3} {'x_n':>10} {'y_n':>10}")
        print(f"{0:>3} {x0:>10.6f} {y0:>10.6f}")

    for n in range(1, N + 1):
        f0, g0 = f(x0, y0), g(x0, y0)
        Fx, Fy = fx(x0, y0), fy(x0, y0)
        Gx, Gy = gx(x0, y0), gy(x0, y0)
        D = Fx * Gy - Gx * Fy
        if D == 0:
            raise ZeroDivisionError("Jacobian is zero")
        h = (-f0 * Gy + g0 * Fy) / D
        k = (-g0 * Fx + f0 * Gx) / D
        x0, y0 = x0 + h, y0 + k
        if verbose:
            print(f"{n:>3} {x0:>10.6f} {y0:>10.6f}")
        if abs(h) < tol and abs(k) < tol:
            return x0, y0
    return x0, y0


if __name__ == "__main__":

    print("\n--- Q1: 3yx^2-10x+7=0, y^2-5y+4=0; start (0.5, 0.5) ---")
    print("fx=6yx-10, fy=3x^2, gx=0, gy=2y-5")
    f = lambda x, y: 3 * y * x**2 - 10 * x + 7
    g = lambda x, y: y**2 - 5 * y + 4
    fx = lambda x, y: 6 * y * x - 10
    fy = lambda x, y: 3 * x**2
    gx = lambda x, y: 0
    gy = lambda x, y: 2 * y - 5
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 0.5, 0.5, tol=1e-5)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q2: x^2+y^2-1=0, y-x^2=0; start (0.8, 0.6) ---")
    print("fx=2x, fy=2y, gx=-2x, gy=1")
    f = lambda x, y: x**2 + y**2 - 1
    g = lambda x, y: y - x**2
    fx = lambda x, y: 2 * x
    fy = lambda x, y: 2 * y
    gx = lambda x, y: -2 * x
    gy = lambda x, y: 1
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 0.8, 0.6, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q3: sin(x)-y+0.9793=0, cos(y)-x+0.6703=0; start (0.5, 1.5) ---")
    print("fx=cos(x), fy=-1, gx=-1, gy=-sin(y)")
    f = lambda x, y: math.sin(x) - y + 0.9793
    g = lambda x, y: math.cos(y) - x + 0.6703
    fx = lambda x, y: math.cos(x)
    fy = lambda x, y: -1
    gx = lambda x, y: -1
    gy = lambda x, y: -math.sin(y)
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 0.5, 1.5, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q4: x^2+xy+y^2-7=0, x^3+y^3-9=0; start (1.5, 0.5) ---")
    print("fx=2x+y, fy=x+2y, gx=3x^2, gy=3y^2")
    f = lambda x, y: x**2 + x * y + y**2 - 7
    g = lambda x, y: x**3 + y**3 - 9
    fx = lambda x, y: 2 * x + y
    fy = lambda x, y: x + 2 * y
    gx = lambda x, y: 3 * x**2
    gy = lambda x, y: 3 * y**2
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 1.5, 0.5, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q5: x^2-2x-y+0.5=0, x^2+4y^2-4=0; start (2, 0.25) ---")
    print("fx=2x-2, fy=-1, gx=2x, gy=8y")
    f = lambda x, y: x**2 - 2 * x - y + 0.5
    g = lambda x, y: x**2 + 4 * y**2 - 4
    fx = lambda x, y: 2 * x - 2
    fy = lambda x, y: -1
    gx = lambda x, y: 2 * x
    gy = lambda x, y: 8 * y
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 2, 0.25, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q6: x^2+y^2-4=0, xy-1=0; start (1.9, 0.6) ---")
    print("fx=2x, fy=2y, gx=y, gy=x")
    f = lambda x, y: x**2 + y**2 - 4
    g = lambda x, y: x * y - 1
    fx = lambda x, y: 2 * x
    fy = lambda x, y: 2 * y
    gx = lambda x, y: y
    gy = lambda x, y: x
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 1.9, 0.6, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q7: e^x-y=0, xy-e^x=0; start (0.8, 1.5) ---")
    print("fx=e^x, fy=-1, gx=y-e^x, gy=x")
    f = lambda x, y: math.exp(x) - y
    g = lambda x, y: x * y - math.exp(x)
    fx = lambda x, y: math.exp(x)
    fy = lambda x, y: -1
    gx = lambda x, y: y - math.exp(x)
    gy = lambda x, y: x
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 0.8, 1.5, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q8: x^2+y-11=0, x+y^2-7=0; start (3.5, 1.8) ---")
    print("fx=2x, fy=1, gx=1, gy=2y")
    f = lambda x, y: x**2 + y - 11
    g = lambda x, y: x + y**2 - 7
    fx = lambda x, y: 2 * x
    fy = lambda x, y: 1
    gx = lambda x, y: 1
    gy = lambda x, y: 2 * y
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 3.5, 1.8, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q9: x^2-y-1=0, x-y^2+1=0; start (1.5, 1.5) ---")
    print("fx=2x, fy=-1, gx=1, gy=-2y")
    f = lambda x, y: x**2 - y - 1
    g = lambda x, y: x - y**2 + 1
    fx = lambda x, y: 2 * x
    fy = lambda x, y: -1
    gx = lambda x, y: 1
    gy = lambda x, y: -2 * y
    x_r, y_r = newton_system(f, g, fx, fy, gx, gy, 1.5, 1.5, tol=1e-6)
    print(f"Root ~ ({round(x_r,4)}, {round(y_r,4)})")

    print("\n--- Q10 (Application, 2-link robot arm L1=L2=1) ---")
    print("cos(t1)+cos(t1+t2)=1.2, sin(t1)+sin(t1+t2)=0.8; start (0, 1.5)")
    f = lambda t1, t2: math.cos(t1) + math.cos(t1 + t2) - 1.2
    g = lambda t1, t2: math.sin(t1) + math.sin(t1 + t2) - 0.8
    fx = lambda t1, t2: -math.sin(t1) - math.sin(t1 + t2)
    fy = lambda t1, t2: -math.sin(t1 + t2)
    gx = lambda t1, t2: math.cos(t1) + math.cos(t1 + t2)
    gy = lambda t1, t2: math.cos(t1 + t2)
    t1_r, t2_r = newton_system(f, g, fx, fy, gx, gy, 0, 1.5, tol=1e-6)
    print(f"Root ~ (theta1, theta2) = ({round(t1_r,4)}, {round(t2_r,4)}) rad")

    print("\n--- Q11: Verify (2,1) is an exact root of Q4's system ---")
    f4 = lambda x, y: x**2 + x * y + y**2 - 7
    g4 = lambda x, y: x**3 + y**3 - 9
    print(f"f(2,1) = {f4(2,1)}, g(2,1) = {g4(2,1)}  -> both 0, so (2,1) is an exact root.")
    print("Whether the iteration converges to (2,1) or another root depends on the")
    print("starting point (1.5, 0.5) and the shape of the two curves near it.")