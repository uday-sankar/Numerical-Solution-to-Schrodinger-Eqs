#Solutions of Quantum Harmonic Oscilator
import Schro_Declutter as EF
import numpy as np
import matplotlib.pyplot as plt
def Poten_H(x):
	V=m*(w*x)**2/2
	return V
h,m,w=1,1,1
EF.Constant_feeder(h,m,1,Poten_H)
X=np.linspace(-8,8,10**4)
E_eigen=EF.Eigen_Range_finder(X,0,5,2)
fig=plt.figure()
ax=plt.axes(xlabel='X',ylabel='Psi')
ax.set_title("Solutions of quantum harmonic oscilator")
EF.Plot_Eq(X,E_eigen,ax)
ax.plot(X,Poten_H(X))
plt.show()
