import math

g, c, m, t0, v0, h, tend = map(float, input().split())

def phi(t, v):
    return g - (c / m) * v

def analytical(t):
    return (g * m / c) * (1 - math.exp(-(c / m) * t))

t, v = t0, v0
print(f"{'t':>8} {'Euler v':>14} {'Analytical v':>14} {'|et|%':>10}")
print(f"{t:8.3f} {v:14.6f} {analytical(t):14.6f} {'-':>10}")
steps = round((tend - t0) / h)
for i in range(1, steps + 1):
    v += phi(t, v) * h
    t = t0 + i * h
    a = analytical(t)
    et = abs((a - v) / a) * 100
    print(f"{t:8.3f} {v:14.6f} {a:14.6f} {et:9.2f}%")
print(f"Terminal velocity = {g * m / c:.4f}")