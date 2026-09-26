import math

points=[(1, 0.6), (2, 2.4), (3, 3.5), (4, 4.8), (5, 5.7)]


def least_square(points):

    sx=0
    sy=0
    sxy=0
    sx2=0

    for i in points:
        sx=sx+i[0]
        sy=sy+i[1]
        sx2=sx2+(i[0]**2)
        sxy=sxy+(i[0]*i[1])

    m=len(points)
    d=(m*sx2)-(sx**2)
    a1=((m*sxy)-(sx*sy))/d
    x_bar=sx/m
    y_bar=sy/m

    a0=y_bar-(a1*x_bar)
    st=0
    s=0
    for i in points:
        st=st+((i[1]-y_bar))**2
        s=((i[1]-a0-(a1*i[0]))**2)+s
    cc=math.sqrt((st-s)/st)

    return a0,a1,cc

if __name__ == "__main__":
    print(least_square(points))