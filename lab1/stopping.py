import math

x_s, n_s, nmax_s = input().split()
x, n, nmax = float(x_s), int(n_s), int(nmax_s)

es = 0.5 * 10 ** (2 - n)
true = math.exp(x)
total, term, ea, k = 0.0, 1.0, 100.0, 0

print(f"es = {es:.6f}%")
print(f"{'terms':>6} {'estimate':>16} {'et%':>12} {'ea%':>12}")
while True:
    total += term
    ea = abs(term / total) * 100
    k += 1
    et = abs((true - total) / true) * 100
    if k == 1:
        print(f"{k:6d} {total:16.8f} {et:12.6f} {'-':>12}")
    else:
        print(f"{k:6d} {total:16.8f} {et:12.6f} {ea:12.6f}")
    term = term * x / k
    if (k > 1 and ea < es) or k >= nmax:
        break

if ea >= es and k >= nmax:
    print(f"Warning: convergence not reached in {nmax} terms")
print(f"e^{x:.4f} = {total:.8f} after {k} terms (true {true:.8f})")