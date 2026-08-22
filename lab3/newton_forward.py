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

def newton_forward(x, y, X):
    n = len(y)
    h = x[1] - x[0]
    D = forward_diff_table(y)
    p = (X - x[0]) / h
    yp = y[0]
    term = 1.0
    for k in range(1, n):
        term *= (p - (k - 1)) / k
        yp += term * D[k][0]
    return yp

def problem1():
    x = [1, 3, 5, 7]
    y = [24, 120, 336, 720]
    print("Problem 1: (1,24),(3,120),(5,336),(7,720), find y(2)")
    print_diff_table(x, y)
    print(f"y(2) = {newton_forward(x, y, 2)}")
    print()

def problem2():
    x = [1, 2, 3, 4, 5]
    y = [xi**3 for xi in x]
    print("Problem 2: y = x^3, estimate y(1.5)")
    print(f"y(1.5) = {newton_forward(x, y, 1.5)}")
    print()

def problem3():
    x = [40, 50, 60, 70, 80, 90]
    y = [184, 204, 226, 250, 276, 304]
    print("Problem 3: f at x=40..90, find f(43)")
    print(f"f(43) = {newton_forward(x, y, 43)}")
    print()

def problem4():
    x = [1.0, 1.1, 1.2, 1.3, 1.4]
    y = [2.7183, 3.0042, 3.3201, 3.6693, 4.0552]
    print("Problem 4: e^x at x=1.0(0.1)1.4, estimate e^1.05")
    print(f"e^1.05 (interp) = {newton_forward(x, y, 1.05)}, actual = {math.e**1.05}")
    print()

def problem5():
    x = [1891, 1901, 1911, 1921, 1931]
    y = [46, 66, 81, 93, 101]
    print("Problem 5: population 1891-1931, estimate population in 1895")
    print(f"population(1895) = {newton_forward(x, y, 1895)}")
    print()

def problem6():
    x = [0.10, 0.15, 0.20, 0.25, 0.30]
    y = [0.1003, 0.1511, 0.2027, 0.2553, 0.3093]
    print("Problem 6: tan x at 0.10(0.05)0.30, find tan(0.12)")
    print(f"tan(0.12) = {newton_forward(x, y, 0.12)}")
    print()

def problem7():
    x = [0, 10, 20, 30, 40]
    y = [math.sin(math.radians(xi)) for xi in x]
    print("Problem 7: sin theta at 0,10,20,30,40, estimate sin(5)")
    print(f"sin(5deg) (interp) = {newton_forward(x, y, 5)}, actual = {math.sin(math.radians(5))}")
    print()

def problem8():
    print("Problem 8: sum_{k=1}^{n} k^2 as polynomial in n by Newton's forward formula")
    n_vals = [1, 2, 3, 4, 5]
    sums = []
    total = 0
    for nv in n_vals:
        total += nv**2
        sums.append(total)
    x = n_vals
    y = sums
    print_diff_table(x, y)
    print("The differences show a cubic pattern, consistent with n(n+1)(2n+1)/6")
    for nv in range(1, 8):
        print(f"n={nv}: interp = {newton_forward(x, y, nv)}, formula = {nv*(nv+1)*(2*nv+1)/6}")
    print()

def problem9():
    x = [0, 1, 2, 3]
    y = [1, 0, 1, 10]
    print("Problem 9: f(0)=1,f(1)=0,f(2)=1,f(3)=10, find cubic and f(0.5)")
    print_diff_table(x, y)
    print(f"f(0.5) = {newton_forward(x, y, 0.5)}")
    print()

def problem10():
    x = [1, 2, 3, 4, 5]
    y = [0, 0.3010, 0.4771, 0.6021, 0.6990]
    print("Problem 10: log10 x at x=1..5, estimate log10(1.5)")
    print(f"log10(1.5) (interp) = {newton_forward(x, y, 1.5)}, actual = {math.log10(1.5)}")
    print("Accuracy is only fair because x=1.5 lies between the first two nodes,")
    print("where the function log10(x) is changing rapidly relative to the polynomial fit.")
    print()

def problem11():
    x = [0, 5, 10, 15, 20]
    y = [0.99987, 0.99999, 0.99973, 0.99913, 0.99823]
    print("Problem 11: density of water at T=0,5,10,15,20, estimate density at T=3")
    print(f"density(3) = {newton_forward(x, y, 3)}")
    print()

def problem12():
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 1, 8, 27, 64, 125]
    print("Problem 12: y at x=0..5 = 0,1,8,27,64,125, build table and confirm Delta^3 constant")
    D = forward_diff_table(y)
    print_diff_table(x, y)
    print(f"Delta^3 y0 = {D[3][0]}, Delta^3 y1 = {D[3][1]}, Delta^3 y2 = {D[3][2]}")
    print("Polynomial fit is y = x^3")
    print()

def worked_example_2_1():
    x = [1, 3, 5, 7]
    y = [24, 120, 336, 720]
    print("Worked Example 2.1: cubic through four points")
    print_diff_table(x, y)
    print(f"y(8) = {newton_forward(x, y, 8)}")
    print()

def worked_example_2_2():
    print("Worked Example 2.2: sum of cubes Sn = 1^3+2^3+...+n^3")
    n_vals = [1, 2, 3, 4, 5]
    sums = []
    total = 0
    for nv in n_vals:
        total += nv**3
        sums.append(total)
    print_diff_table(n_vals, sums)
    for nv in n_vals:
        formula = (nv*(nv+1)/2)**2
        print(f"n={nv}: Sn(formula) = {formula}, actual = {sums[nv-1]}")
    print()

def main():
    worked_example_2_1()
    worked_example_2_2()
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