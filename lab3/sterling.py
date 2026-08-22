import math

def forward_diff_table(y):
    n = len(y)
    D = [[0.0]*n for _ in range(n)]
    for i in range(n):
        D[0][i] = y[i]
    for k in range(1, n):
        for i in range(n-k):
            D[k][i] = D[k-1][i+1] - D[k-1][i]
    return D

def print_diff_table(x, y):
    D = forward_diff_table(y)
    n = len(y)
    header = "x\ty"
    for k in range(1, n):
        header += f"\tD^{k}"
    print(header)
    for i in range(n):
        row = f"{x[i]}\t{D[0][i]}"
        for k in range(1, n-i):
            row += f"\t{D[k][i]}"
        print(row)
    print()

def stirling(x, y, c, X):
    n = len(y)
    h = x[1] - x[0]
    D = forward_diff_table(y)
    p = (X - x[c]) / h
    yp = y[c]
    if c - 1 >= 0 and c < n - 1:
        yp += p * (D[1][c-1] + D[1][c]) / 2
    if c - 1 >= 0 and c - 1 <= n - 3:
        yp += (p**2) / math.factorial(2) * D[2][c-1]
    if c - 2 >= 0 and c - 1 <= n - 4 and c - 2 <= n - 4:
        yp += p * (p**2 - 1) / math.factorial(3) * (D[3][c-2] + D[3][c-1]) / 2
    if c - 2 >= 0 and c - 2 <= n - 5:
        yp += (p**2) * (p**2 - 1) / math.factorial(4) * D[4][c-2]
    return yp

def problem1():
    x = [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67]
    y = [math.e**xi for xi in x]
    print("Problem 1: e^x at 0.61(0.01)0.67, find e^0.644 (central node 0.64)")
    print_diff_table(x, y)
    c = x.index(0.64)
    print(f"e^0.644 (Stirling) = {stirling(x, y, c, 0.644)}, actual = {math.e**0.644}")
    print()

def problem2():
    x = [0, 10, 20, 30, 40, 50, 60]
    y = [1.00000, 0.98481, 0.93969, 0.86603, 0.76604, 0.64279, 0.50000]
    print("Problem 2: cos theta at 0(10)60, find cos(25) (central node 30)")
    c = x.index(30)
    print(f"cos(25deg) (Stirling) = {stirling(x, y, c, 25)}, actual = {math.cos(math.radians(25))}")
    print()

def problem3():
    x = [0, 10, 20, 30, 40]
    y = [math.sin(math.radians(xi)) for xi in x]
    print("Problem 3: sin x at 0(10)40, find sin(16)")
    c = x.index(20)
    print(f"sin(16deg) (Stirling) = {stirling(x, y, c, 16)}, actual = {math.sin(math.radians(16))}")
    print()

def problem4():
    x = [20, 21, 22, 23, 24]
    y = [0.342, 0.358, 0.374, 0.391, 0.407]
    print("Problem 4: y at x=20..24, estimate y(22.4)")
    c = x.index(22)
    print(f"y(22.4) (Stirling) = {stirling(x, y, c, 22.4)}")
    print()

def gauss_forward(x, y, c, X, max_order=None):
    n = len(y)
    h = x[1] - x[0]
    D = forward_diff_table(y)
    p = (X - x[c]) / h
    if max_order is None:
        max_order = n - 1
    yp = y[c]
    P = 1.0
    for k in range(1, max_order + 1):
        if k == 1:
            f = p
        elif k % 2 == 0:
            f = p - (k // 2)
        else:
            f = p + ((k - 1) // 2)
        P *= f
        idx = c - (k // 2)
        if idx < 0 or idx > n - 1 - k:
            break
        term = P / math.factorial(k) * D[k][idx]
        yp += term
    return yp

def gauss_backward(x, y, c, X, max_order=None):
    n = len(y)
    h = x[1] - x[0]
    D = forward_diff_table(y)
    p = (X - x[c]) / h
    if max_order is None:
        max_order = n - 1
    yp = y[c]
    P = 1.0
    for k in range(1, max_order + 1):
        if k == 1:
            f = p
        elif k % 2 == 0:
            f = p + (k // 2)
        else:
            f = p - ((k - 1) // 2)
        P *= f
        idx = c - ((k + 1) // 2)
        if idx < 0 or idx > n - 1 - k:
            break
        term = P / math.factorial(k) * D[k][idx]
        yp += term
    return yp

def bessel(x, y, c, X):
    n = len(y)
    h = x[1] - x[0]
    D = forward_diff_table(y)
    p = (X - x[c]) / h
    yp = (y[c] + y[c+1]) / 2 if c + 1 < n else y[c]
    yp += (p - 0.5) * D[1][c]
    if c - 1 >= 0 and c + 1 < n:
        yp += p * (p - 1) / math.factorial(2) * (D[2][c-1] + D[2][c]) / 2
    return yp

def problem5():
    x = [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67]
    y = [math.e**xi for xi in x]
    c = x.index(0.64)
    X = 0.644
    print("Problem 5: compare Stirling and Bessel for p near 0")
    print(f"Stirling estimate = {stirling(x, y, c, X)}")
    print(f"Bessel estimate = {bessel(x, y, c, X)}")
    print(f"actual = {math.e**X}")
    print()

def problem6():
    x = [0.20, 0.22, 0.24, 0.26, 0.28]
    y = [math.tan(xi) for xi in x]
    print("Problem 6: tan x at 0.20(0.02)0.28, estimate tan(0.245)")
    c = x.index(0.24)
    print(f"tan(0.245) (Stirling) = {stirling(x, y, c, 0.245)}, actual = {math.tan(0.245)}")
    print()

def problem7():
    x = [2.0, 2.1, 2.2, 2.3, 2.4]
    y = [math.log10(xi) for xi in x]
    print("Problem 7: log10 x at 2.0(0.1)2.4, estimate log10(2.21)")
    c = x.index(2.2)
    stirling_val = stirling(x, y, c, 2.21)
    newton_x = x
    def forward_interp(x, y, X):
        n = len(x)
        h = x[1] - x[0]
        D = forward_diff_table(y)
        p = (X - x[0]) / h
        yp = y[0]
        term = 1.0
        for k in range(1, n):
            term *= (p - (k-1)) / k
            yp += term * D[k][0]
        return yp
    newton_val = forward_interp(x, y, 2.21)
    actual = math.log10(2.21)
    print(f"Stirling = {stirling_val}, error = {abs(stirling_val-actual)}")
    print(f"Newton forward = {newton_val}, error = {abs(newton_val-actual)}")
    print()

def problem8():
    x = [-2, -1, 0, 1, 2]
    y = [0.135, 0.368, 1.000, 2.718, 7.389]
    print("Problem 8: f at x=-2..2 (=e^x), estimate f(0.5)")
    c = x.index(0)
    print(f"f(0.5) (Stirling) = {stirling(x, y, c, 0.5)}, actual = {math.e**0.5}")
    print()

def problem9():
    x = [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67]
    y = [math.e**xi for xi in x]
    c = x.index(0.64)
    X = 0.644
    stirling_val = stirling(x, y, c, X)
    forward_val = gauss_forward(x, y, c, X)
    backward_val = gauss_backward(x, y, c, X)
    print("Problem 9: verify Stirling equals mean of Gauss forward and backward")
    print(f"Gauss forward = {forward_val}")
    print(f"Gauss backward = {backward_val}")
    print(f"mean = {(forward_val+backward_val)/2}")
    print(f"Stirling = {stirling_val}")
    print()

def problem10():
    x = [20, 30, 40, 50, 60]
    y = [0.798, 1.203, 1.612, 2.023, 2.436]
    print("Problem 10: thermocouple emf at T=20..60, estimate emf at T=42")
    c = x.index(40)
    print(f"emf(42) (Stirling) = {stirling(x, y, c, 42)}")
    print()

def problem11():
    x = [-2, -1, 0, 1, 2]
    y = [0.135, 0.368, 1.000, 2.718, 7.389]
    print("Problem 11: estimate y and y' at the central node from a 5-point table")
    c = x.index(0)
    h = x[1] - x[0]
    D = forward_diff_table(y)
    yprime = (D[1][c-1] + D[1][c]) / (2*h) - 0 * D[3][c-2] if c-2 >= 0 else (D[1][c-1]+D[1][c])/(2*h)
    print(f"y(0) = {y[c]}")
    print(f"y'(0) approx = {(D[1][c-1] + D[1][c]) / (2*h)}")
    print(f"actual y'(0) = {math.e**0}")
    print()

def problem12():
    x = [1.0, 1.1, 1.2, 1.3, 1.4]
    y = [0.7652, 0.7196, 0.6711, 0.6201, 0.5669]
    print("Problem 12: J0(x) at x=1.0(0.1)1.4, estimate J0(1.22)")
    c = x.index(1.2)
    print(f"J0(1.22) (Stirling) = {stirling(x, y, c, 1.22)}")
    print()

def worked_example_5_1():
    x = [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67]
    y = [math.e**xi for xi in x]
    print("Worked Example 5.1: e^0.644 by Stirling's formula")
    print_diff_table(x, y)
    c = x.index(0.64)
    print(f"e^0.644 = {stirling(x, y, c, 0.644)}")
    print()

def main():
    worked_example_5_1()
    problem1()
    problem2()
    problem3()
    problem4()
    problem5()
    problem6()
    problem7()
    problem8()
    problem9()
    problem10()
    problem11()
    problem12()

if __name__ == "__main__":
    main()