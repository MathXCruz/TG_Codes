'''  This code does the curvefit using Su, T and P from Vary_phi_T_P.py to find
 the best fit for alpha and beta.'''

import numpy as np
from scipy.optimize import curve_fit
from pandas_ods_reader import read_ods

#   gri30
#phi = 0.8
#Su0 = 36.767362383578615
#phi = 1.0
#Su0 = 48.626234213297934
#phi = 1.2
#Su0 = 47.82541105952791


#   San Diego 2016
#phi = 0.8
#Su0 = 32.037321061768644
#phi = 1.0
#Su0 = 39.608894383201296
#phi = 1.2
#Su0 = 34.356141394893285


#   Blanquart
#phi = 0.8
Su0 = 30.31972568176305
#phi = 1.0
#Su0 = 41.21565286360448
#phi = 1.2
#Su0 = 40.262340689561526

T0 = 298
P0 = 1
alpha = 1
beta = 1
cont = 0
i = 0
j = 0

def func(X, alpha, beta):
    T, P = X
    return Su0 * (T/T0)**alpha * (P/P0)**beta

T = read_ods('Results/Temperatura650.ods', 1, headers = False)
T = T.to_numpy()
if np.shape(T)[0] > 1:
    T = T.flatten()

P = read_ods('Results/Pressao650.ods', 1, headers = False)
P = P.to_numpy().astype(float)
if np.shape(P)[0] > 1:
    P = P.flatten()

Su = read_ods('Results/S_650_phi10sd.ods', 1, headers = False)
Su = Su.to_numpy()
if np.shape(Su)[0] > 1:
    Su = Su.flatten()

if len(Su) != len(T):
    Su = Su.reshape(len(T),-1)

while i < len(Su):
    if Su[i] == 'null':
        Su = np.delete(Su, i)
        T = np.delete(T, i)
        P = np.delete(P, i)
        i -= 1
    i += 1

Su = Su.astype(float)
        
r = curve_fit(func, (T,P), Su)

a = r[0]

z = func((T,P), a[0], a[1])

while j < len(Su): 
    if abs(z[j]-Su[j])/Su[j] <= 0.05:
        cont += 1
    j +=1

a0 = str(a[0])
a1 = str(a[1])
perc = cont/len(Su)
perc = str(perc*100)
print('Alpha = ' +a0+ '\nBeta = ' + a1+'\n')
print('Percentual em mais ou menos 5%: '+perc+ '%')  