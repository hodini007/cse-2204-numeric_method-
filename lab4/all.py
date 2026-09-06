import math
import numpy as np


def straight_line_fit(points):
    sx = 0.0
    sy = 0.0
    sxy = 0.0
    sx2 = 0.0

    for x, y in points:
        sx += x
        sy += y
        sxy += x * y
        sx2 += x * x

    m = len(points)
    d = m * sx2 - sx * sx
    a1 = (m * sxy - sx * sy) / d
    x_bar = sx / m
    y_bar = sy / m
    a0 = y_bar - a1 * x_bar
    st = 0.0
    s = 0.0

    for x, y in points:
        st += (y - y_bar) ** 2
        s += (y - (a0 + a1 * x)) ** 2

    cc = math.sqrt((st - s) / st)
    return a0, a1, cc


def polynomial_fit(points):
    n = len(points)
    sx = sum(x for x, y in points)
    sy = sum(y for x, y in points)
    sx2 = sum(x ** 2 for x, y in points)
    sx3 = sum(x ** 3 for x, y in points)
    sx4 = sum(x ** 4 for x, y in points)
    sxy = sum(x * y for x, y in points)
    sx2y = sum((x ** 2) * y for x, y in points)

    A = np.array([
        [n, sx, sx2],
        [sx, sx2, sx3],
        [sx2, sx3, sx4],
    ], dtype=float)

    b = np.array([
        [sy],
        [sxy],
        [sx2y],
    ], dtype=float)

    coeffs = np.linalg.solve(A, b)
    a0 = coeffs[0, 0]
    a1 = coeffs[1, 0]
    a2 = coeffs[2, 0]
    return a0, a1, a2


def multiple_linear_fit(points):
    xsum = 0
    ysum = 0
    zsum = 0
    yzsum = 0
    zxsum = 0
    xxsum = 0
    yysum = 0
    xysum = 0

    for x, y, z in points:
        xsum += x
        ysum += y
        zsum += z
        yzsum += y * z
        zxsum += z * x
        xxsum += x ** 2
        yysum += y ** 2
        xysum += x * y

    A = np.array([
        [len(points), xsum, ysum],
        [xsum, xxsum, xysum],
        [ysum, xysum, yysum],
    ], dtype=float)

    B = np.array([zsum, zxsum, yzsum], dtype=float)
    a0, a1, a2 = np.linalg.solve(A, B)
    return a0, a1, a2


def non_linear_fit(points, g, h, recover):
    transformed = [(g(x, y), h(x, y)) for x, y in points]
    a0, a1, _ = straight_line_fit(transformed)
    return recover(a0, a1)


def parse_points_2d(text):
    pairs = []
    for part in text.split(';'):
        item = part.strip()
        if not item:
            continue
        x_str, y_str = item.split(',')
        pairs.append((float(x_str), float(y_str)))
    return pairs


def parse_points_3d(text):
    triples = []
    for part in text.split(';'):
        item = part.strip()
        if not item:
            continue
        x_str, y_str, z_str = item.split(',')
        triples.append((float(x_str), float(y_str), float(z_str)))
    return triples


def menu():
    print("1. Straight line fit")
    print("2. Polynomial fit")
    print("3. Multiple linear fit")
    print("4. Nonlinear fit")
    print("5. Exit")
    choice = input("Select process: ").strip()
    return choice


def nonlinear_method_menu():
    print("1. Exponential model")
    print("2. Power law model")
    method = input("Select nonlinear method: ").strip()
    return method


def main():
    while True:
        process = menu()
        if process == "5":
            break

        if process == "1":
            data = parse_points_2d(input("Enter points as x,y;x,y: "))
            print(straight_line_fit(data))

        elif process == "2":
            data = parse_points_2d(input("Enter points as x,y;x,y: "))
            print(polynomial_fit(data))

        elif process == "3":
            data = parse_points_3d(input("Enter points as x,y,z;x,y,z: "))
            print(multiple_linear_fit(data))

        elif process == "4":
            method = nonlinear_method_menu()
            data = parse_points_2d(input("Enter points as x,y;x,y: "))
            if method == "1":
                result = non_linear_fit(data, lambda x, y: x, lambda x, y: math.log(y), lambda a0, a1: (math.exp(a0), a1))
                print(result)
            elif method == "2":
                result = non_linear_fit(data, lambda x, y: math.log(x), lambda x, y: math.log(y), lambda a0, a1: (math.exp(a0), a1))
                print(result)
            else:
                print("Invalid nonlinear method")

        else:
            print("Invalid process")

        print()


if __name__ == "__main__":
    main()
