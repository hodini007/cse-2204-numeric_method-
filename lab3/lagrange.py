import math

def lagrange(x, y, X):
    n = len(x)
    total = 0.0
    for i in range(n):
        L = 1.0
        for j in range(n):
            if j != i:
                L *= (X - x[j]) / (x[i] - x[j])
        total += L * y[i]
    return total

def lagrange_polynomial_string(x, y):
    n = len(x)
    print("Basis polynomials li(x):")
    for i in range(n):
        num_terms = []
        den = 1.0
        for j in range(n):
            if j != i:
                num_terms.append(f"(x-{x[j]})")
                den *= (x[i] - x[j])
        print(f"l{i}(x) = " + "*".join(num_terms) + f" / {den}")
    print()

def problem1():
    x = [300, 304, 305, 307]
    y = [2.4771, 2.4829, 2.4843, 2.4871]
    print("Problem 1: log10 x at 300,304,305,307, find log10(301)")
    print(f"log10(301) = {lagrange(x, y, 301)}, actual = {math.log10(301)}")
    print()

def problem2():
    x = [2.0, 2.5, 3.0]
    y = [0.69315, 0.91629, 1.09861]
    print("Problem 2: ln x at 2.0,2.5,3.0, find quadratic and ln(2.7)")
    val = lagrange(x, y, 2.7)
    actual = math.log(2.7)
    print(f"ln(2.7) = {val}, actual = {actual}, error = {abs(val-actual)}")
    print()

def problem3():
    x = [0, math.pi/4, math.pi/2]
    y = [0, 0.70711, 1.0]
    print("Problem 3: sin x at 0,pi/4,pi/2, estimate sin(pi/6)")
    val = lagrange(x, y, math.pi/6)
    print(f"sin(pi/6) = {val}, actual = {math.sin(math.pi/6)}")
    print()

def problem4():
    x = [0, 1, 2, 5]
    y = [2, 3, 12, 147]
    print("Problem 4: (0,2),(1,3),(2,12),(5,147), find y(3)")
    print(f"y(3) = {lagrange(x, y, 3)}")
    print()

def problem5():
    x = [5, 6, 9, 11]
    y = [12, 13, 14, 16]
    print("Problem 5: (5,12),(6,13),(9,14),(11,16), find y(10)")
    print(f"y(10) = {lagrange(x, y, 10)}")
    print()

def problem6():
    x = [1, 2, 4, 7]
    y = [1, 8, 64, 343]
    print("Problem 6: (1,1),(2,8),(4,64),(7,343) (data of x^3), find y(3)")
    print(f"y(3) = {lagrange(x, y, 3)}, actual x^3 = {3**3}")
    print()

def problem7():
    x = [0, 1, 3, 4]
    y = [-12, 0, 12, 24]
    print("Problem 7: (0,-12),(1,0),(3,12),(4,24), recover polynomial and check")
    for xv in x:
        print(f"y({xv}) = {lagrange(x, y, xv)}")
    print()

def problem8():
    x = [1, 2, 4]
    print("Problem 8: for nodes 1,2,4, write basis polynomials and verify sum li(x)=1, li(xj)=delta_ij")
    y_dummy = [1, 0, 0]
    lagrange_polynomial_string(x, y_dummy)
    for xj in x:
        total = 0
        for i in range(len(x)):
            L = 1.0
            for j in range(len(x)):
                if j != i:
                    L *= (xj - x[j]) / (x[i] - x[j])
            total += L
            if xj == x[i]:
                print(f"l{i}({xj}) = {L} (should be 1)")
            else:
                print(f"l{i}({xj}) = {L} (should be 0)")
        print(f"sum li({xj}) = {total}")
    print()

def problem9():
    x = [0, 1, 3, 4]
    y = [1, 3, 55, 99]
    print("Problem 9: f(0)=1,f(1)=3,f(3)=55,f(4)=99, fit cubic and estimate f(2)")
    print(f"f(2) = {lagrange(x, y, 2)}")
    print()

def problem10():
    x = [0, 1, 2, 5]
    y = [2, 3, 12, 147]
    print("Problem 10: compare Lagrange with Newton divided-difference for data of problem 4")
    def divided_diff(x, y):
        n = len(x)
        coef = y[:]
        table = [coef[:]]
        for k in range(1, n):
            new_row = []
            for i in range(n-k):
                val = (table[k-1][i+1] - table[k-1][i]) / (x[i+k] - x[i])
                new_row.append(val)
            table.append(new_row)
        return [row[0] for row in table]
    dd = divided_diff(x, y)
    def newton_dd_eval(x, dd, X):
        n = len(dd)
        result = dd[0]
        prod = 1.0
        for i in range(1, n):
            prod *= (X - x[i-1])
            result += dd[i] * prod
        return result
    for xv in [3, 4]:
        print(f"x={xv}: Lagrange = {lagrange(x, y, xv)}, Newton divided-diff = {newton_dd_eval(x, dd, xv)}")
    print()

def problem11():
    R = [27.3, 10.0, 4.16, 0.97]
    T = [0, 25, 50, 100]
    print("Problem 11: thermistor R(T), estimate T when R=6.0 (interpolate T as function of R)")
    print(f"T (R=6.0) = {lagrange(R, T, 6.0)}")
    print()

def problem12():
    x = [0, 1, 2, 3]
    y = [0, 1, 16, 81]
    print("Problem 12: estimate y(2.5) from cubic fit to x^4 data, compare with exact")
    val = lagrange(x, y, 2.5)
    actual = 2.5**4
    print(f"y(2.5) (cubic Lagrange) = {val}, actual (x^4) = {actual}, error = {abs(val-actual)}")
    print()

def worked_example_6_1():
    x = [300, 304, 305, 307]
    y = [2.4771, 2.4829, 2.4843, 2.4871]
    print("Worked Example 6.1: log10(301) from four points")
    print(f"log10(301) = {lagrange(x, y, 301)}")
    print()

def worked_example_6_2():
    x = [2.0, 2.5, 3.0]
    y = [0.69315, 0.91629, 1.09861]
    print("Worked Example 6.2: quadratic for ln x, then ln(2.7)")
    val = lagrange(x, y, 2.7)
    print(f"ln(2.7) = {val}, true value = 0.9932518, error = {abs(val-0.9932518)}")
    print()

def main():
    worked_example_6_1()
    worked_example_6_2()
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