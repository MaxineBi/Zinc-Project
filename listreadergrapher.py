import numpy as np
import matplotlib.pyplot as plt

with open('MWNMRfinaloutput.txt') as f:
    MWlist = [ float(i)/1000 for i in f]
MWarray = np.array(MWlist)


plt.hist(MWarray, bins = 15,  range=[0, 40])

plt.gca().set(title= 'NMR', ylabel = 'Number of NMR Structures', xlabel = 'Structure molecular Mass (kDa)')

plt.show()
