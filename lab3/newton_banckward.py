import math

def backward_diff_table(y):
    n = len(y)
    D = [[0.0]*n for _ in range(n)]
    for i in range(n):
        D[0][i] = y[i]
    for k in range(1, n):
        for i in range(k, n):
            D[k][i] = D[k-1][i] - D[k-1][i-1]
    return D

def print_diff_table(x, y):
    D = backward_diff_table(y)
    n = len(y)
    header = "x\ty"
    for k in range(1, n):
        header += f"\tNab^{k}"
    print(header)
    for i in range(n):
        row = f"{x[i]}\t{D[0][i]}"
        for k in range(1, i+1):
            row += f"\t{D[k][i]}"
        print(row)
    print()

def newton_backward(x, y, X):
    n = len(y)
    h = x[1] - x[0]
    D = backward_diff_table(y)
    p = (X - x[n-1]) / h
    yp = y[n-1]
    term = 1.0
    for k in range(1, n):
        term *= (p + (k - 1)) / k
        yp += term * D[k][n-1]
    return yp

def problem1():
    x = [15, 20, 25, 30, 35, 40]
    y = [math.sin(math.radians(xi)) for xi in x]
    print("Problem 1: sin x at 15(5)40, find sin(38)")
    print_diff_table(x, y)
    print(f"sin(38deg) (interp) = {newton_backward(x, y, 38)}, actual = {math.sin(math.radians(38))}")
    print()

def problem2():
    x = [40, 50, 60, 70, 80, 90]
    y = [184, 204, 226, 250, 276, 304]
    print("Problem 2: f at x=40..90, estimate f(85)")
    print(f"f(85) = {newton_backward(x, y, 85)}")
    print()

def problem3():
    x = [1.0, 1.1, 1.2, 1.3, 1.4]
    y = [2.7183, 3.0042, 3.3201, 3.6693, 4.0552]
    print("Problem 3: e^x at 1.0(0.1)1.4, estimate e^1.38")
    print(f"e^1.38 (interp) = {newton_backward(x, y, 1.38)}, actual = {math.e**1.38}")
    print()

def problem4():
    x = [1891, 1901, 1911, 1921, 1931]
    y = [46, 66, 81, 93, 101]
    print("Problem 4: population 1891-1931, estimate population in 1925")
    print(f"population(1925) = {newton_backward(x, y, 1925)}")
    print()

def problem5():
    x = [0.10, 0.15, 0.20, 0.25, 0.30]
    y = [0.1003, 0.1511, 0.2027, 0.2553, 0.3093]
    print("Problem 5: tan x at 0.10(0.05)0.30, estimate tan(0.28)")
    print(f"tan(0.28) = {newton_backward(x, y, 0.28)}")
    print()

def problem6():
    x = [1, 2, 3, 4, 5]
    y = [xi**3 for xi in x]
    print("Problem 6: y=x^3 at x=1..5, estimate y(4.5) by backward formula")
    print(f"y(4.5) = {newton_backward(x, y, 4.5)}")
    print()

def problem7():
    x = [0, 10, 20, 30, 40, 50, 60]
    y = [math.cos(math.radians(xi)) for xi in x]
    print("Problem 7: cos theta at 0(10)60, estimate cos(55)")
    print(f"cos(55deg) (interp) = {newton_backward(x, y, 55)}, actual = {math.cos(math.radians(55))}")
    print()

def problem8():
    x = [1, 2, 3, 4, 5]
    y = [1, 8, 27, 64, 125]
    print("Problem 8: f(1)=1,f(2)=8,f(3)=27,f(4)=64,f(5)=125, find f(4.7)")
    print(f"f(4.7) = {newton_backward(x, y, 4.7)}")
    print()

def problem9():
    x = [300, 310, 320, 330, 340]
    y = [2.4771, 2.4914, 2.5051, 2.5185, 2.5315]
    print("Problem 9: log10 x at x=300..340, estimate log10(337)")
    print(f"log10(337) = {newton_backward(x, y, 337)}")
    print()

def problem10():
    x = [100, 110, 120, 130, 140]
    y = [101.3, 143.3, 198.5, 270.1, 361.3]
    print("Problem 10: steam pressure T=100..140, estimate pressure at T=138")
    print(f"pressure(138) = {newton_backward(x, y, 138)}")
    print()

def problem11():
    x = [1, 2, 3, 4, 5]
    y = [2, 5, 10, 17, 26]
    print("Problem 11: verify backward formula reproduces tabulated values exactly at nodes")
    for i in range(len(x)):
        val = newton_backward(x, y, x[i])
        print(f"x={x[i]}: interp = {val}, actual = {y[i]}")
    print()

def problem12():
    x = [2016, 2017, 2018, 2019, 2020, 2021]
    y = [12, 15, 20, 27, 39, 52]
    print("Problem 12: yearly sales 2016-2021, estimate sales at 2020.5")
    print(f"sales(2020.5) = {newton_backward(x, y, 2020.5)}")
    print()

def worked_example_3_1():
    x = [15, 20, 25, 30, 35, 40]
    y = [math.sin(math.radians(xi)) for xi in x]
    print("Worked Example 3.1: sin(38 deg) from a table of sines")
    print_diff_table(x, y)
    print(f"sin(38deg) = {newton_backward(x, y, 38)}")
    print()

def main():
    worked_example_3_1()
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