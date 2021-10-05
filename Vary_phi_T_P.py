'''  This code is used to calculate Su varying T and P, using the mechanism on
 line 23.'''

import time
import numpy as np
import cantera as ct

#timer
start_time = time.time()

# Simulation Parameters
P0 = ct.one_atm
solution = 'sandiego16.cti'

Temp= []
Press = []
T = np.arange(298, 750, 18)
P = np.arange(0.4*P0, 40*P0, 1.6*P0)
S = []
reactants = 'C3H8: 1.0, O2:5.0, N2: 18.8'

for t in T:   
    for p in P:
#   Ideal Gas and mixture object used to calculate mixture properties

        gas = ct.Solution(solution)
        gas.TPX = t, p, reactants
    
        # Flame Object
        f = ct.FreeFlame(gas, width=0.03)
        f.transport_model = 'Multi'
        f.set_refine_criteria(ratio=3, slope=0.07,curve=0.14)
        f.energy_enabled = True
        f.radiation_enabled = True
        f.soret_enabled = True

#   If Temp and Press are already on a file, you can comment lines 54, 55, 58 and 59
        try:
            f.solve(loglevel=1, refine_grid=True, auto=False)
        
            #Temp.append(t)
            #Press.append(p/ct.one_atm)
            S.append(f.velocity[0]*100)
        except:
            #Temp.append(t)
            #Press.append(p/ct.one_atm)
            S.append('null')
#   Convertion to array type and conversion to matrix           
S = np.asarray(S)

#   Save S to .csv file and print execution time 
np.savetxt('S_650_phi10sd.csv', S, delimiter=',', fmt = '%s')
#np.savetxt('Temperatura.csv', Temp, delimiter=',', fmt = '%s')
#np.savetxt('Pressao.csv', Press, delimiter=',', fmt = '%s')
print("--- %s seconds ---" % (time.time() - start_time))