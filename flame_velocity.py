'''  This code is used to calculate the velocity and temperature in the domain.
Su0 [m/s] can be called in the console after execution by the command f.velocity[0].'''

import time
import cantera as ct
import matplotlib.pyplot as plt

# Simulation Parameters
T0 = 298.0
P0 = ct.one_atm*0.4
fuel = input("Enter fuel type: ")

if fuel == 'Etanol':
    reactants = 'c2h5oh:1.0, O2:3.0, N2:11.28'
    gas = ct.Solution('ethanol_mech.cti')
elif fuel == 'Metano':
    reactants = 'CH4:1.0, O2:2.0, N2:7.52'
    gas = ct.Solution('gri30.cti')
elif fuel == 'Propano':
    reactants = 'C3H8:0.8, O2:5.0, N2:18.8'
    gas = ct.Solution('gri30.cti')
#timer
start_time = time.time()

gas.TPX = T0, P0, reactants

# Flame Object
f = ct.FreeFlame(gas, width=0.03)
f.transport_model = 'Multi'
f.set_refine_criteria(ratio=3, slope=0.07,curve=0.14)
f.energy_enabled = True
f.radiation_enabled = True
f.soret_enabled = True


f.solve(loglevel=1, refine_grid=True, auto=False)

print(f.velocity[0]*100)
'''
plt.figure(figsize = (12,8))
plt.subplot(3,1,1)
plt.plot(f.grid, f.T)
plt.ylabel('Flame Temperature [K]')
plt.title('Temperature & Velocity of the flame in axial direction: '+reactants)
plt.subplot(3,1,2)
plt.plot(f.grid, f.velocity*100)
plt.ylabel('Flame Velocity [cm/sec]')
plt.xlabel('Width of the Flame [m]')'''


#   Uncomment this part if you want to plot the molar fractions (scales may need calibration)

'''
plt.figure(figsize = (12,8))
plt.subplot(4,1,1)
plt.plot(f.grid,f.X[13,:]*10, color='tab:red')
plt.plot(f.grid,f.X[15,:]*10, color='tab:blue')
plt.plot(f.grid,f.X[14,:]*10, color='tab:orange')
plt.legend(['CH4 x10', 'CO2 x10', 'CO x10'])
plt.ylabel('Molar Fraction (X)')
plt.subplot(4,1,2)
plt.plot(f.grid,f.X[12,:]*1000, color='tab:green')
plt.plot(f.grid,f.X[17,:]*1000, color='tab:purple')
plt.plot(f.grid,f.X[16,:]*10000, color='tab:brown')
plt.legend(['CH3 x1000', 'CH2O x1000','HCO x10⁵'])
plt.ylabel('Molar Fraction (X)')
plt.subplot(4,1,3)
plt.plot(f.grid,f.X[7,:]*100000, color='tab:pink')
plt.plot(f.grid,f.X[5,:]*10, color='tab:gray')
plt.plot(f.grid,f.X[6,:]*10000, color='tab:olive')
plt.plot(f.grid,f.X[4,:]*100, color='tab:cyan')
plt.legend(['H2O2 x10⁵', 'H2O x10', 'HO2 x10⁴', 'OH x100'])
plt.ylabel('Molar Fraction (X)')
plt.subplot(4,1,4)
plt.plot(f.grid,f.X[9,:]*1000000, color='k')
plt.plot(f.grid,f.X[2,:]*1000, color='m')
plt.plot(f.grid,f.X[35,:]*10000, color='darkslateblue')
#plt.plot(f.grid,f.X[13,:], color='purple')
plt.legend(['CH x10⁶', 'O x1000', 'NO x10⁵'], loc=0)
plt.ylabel('Molar Fraction (X)')
plt.xlabel('Width of the Flame [m]')
'''


plt.show()
print("--- %s seconds ---" % (time.time() - start_time))