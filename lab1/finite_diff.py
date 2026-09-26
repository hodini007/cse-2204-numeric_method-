def f(x):
    return -0.1 * x**4 - 0.15 * x**3 - 0.5 * x**2 - 0.25 * x + 1.2

def fprime(x):
    return -0.4 * x**3 - 0.45 * x**2 - x - 0.25

def pct(true, est):
    return abs((true - est) / true) * 100

data = input().split()
x, q = float(data[0]), int(data[1])
hs = list(map(float, data[2:2 + q]))
true = fprime(x)

print(f"true f'({x:.4f}) = {true:.6f}")
print(f"{'h':>10} {'forward':>12} {'et%':>8} {'backward':>12} {'et%':>8} {'centered':>12} {'et%':>8}")
for h in hs:
    fwd = (f(x + h) - f(x)) / h
    bwd = (f(x) - f(x - h)) / h
    cen = (f(x + h) - f(x - h)) / (2 * h)
    print(f"{h:10.6f} {fwd:12.6f} {pct(true, fwd):7.2f}% {bwd:12.6f} {pct(true, bwd):7.2f}% {cen:12.6f} {pct(true, cen):7.2f}%")