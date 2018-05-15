import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import leastsq
def get_data(file_name):
    data = pd.read_csv(file_name)
    time = []
    p_l_price = []
    p_a_price = []
    u_l_price = []
    u_a_price = []
    for x, y1, y2, y3, y4 in zip(data['time'], data['p_l_price'], data['p_a_price'],
                              data['u_l_price'],data['u_a_price']):
        time.append([float(x)])
        p_l_price.append(float(y1))
        p_a_price.append([float(y2)])
        u_l_price.append(float(y3))
        u_a_price.append(float(y4))
    return time,p_l_price,p_a_price,u_l_price,u_a_price
x,y1,y2,y3,y4 = get_data('homeworkdata.csv')

#曲线拟合部分 拟合模型为二次函数
xz = np.linspace(61,72,1000)
X=np.array([float(z) for z in np.array(x[0:6])])
Y1=np.array([float(z) for z in np.array(y1[0:6])])
Y2=np.array([float(z) for z in np.array(y2[0:6])])
#需要拟合函数的误差
def f(p,x,y):
    a,b,c = p
    return((a*x**2+b*x+c)-y)

test1 = leastsq(f,[0,0,0],args=(X,Y1))
a1,b1,c1=test1[0]

yz1=a1*xz**2+b1*xz+c1
test2 = leastsq(f,[0,0,0],args=(X,Y2))
a2,b2,c2=test2[0]
yz2=a2*xz**2+b2*xz+c2
print("a1=",a1,"b1=",b1,"c1=",c1)
print("a2=",a2,"b2=",b2,"c2=",c2)

#预测
#个人最低成交价
yuce1=a1*70*70+b1*70+c1
print("2018年5月26日个人最低成交价预测为:",yuce1)
#个人平均成交价
yuce2=a2*70*70+b2*70+c2
print("2018年5月26日个人平均成交价预测为:",yuce2)


#画图
plt.figure(figsize=(8,4))
plt.plot(x,y1,label="$Personal minimum price$",color="red",linewidth=1)
plt.plot(x,y2,label="$Personal average price$",color="blue",linewidth=1)
plt.plot(x,y3,label="$Unit minimum price$",color="yellow",linewidth=1)
plt.plot(x,y4,label="$Unit average price$",color="green",linewidth=1)

#plt.plot(xz,yz1,label="$quxian1$",color="black",linewidth=1)
#plt.plot(xz,yz2,label="$quxian2$",color="black",linewidth=1)

plt.xlabel("Time")
plt.ylabel("price")
plt.title("License plate price")
plt.legend()
plt.show()