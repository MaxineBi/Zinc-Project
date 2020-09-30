import numpy as np
import matplotlib.pyplot as plt

#create an array from a file with your molecular weights only... /1000 so it's in kDa
with open('MWXRAYfinaloutput.txt') as f:
    MWlist = [ float(i)/1000 for i in f]
MWarray = np.array(MWlist)

#use the array to make a histogram frequency plot. change the bins and range depending on what makes sense
plt.hist(MWarray, bins = 15,  range=[0, 280])

plt.gca().set(title= 'X-RAY', ylabel = 'Number of X-Ray Structures', xlabel = 'Structure molecular Mass (kDa)')

plt.show()
