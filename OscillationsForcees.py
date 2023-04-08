# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np
import re
import math

"""Ce code nous génère le graphique de 
l'équation du mouvement du système avec
oscillations libre. Donc F(t) = 100cos(10t) """

def f(v,x):
    return (v[1],-2*v[1]-400*v[0]+10*np.cos(10*x))

x0 = [0.01,0]

absc = np.linspace(1,10,600)
vs = odeint(f,x0,absc)
ord =vs[:,0]

plt.plot(absc,ord,'-')
plt.plot(absc,ord,'b*')
plt.xlabel("axe-x")
plt.ylabel("axe-y")
plt.plot("Lorsque F(t) = Fo*Cos(wt) ")
plt.show()
