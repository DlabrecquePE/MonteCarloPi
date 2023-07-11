#Libraries
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib

#initialize
actual=3.141592653589793238462643383279
batchsize = 255

inside = 0
outside = 0
plot_sample = 0

plt.figure(figsize=(8,8))
plt.axis([-1.1,1.1,-1.1,1.1])
plt.title("Pi by Monte Carlo Method")

while True:

    #generate data
    sample=np.array([np.random.uniform(-1,1, size = batchsize),np.random.uniform(-1,1, size = batchsize)])
    magnitudes=[]
    for elem in range(batchsize):
        magnitudes.append(np.sqrt((sample[0,elem]**2)+(sample[1,elem]**2)))

    #calculate and plot
    for x in range(batchsize):
        if magnitudes[x] > 1:
            outside+=1
            plt.scatter(sample[0,x],sample[1,x],color='blue')
        else:
            inside+=1
            plt.scatter(sample[0,x],sample[1,x],color='red')
        s=4*(inside)/(inside+outside)
        d=np.abs(s-actual)

    #manage output
    plot_sample+=batchsize
    output_string1='Pi is approximately '+str(s)
    output_string2='Off from the actual value by '+str(d)
    output_string3='Sample # '+str(plot_sample)
    out1=plt.text(-0.6,-1.25,output_string1)
    out2=plt.text(-0.6,-1.30,output_string2)
    out3=plt.text(-0.6,-1.35,output_string3)
    plt.show()
    out1.remove()
    out2.remove()
    out3.remove()
