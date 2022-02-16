import numpy as np
import matplotlib.pyplot as plt

def gen_data():
    selected = np.zeros(TOTAL)
    count = 0
    times = 0
    while True:
        times += 1
        egg_get = int(np.random.rand()*TOTAL%TOTAL)
        
        # get a new kind of egg
        if selected[egg_get] == 0: 
            selected[egg_get] = 1
            count += 1
        
        if count==TOTAL: 
            break
    return times

def main():
    # generate data
    data = []
    for _ in range(TIMES):
        data.append(gen_data())
    
    # draw figure 1
    f1 = plt.figure(1)
    HIST_BINS = np.linspace(np.min(data), np.max(data), BINS) #(start, stop, number of parts)
    mean = np.mean(data)
    african =  sum(i < mean for i in data)
    european = sum(i >= mean for i in data)
    plt.hist(data, HIST_BINS, facecolor='grey')
    plt.title("average="+str(mean)+" European="+str(european)+" African="+str(african))
    
    # draw figure 2
    f2 = plt.figure(2)
    count, bins_count = np.histogram(data, bins=BINS)
    cdf = np.cumsum(count)
    plt.plot(bins_count[1:], cdf, label="CDF")
    plt.grid()
    plt.show()


# parameters
np.random.seed(19680801)
TIMES = 10000
BINS = 100 # number of parts
TOTAL = 60

if __name__=="__main__":
    main()