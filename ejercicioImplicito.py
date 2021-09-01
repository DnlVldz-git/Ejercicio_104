import math
import numpy as np

def  y(n, y0, dt):
    if(n == 0):
        return y0
    else:
        return (y(n-1, y0, dt)+dt*(y(n-1,y0,dt))**2)
    
def yFor(N):    
    y0=-10.0
    dt = 1/N
    y_ = np.array([y0 for _ in range(N+1)])

    for i in range(N):
        y_[i+1] = y_[i]+dt*(y_[i])**2
    return y_[N]

def zFor(N):    
    z0=-10.0
    dt = 1/N
    z_ = np.array([z0 for _ in range(N+1)])

    for i in range(N):
        z_[i+1] = 1/(2*dt)*(1-np.sqrt(1-4*dt*z_[i]))
    return z_[N]

def exacta(t):
    return -10/(1+10*t)

def exacta2():
    r0 = 1/2
    a = 1
    t = 1
    R = 1
    return (r0)/(r0+math.e**(-a*t)*(R-r0))

def ynLog(N):
    y0 = 1/2
    dt = 1/N
    R = 1
    a = 1
    y_ = np.array([y0 for _ in range(N+1)])
    for i in range(N):
        y_[i+1] = a*y_[i]*(1-(y_[i]/R))*dt+y_[i]
    return y_[N]

def znLog(N):
    z0 = 1/2
    dt = 1/N
    z_ = np.array([z0 for _ in range(N+1)])
    for i in range(N):
        z_[i+1] = ((-1*(1-dt)+math.sqrt(((1-dt)**2-4*(dt)*(-z_[i]))))/(2*dt))
    return z_[N]

def errorAbs1(num):
    return abs(exacta2()-ynLog(num))

def errorAbs2(num):
    return abs(exacta2()-znLog(num))

print("-----------------------")
num = 10
for i in range(100):
    if(i==0):  
        print("N-------Yn---------Eyn/dt-----------Zn-------------Ezn/dt")
        print(f"{1:<5}{ynLog(1):<15.5f}{errorAbs1(1):<15.5f}{znLog(1):<15.5f}{errorAbs2(1):<15.5f}")
    else:
        print(f"{num:<5}{ynLog(num):<15.5f}{errorAbs1(num):<15.5f}{znLog(num):<15.5f}{errorAbs2(num):<15.5f}")
        num += 10
    
