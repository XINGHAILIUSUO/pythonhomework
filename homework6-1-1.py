import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

plt.figure(figsize=(6,6))

x = np.linspace(-5,5,1000)
X = np.array([0., 1., 2., 3., -1.,-2.,-3.])
Y = np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])
#需要拟合函数的误差
def f(p,x,y):
    a,b,c = p
    return((a*x**2+b*x+c)-y)

test = leastsq(f,[0,0,0],args=(X,Y))
a,b,c=test[0]
y=a*x**2+b*x+c
print("a=",a,"b=",b,"c=",c)
plt.scatter(X,Y,color="red",label="Sample Point",linewidth=3)
ax = plt.gca()
ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小
plt.plot(x, y, color='b',linewidth=2,markersize=20, label=u'fitted curve')
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')
plt.xlabel(u'x')
plt.ylabel(u'y')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')
plt.savefig("D://6-1-1.jpg")
plt.show()
