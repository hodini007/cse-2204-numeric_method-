import math
import numpy as np 



points=[(0, 0, 2), (1, 1, 4), (2, 3, 3), (4, 2, 16), (6, 8, 8)]




def least_square(points):

    xsum=0
    ysum=0
    zsum=0
    yzsum=0
    zxsum=0
    xxsum=0
    yysum=0
    xysum=0

    for i in points:
        xsum=xsum+i[0]
        ysum=ysum+i[1]
        zsum=zsum+i[2]
        yzsum=yzsum+(i[1]*i[2])
        zxsum=zxsum+(i[2]*i[0])
        xxsum=xxsum+(i[0]**2)
        yysum=yysum+(i[1]**2)
        xysum=xysum+(i[0]*i[1])

    #using numpy to solve thwe linear equations
    A = np.array([[len(points), xsum, ysum], [xsum, xxsum, xysum], [ysum, xysum, yysum]])
    B = np.array([zsum, zxsum, yzsum])
    a0, a1, a2 = np.linalg.solve(A, B)

    return a0, a1, a2

if __name__ == "__main__":
    print(least_square(points))