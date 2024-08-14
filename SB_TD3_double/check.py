import numpy as np
y=np.load('Sch.npz')['array1']
print(y)
while(True):
    x=np.load('Sch.npz')['array1']
    if(y!=x):
    	y=x
    	print(x)
