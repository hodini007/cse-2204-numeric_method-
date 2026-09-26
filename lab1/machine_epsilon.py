import math
import numpy as np

e, cnt = 1.0, 0
while 1.0 + e / 2.0 > 1.0:
    e /= 2.0
    cnt += 1
print(f"double: eps = {e:.6e} = 2^-{cnt}")

ef, cf = np.float32(1.0), 0
while np.float32(1.0) + ef / np.float32(2.0) > np.float32(1.0):
    ef = ef / np.float32(2.0)
    cf += 1
print(f"float : eps = {float(ef):.6e} = 2^-{cf}")

print("1.0 + 1e-20 == 1.0 :", (1.0 + 1e-20) == 1.0)

for x in (1e-4, 1e-8):
    direct = (1 - math.cos(x)) / x**2
    stable = 2 * math.sin(x / 2) ** 2 / x**2
    print(f"x = {x:g}: direct = {direct:.10f}, stable = {stable:.10f}")