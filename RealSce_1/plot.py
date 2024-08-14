import matplotlib.pyplot as plt
import csv
import numpy as np




with open("Rewards_Thr_opt.csv",'r') as file:
	reader=csv.reader(file,delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
	reward1=list(reader)
reward1=np.array(reward1[0],dtype=float)
ep=[x for x in range(1,201)]
plt.plot(ep,reward1)
plt.show()
