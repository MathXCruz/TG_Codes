'''   This code is meant to compare the mechanism input on line 27 with an experimental
 result graph (line 18). The range of phi can be changed on line 20 and the graph
 limits must be set equal to the experimental one on lines 49 and 50.'''

import time
import cantera as ct
import matplotlib.pyplot as plt
import numpy as np

start_time = time.time()
# Simulation Parameters
Tin = 300.0
P = ct.one_atm
Temp= []
A = []
St = []

img = plt.imread("C3H8_sitegri30.jpg")

a = np.arange(0.6, 1.5, 0.01)
for c in a:
    b = str(c)
    reactants = 'C3H8:' +b+ ', O2:5.0, N2: 18.8'

# Ideal Gas and mixture object used to calculate mixture properties

    gas = ct.Solution('Blanquart2018.cti')
    gas.TPX = Tin, P, reactants

# Flame Object
    f = ct.FreeFlame(gas, width=0.03)
    f.transport_model = 'Multi'
    f.set_refine_criteria(ratio=3, slope=0.07,curve=0.14)
    f.energy_enabled = True
    f.radiation_enabled = True
    f.soret_enabled = True


    f.solve(loglevel=1, refine_grid=True, auto=False)
    Temp.append(f.T[-1])
    St.append(f.velocity[0])
    A.append(c)
    
fig, ax = plt.subplots()
color = 'tab:orange'
ax.set_xlabel('phi')
ax.set_ylabel('S_u [cm/s]', color=color)
plt.title('Laminar Burning Speed: Propano + Air')
plt.xlim(0.6, 1.5)
plt.ylim(0, .60)
ax.plot(A, St, color=color)
ax.tick_params(axis='y', labelcolor=color)
ax.imshow(img, extent=[0.6, 1.5, 0, .60])
    
#plt.show()
print("--- %s seconds ---" % (time.time() - start_time))