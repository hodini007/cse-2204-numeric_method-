import math

def inverse_lagrange(x, y, Y):
    n = len(y)
    total = 0.0
    for i in range(n):
        L = 1.0
        for j in range(n):
            if j != i:
                L *= (Y - y[j]) / (y[i] - y[j])
        total += L * x[i]
    return total

def problem1():
    x = [1, 3, 4]
    y = [4, 12, 19]
    print("Problem 1: (1,4),(3,12),(4,19), find x where y=7")
    val = inverse_lagrange(x, y, 7)
    print(f"x = {val}, true value (y=x^2+3) = {math.sqrt(7-3)}")
    print()

def problem2():
    x = [20, 30, 40]
    y = [0.342, 0.500, 0.643]
    print("Problem 2: sin x at 20,30,40, find angle whose sine is 0.45")
    val = inverse_lagrange(x, y, 0.45)
    print(f"angle = {val} deg, actual = {math.degrees(math.asin(0.45))}")
    print()

def problem3():
    x = [2, 4, 6]
    y = [4, 16, 36]
    print("Problem 3: y=x^2 at (2,4),(4,16),(6,36), find x for y=12, compare with sqrt(12)")
    val = inverse_lagrange(x, y, 12)
    print(f"x = {val}, sqrt(12) = {math.sqrt(12)}")
    print()

def problem4():
    x = [1.0, 1.1, 1.2, 1.3]
    y = [2.7183, 3.0042, 3.3201, 3.6693]
    print("Problem 4: e^x at x=1.0,1.1,1.2,1.3, find x such that e^x=3.0")
    val = inverse_lagrange(x, y, 3.0)
    print(f"x = {val}, actual (ln 3) = {math.log(3.0)}")
    print()

def problem5():
    x = [1, 2, 3]
    y = [0.5, 2.0, 4.5]
    print("Problem 5: strain y=0.5x^2 at x=1,2,3, find x where y=3.0, compare with sqrt(6)")
    val = inverse_lagrange(x, y, 3.0)
    print(f"x = {val}, sqrt(6) = {math.sqrt(6)}")
    print()

def problem6():
    x = [2, 3, 4]
    y = [0.3010, 0.4771, 0.6021]
    print("Problem 6: log10 x at x=2,3,4, find x for which log10(x)=0.4")
    val = inverse_lagrange(x, y, 0.4)
    print(f"x = {val}, actual = {10**0.4}")
    print()

def problem7():
    x = [0.5, 0.6, 0.7]
    y = [-0.18, 0.05, 0.30]
    print("Problem 7: estimate the root (x where y=0) near a sign change")
    val = inverse_lagrange(x, y, 0)
    print(f"root x = {val}")
    print()

def problem8():
    x = [10, 20, 30, 40]
    y = [2.1, 4.0, 5.6, 6.9]
    print("Problem 8: calibration table, find input giving output 5.0")
    val = inverse_lagrange(x, y, 5.0)
    print(f"input x = {val}")
    print()

def problem9():
    x = [1.0, 1.1, 1.2, 1.3]
    y = [2.7183, 3.0042, 3.3201, 3.6693]
    print("Problem 9: compare inverse interpolation with Newton-Raphson for f(x)=e^x, target Y=3.0")
    inv_val = inverse_lagrange(x, y, 3.0)
    def newton_raphson(f, fprime, x0, tol=1e-10, max_iter=100):
        xi = x0
        for _ in range(max_iter):
            fx = f(xi)
            if abs(fx) < tol:
                break
            xi = xi - fx / fprime(xi)
        return xi
    nr_val = newton_raphson(lambda t: math.e**t - 3.0, lambda t: math.e**t, 1.1)
    print(f"Inverse interpolation x = {inv_val}")
    print(f"Newton-Raphson x = {nr_val}")
    print(f"exact x = ln(3) = {math.log(3.0)}")
    print()

def problem10():
    x = [20, 30, 40, 50]
    y = [0.798, 1.203, 1.612, 2.023]
    print("Problem 10: thermocouple table, find temperature for emf=1.5 mV")
    val = inverse_lagrange(x, y, 1.5)
    print(f"T = {val}")
    print()

def problem11():
    x = [1, 2, 3, 4, 5]
    y = [2, 5, 6, 5, 2]
    print("Problem 11: find abscissa of maximum by inverse-interpolating f'(x)=0")
    fprime = []
    xmid = []
    for i in range(len(x)-1):
        fprime.append((y[i+1]-y[i])/(x[i+1]-x[i]))
        xmid.append((x[i+1]+x[i])/2)
    print("Midpoint derivative estimates:")
    for xm, fp in zip(xmid, fprime):
        print(f"x={xm}: f'~{fp}")
    val = inverse_lagrange(xmid, fprime, 0)
    print(f"abscissa of maximum (f'=0) = {val}")
    print()

def problem12():
    x = [1, 3, 4, 0]
    y = [4, 12, 19, 3]
    print("Problem 12: add point (0,3) to problem 1 data, recompute x at y=7")
    val = inverse_lagrange(x, y, 7)
    print(f"x = {val} (using 4 points)")
    x3 = [1, 3, 4]
    y3 = [4, 12, 19]
    val3 = inverse_lagrange(x3, y3, 7)
    print(f"x = {val3} (using original 3 points)")
    print(f"true value = {math.sqrt(7-3)}")
    print()

def worked_example_7_1():
    x = [1, 3, 4]
    y = [4, 12, 19]
    print("Worked Example 7.1: find x when y=7")
    val = inverse_lagrange(x, y, 7)
    print(f"x = {val}, true value = 2.0")
    print()

def main():
    worked_example_7_1()
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