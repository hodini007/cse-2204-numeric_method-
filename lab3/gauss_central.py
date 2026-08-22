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

def problem1():
    x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
    y = [math.e**xi for xi in x]
    print("Problem 1: e^x at 1.00(0.05)1.30, find e^1.17 (central node 1.15, p=0.4)")
    print_diff_table(x, y)
    c = x.index(1.15)
    print(f"e^1.17 (Gauss forward) = {gauss_forward(x, y, c, 1.17)}, actual = {math.e**1.17}")
    print()

def problem2():
    x = [20, 30, 40, 50, 60]
    y = [math.sin(math.radians(xi)) for xi in x]
    print("Problem 2: sin theta at 20(10)60, find sin(35) by Gauss's forward formula")
    c = x.index(30)
    print(f"sin(35deg) (Gauss forward) = {gauss_forward(x, y, c, 35)}, actual = {math.sin(math.radians(35))}")
    print()

def problem3():
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [1, 8, 27, 64, 125, 216, 343]
    print("Problem 3: y at x=0..6, find y(3.3)")
    c = x.index(3)
    print(f"y(3.3) (Gauss forward) = {gauss_forward(x, y, c, 3.3)}")
    print()

def problem4():
    x = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    y = [0, 0.176, 0.301, 0.477, 0.602, 0.699, 0.778]
    print("Problem 4: log10 x at x=1.0(0.5)4.0, estimate log10(2.6)")
    c = x.index(2.5)
    print(f"log10(2.6) (Gauss forward) = {gauss_forward(x, y, c, 2.6)}, actual = {math.log10(2.6)}")
    print()

def problem5():
    x = [0.10, 0.15, 0.20, 0.25, 0.30]
    y = [0.1003, 0.1511, 0.2027, 0.2553, 0.3093]
    print("Problem 5: tan x at 0.10(0.05)0.30, find tan(0.21) by a central formula")
    c = x.index(0.20)
    print(f"tan(0.21) (Gauss forward) = {gauss_forward(x, y, c, 0.21)}")
    print()

def problem6():
    x = [-2, -1, 0, 1, 2]
    y = [2.626, 0.342, 0, 0.342, 2.626]
    print("Problem 6: f at x=-2..2, estimate f(0.25) (central node 0)")
    c = x.index(0)
    print(f"f(0.25) (Gauss forward) = {gauss_forward(x, y, c, 0.25)}")
    print()

def problem7():
    x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
    y = [math.e**xi for xi in x]
    print("Problem 7: e^x table, Gauss backward about x0=1.20 (p=-0.6), confirm agreement with forward result")
    c = x.index(1.20)
    print(f"e^1.17 (Gauss backward) = {gauss_backward(x, y, c, 1.17)}, actual = {math.e**1.17}")
    print()

def problem8():
    x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    y = [math.e**(-xi) for xi in x]
    print("Problem 8: e^-x at 0.0(0.1)0.6, estimate e^-0.27")
    c = x.index(0.3)
    print(f"e^-0.27 (Gauss backward) = {gauss_backward(x, y, c, 0.27)}, actual = {math.e**(-0.27)}")
    print()

def problem9():
    x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
    y = [math.e**xi for xi in x]
    print("Problem 9: 7-point table, interpolate at p=0.3 about the centre")
    c = x.index(1.15)
    X = x[c] + 0.3 * (x[1] - x[0])
    for order in range(1, 5):
        val = gauss_forward(x, y, c, X, max_order=order)
        print(f"order={order}: estimate = {val}")
    print(f"actual = {math.e**X}")
    print()

def problem10():
    x = [10, 20, 30, 40, 50]
    y = [2.1, 4.0, 5.6, 6.9, 8.0]
    print("Problem 10: calibration table, find the reading at input 33")
    c = x.index(30)
    print(f"reading(33) (Gauss forward) = {gauss_forward(x, y, c, 33)}")
    print()

def problem11():
    x = [0.50, 0.52, 0.54, 0.56, 0.58]
    y = [1.1276, 1.1417, 1.1561, 1.1707, 1.1855]
    print("Problem 11: cosh x at 0.5(0.02)0.58, estimate cosh(0.552)")
    c = x.index(0.54)
    print(f"cosh(0.552) (Gauss forward) = {gauss_forward(x, y, c, 0.552)}, actual = {math.cosh(0.552)}")
    print()

def problem12():
    x = [0, 1, 2, 3, 4]
    y = [1, 4, 9, 16, 25]
    print("Problem 12: central zig-zag for Gauss forward and backward on a 5-point set")
    D = forward_diff_table(y)
    print_diff_table(x, y)
    c = 2
    print(f"Shared central second difference used by both formulae: Delta^2 y at index {c-1} = {D[2][c-1]}")
    print()

def worked_example_4_1():
    x = [1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30]
    y = [math.e**xi for xi in x]
    print("Worked Example 4.1: e^1.17 by Gauss's forward formula")
    print_diff_table(x, y)
    c = x.index(1.15)
    print(f"e^1.17 = {gauss_forward(x, y, c, 1.17)}")
    print()

def main():
    worked_example_4_1()
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