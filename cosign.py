import numpy as np
alist =[1,2,3,4,5,6]
b = alist[-1]


NUMB_IMAGES = 5011  #numb images in VOC2007
def CosAnneal(high_lr, low_lr, numb_images = NUMB_IMAGES, batch_size = 64):
    cur_itr =0
    max_iter = numb_images // batch_size

    #cosign varies between 1 and -1 (sweep of 2), factor to scale between lowlr and high_lr
    scale = 2/(high_lr-low_lr)

    # then translate so ranges between lowlr and high_lr
    vals = (np.cos(np.linspace(0, np.pi, max_iter))/scale) + (high_lr-low_lr)/2 + low_lr
    while(True):
        yield vals[cur_itr]
        cur_itr+=1
        cur_itr%=max_iter


NUMB_SAMPLES = 600

#get repeating cosigns
ca = CosAnneal(.003, .001)
amplitude= ([next(ca) for x in range(NUMB_SAMPLES)])
time = list(range(NUMB_SAMPLES))


import matplotlib.pyplot as plot


# Amplitude of the cosine wave is cosine of a variable like time
# Plot a cosine wave using time and amplitude obtained for the cosine wave

plot.plot(time, amplitude)

# Give a title for the cosine wave plot
plot.title('Cosine wave')

# Give x axis label for the cosine wave plot
plot.xlabel('Time')

# Give y axis label for the cosine wave plot
plot.ylabel('Amplitude = cosine(time)')

# Draw the grid for the graph
plot.grid(True, which='both')
plot.axhline(y=0, color='b')

# Display the cosine wave plot
plot.show()