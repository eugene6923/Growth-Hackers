from matplotlib import pyplot as plt
import numpy as np
from scipy import optimize as op
import pandas as pd

a=pd.read_csv("D:\\그로스해커스\\quest_tipping.csv",engine='python')

sex=a['SEX'].values
bill=a['TOTBILL'].values
tiprate=a['TIPRATE'].values

a['SEX'].replace(to_replace='Female',value=0,inplace=True)
a['SEX'].replace(to_replace='Male',value=1,inplace=True)

def f2(beta):
    sse=0
    tiprate=len(a['TIPRATE'])
    for i in range(tiprate):
        sse += (beta[0]-beta[1]*a['TIPRATE'][i]+beta[2]*a['SEX'][i]-a['TIPRATE'][i])**2
    return 1/(2*tiprate)*sse

beta_hat=op.minimize(f2,[2,2,2])['x']
print(beta_hat)

def d(x,y):
    return beta_hat[0]+beta_hat[1]+beta_hat[2]*y

xx = np.linspace(-10,10,501)
yy = np.linspace(-10,10,501)
X, Y=np.meshgrid(xx,yy)
Z=d(X,Y)

plt.figure(figsize=(12,8))
plt.subplot(221)
plt.scatter(a['SEX'],a['TIPRATE'])
plt.subplot(222)
plt.scatter(a['TOTBILL'],a['TIPRATE'])
plt.subplot(223)
plt.contour(xx,yy,Z)
plt.show