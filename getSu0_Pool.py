import time
import numpy as np
import cantera as ct
#import multiprocessing as mp

def getSu(t, p, reactants, mech):
        gas = ct.Solution(mech)
        gas.TPX = t, p, reactants
    
        # Flame Object
        f = ct.FreeFlame(gas, width=0.03)
        f.transport_model = 'Multi'
        f.set_refine_criteria(ratio=3, slope=0.07,curve=0.14)
        f.energy_enabled = True
        f.radiation_enabled = True
        f.soret_enabled = True
        try:
            f.solve(loglevel=1, refine_grid=True, auto=False)
            return f.velocity[0] * 100
        except:
            return 'null'
        
start_time = time.time()

P0 = ct.one_atm
mech = 'gri30.cti'
reactants = 'C3H8: 0.8, O2: 5.0, N2: 18.8'
T = np.linspace(298, 750, 18, endpoint=True)
P = np.linspace(0.4*P0, 40*P0, 1.6*P0, endpoint=True)

if __name__ == '__main__':
    #pool = mp.Pool(processes = 3)
    #results = [pool.apply(getSu, args=(t, p, reactants, mech)) for t in T for p in P]
    results = [getSu(t, p, reactants, mech) for t in T for p in P]
    np.savetxt('S_650_phi08sd.csv', results, delimiter=',', fmt = '%s')
    print("--- %s seconds ---" % (time.time() - start_time))