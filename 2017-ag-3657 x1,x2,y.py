import numpy as np
import statsmodels.api as sm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd


y = [5,7,15,17,9,11]
x.x1 = [0,0,10,10,20,20]
x.x2 = [0,0,100,100,400,400]
x = np.column_stack((X1,X2))
x = sm.add_constant(x, prepend=True)
res = sm.OLS(y,x).fit()
print res.params
print res.bse
print res.summary()

fig = plt.figure()
axis = fig.add_subplot(111, projection='3d')
axis.scatter(['x.x1'],['x.x2'],['Y'], c='r', marker='o')
xx, yy = np.meshgrid(['x.x1'],['x.x2'])
exog = pd.core.frame.DataFrame({'x.x1':xx.ravel(),'x.x2':yy.ravel()})
out = res.predict(exog=exog)
axis.plot_surface(xx, yy, out.values.reshape(xx.shape), rstride=1, cstride=1, alpha='0.2', color='None')
axis.set_xlabel("x.x1")
axis.set_ylabel("x.x2")
axis.set_zlabel("y")
plt.show()
