import numpy as np
import matplotlib.pyplot as plt
import Support_functions_Morse as EF
import math
def Morse_V(r):
	V=D_e*(1-2.718**(-a*(r-r_e)))**2
	return V

m,h=1,1
t='t'
Xmin=.5
Xmax=5
D_e=10
a=.8
r_e=1
X=np.linspace(Xmin,Xmax,10**3)
for p in range(len(X)):
	if Morse_V(X[p])<D_e:
		Xmin=X[p]-1
		Pos=p
		break
X=np.linspace(Xmin,Xmax,10**4)
EF.Constant_feeder(h,m,D_e,Morse_V)


Eigen_E=EF.Eigen_Range_finder(X,0,D_e*.9,10,.1)
fig=plt.figure()
ax=plt.axes(xlabel="r",ylabel="Psi",ylim=(0,Eigen_E[-1]*1.1))
X=np.linspace(Xmin,Xmax,10**5)
EF.Plot_Eq(X,Eigen_E,ax)
ax.plot(X,Morse_V(X))
plt.legend()
plt.show()
