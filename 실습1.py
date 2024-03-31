import math

def func(a,b,c):
    d = (b*b) - (4*a*c)

    if d<0:
        print("근이 존재하지 않습니다.\n")
    elif d==0:
        x=(-1*b)/(2*a)
        print(x,"\n 중근을 갖습니다.\n")
    else:
        x1=(-1*b+math.sqrt(d))/(2*a)
        x2=(-1*b-math.sqrt(d))/(2*a)
        print(x1,", ",x2)