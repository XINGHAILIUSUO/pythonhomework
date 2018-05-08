import numpy as np
print("请输入a:")
a=float(input())
print("请输入b:")
b=float(input())
print("请输入误差e:")
e=float(input())
k=0
def f(x):
    #return (2*np.sin(np.pi*x)+np.cos(np.pi*x))
    return (x**2-1)
while True:
    if f(a)*f(b)>0:
        print("请输入a:")
        a = float(input())
        print("请输入b:")
        b = float(input())
        print("请输入误差e:")
        e = float(input())
        k = 0
    elif f(a)*f(b)==0:
        if f(a)==0:
            print("x0=",a,"k=",k)
        else:
            print("x0=",b,"k=",k)
        break
    else:
        m=(a+b)/2
        if abs(b-a)<=e:                                     #(b-a>=0 and b-a<=e)or(a-b>=0 and a-b<=e):
            print("x0=:",m,"k=",k)
            break
        else:
            if f(a)*f(m)<0:
                b=m
            else:
                a=m
            k=k+1