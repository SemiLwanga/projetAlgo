# -*- coding: utf-8 -*-
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import numpy as np
import math
import re

"""Ce code nous génère le graphique de 
l'équation du mouvement du système avec
oscillations libre. Donc F(t) = 0 """

def f(v,x):
    return (v[1],-2*v[1]-400*v[0])

x0 = [0.01,0]

absc = np.linspace(1,10,600)
vs = odeint(f,x0,absc)
ord =vs[:,0]

plt.plot(absc,ord,'-')
plt.plot(absc,ord,'r*')
plt.xlabel("axe-x")
plt.ylabel("axe-y")
plt.plot("Lorque F(t) = 0 ")
plt.show()

