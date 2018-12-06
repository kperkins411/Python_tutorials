"""
Very simple backpropagation demo using 1 neuron and 1 error function

X * w1--,
         > (add) -- out1 --error
y * w2--'

out1 = (x*w1 + y*w2)
error = 1/2*(correct-out1)**2

"""
#inputs and expected output
x=2
y=3
correct = 6 #known as the 'ground truth'

#initial weights,
# (this is a non trivial decision, the frameworks, PyTorch, Tensorflow, etc,  provide options)
w1=0.2
w2=0.3

out1= (x*w1 + y*w2)             #neuron output
error = 1/2*(correct-out1)**2   #error function (want this to shrink to 0!)

dout1_dw1 = x  # constant derivative
dout1_dw2 = y  # constant derivative

#how much of dwerror_w to add to w
#another non trivial bit, .01, .001 .0001?  Use learning rate finding algorithm
#see  “Cyclical Learning Rates for Training Neural Networks”. by Leslie Smith for an intelligent solution
learning_rate = .01

#usually you train on batches of your data until you have trained on it all, this is called an epoch
#then you train for several more epochs until you get a low enough error
for i in range(10000):

    # forward pass
    out1 = (x * w1 + y * w2)
    error = 1 / 2 * (correct - out1) ** 2

    print(f"For pass {i}, w1 ={w1}, w2={w2}, error is{error}")

    # backward pass derivitives (dout1_dw1 dout1_dw2 defined above)
    derror_dout1 = -(correct - out1)

    # chain rule
    derror_dw1 = -derror_dout1 * dout1_dw1  # shows fastest increase, want decrease, reverse sign
    derror_dw2 = -derror_dout1 * dout1_dw2

    #adjust weights
    w1 = w1+learning_rate * derror_dw1;
    w2 = w2+learning_rate * derror_dw2;


