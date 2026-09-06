import numpy as np

points = [(0, 1), (1, 3), (2, 7), (3, 13)]

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

print(polynomial_fit(points))
