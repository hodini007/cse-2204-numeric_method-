from math import comb

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
    return D

def find_missing_value(y, missing_index, degree):
    n = len(y)
    order = degree + 1
    coeffs = [(-1)**r * comb(order, r) for r in range(order+1)]
    known_sum = 0
    missing_coeff = 0
    for r in range(order+1):
        idx = n - 1 - r
        if idx == missing_index:
            missing_coeff = coeffs[r]
        else:
            known_sum += coeffs[r] * y[idx]
    return -known_sum / missing_coeff


def problem1():
    x = [-1, 0, 1, 2, 3, 4]
    y = [(xi**3 - 3*xi**2 + 5*xi - 7) for xi in x]
    print("Problem 1: f(x) = x^3 - 3x^2 + 5x - 7")
    D = print_diff_table(x, y)
    n = len(y)
    print(f"Delta^3 f0 = {D[3][0]}")
    print(f"Delta^4 f0 = {D[4][0]}")
    print()

def problem2():
    y = [1, 3, 9, None, 81]
    print("Problem 2: y = 1, 3, 9, ?, 81 with Delta^4 y0 = 0")
    missing = find_missing_value(y, 3, 3)
    print(f"Missing value y3 = {missing}")
    print()

def problem3():
    x = [1951, 1961, 1971, 1981, 1991]
    y = [35, 42, 58, 84, 120]
    print("Problem 3: Population census data")
    print_diff_table(x, y)


def problem8():
    u = [25, 35, 52, 70, 91, 116, 145]
    x = list(range(len(u)))
    print("Problem 8: locate and correct the wrong value using difference spread")
    print_diff_table(x, u)
    print("Inspect Delta^3 and Delta^4 columns for a sign-alternating spike to locate the error.")
    print()


def backward_diff_table(y):
    n = len(y)
    D = [[0.0]*n for _ in range(n)]
    for i in range(n):
        D[0][i] = y[i]
    for k in range(1, n):
        for i in range(k, n):
            D[k][i] = D[k-1][i] - D[k-1][i-1]
    return D

def central_diff_table(y):
    return forward_diff_table(y)

def problem10():
    x = [1, 2, 3, 4, 5]
    y = [xi**4 for xi in x]
    print("Problem 10: Forward, backward and central difference tables for y = x^4")
    print("Forward difference table:")
    print_diff_table(x, y)
    Db = backward_diff_table(y)
    n = len(y)
    print("Backward difference table:")
    header = "x\ty"
    for k in range(1, n):
        header += f"\tNab^{k}"
    print(header)
    for i in range(n):
        row = f"{x[i]}\t{Db[0][i]}"
        for k in range(1, i+1):
            row += f"\t{Db[k][i]}"
        print(row)
    print()



def problem12():
    x = [1, 2, 3, 4, 5]
    y = [xi**4 for xi in x]
    Df = forward_diff_table(y)
    Db = backward_diff_table(y)
    print("Problem 12: verify Delta^2 y1 = Nabla^2 y3 = delta^2 y2 using data of problem 10")
    delta2_y1 = Df[2][1]
    nabla2_y3 = Db[2][3]
    print(f"Delta^2 y1 = {delta2_y1}")
    print(f"Nabla^2 y3 = {nabla2_y3}")
    print(f"Nabla^4 y4 = {Db[4][4]}")
    print()

def worked_example_1_1():
    x = [0, 1, 2, 3, 4]
    y = [xi**3 for xi in x]
    print("Worked Example 1.1: forward difference table of y = x^3")
    print_diff_table(x, y)

def worked_example_1_2():
    y = [1, 3, 9, None, 81]
    print("Worked Example 1.2: missing tabular value")
    missing = find_missing_value(y, 3, 3)
    print(f"y3 = {missing}")
    print()

def main():
    worked_example_1_1()
    worked_example_1_2()
    problem1()
    problem2()
    problem3()
    problem8()
    problem10()
    problem12()

if __name__ == "__main__":
    main()
    