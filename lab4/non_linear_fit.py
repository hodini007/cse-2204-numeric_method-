import math

points = [(1, 2.473), (3, 6.722), (5, 18.274), (7, 49.673), (9, 135.026)]


def fit_line(points):
    sx = 0.0
    sy = 0.0
    sxy = 0.0
    sx2 = 0.0

    for x, y in points:
        sx += x
        sy += y
        sxy += x * y
        sx2 += x * x

    n = len(points)
    d = n * sx2 - sx * sx
    a1 = (n * sxy - sx * sy) / d
    x_bar = sx / n
    y_bar = sy / n
    a0 = y_bar - a1 * x_bar
    return a0, a1


def non_linear_fit(points, g, h, recover):
    transformed = [(g(x, y), h(x, y)) for x, y in points]
    a0, a1 = fit_line(transformed)
    return recover(a0, a1)


X = lambda x, y: x
Y = lambda x, y: math.log(y)
if __name__ == "__main__":
    result = non_linear_fit(points, X, Y, lambda a0, a1: (math.exp(a0), a1))
    print(result)