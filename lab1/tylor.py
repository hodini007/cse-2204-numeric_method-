import math

data = input().split()
n = int(data[0])
d = list(map(float, data[1:n + 2]))
h, true = float(data[n + 2]), float(data[n + 3])

approx, hp = 0.0, 1.0
print(f"{'order':>6} {'term':>14} {'estimate':>14} {'Et':>14} {'et%':>12}")
for k in range(n + 1):
    term = d[k] / math.factorial(k) * hp
    approx += term
    hp *= h
    et = true - approx
    print(f"{k:6d} {term:14.6f} {approx:14.6f} {et:14.6f} {abs(et / true) * 100:11.4f}%")
print(f"f(xi+h) ~ {approx:.6f}")