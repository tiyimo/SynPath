# TM 9th July 2021
# From Ciaburro - Simulation Modelling with Python

import numpy as np
import matplotlib.pyplot as plt

# Define the function
x = np.linspace
y = x**2-2*x+1

# Draw and display graph
fig = plt.figure
axdef = fig.add_subplot (1,1,1)
axdef.spines['left'].set_position('center')
axdef.spines['bottom'].set_position('zero')
axdef.spines['right'].set_color('none')
axdef.spines['top'].set_color('none')
axdef.xaxis.set_tricks_position('bottom')
axdef.yaxis.set_tricks_position('left')
plt.plot(x,y, 'r')
plt.show()

# Define the gradient function
Gradf = lambda x: 2*x-2

# Initialise variables
actual_X = 3 
learning_rate = 0.01
precision_value = 0.000001
previous_step_size = 1
max_iteration = 100000
iteration_counter = 0

# Iteration procedure
while previous_step_size > precision_value and iteration_counter < max_iteration :
    PreviousX = actual_X
    actual_X = actual_X - learning_rate * Gradf(PreviousX)
    previous_step_size = abs(actual_X - PreviousX)
    iteration_counter = iteration_counter +1
    print('Number of iterations = ',iteration_counter ,'\
        nActual value of x is ', actual_X)
    print('X value of f(x) minimum =', actual_X)

print('X value of f(x) minimum = ', actual_X)


# TM 9th July 2021
# Geron - Hands on Machine Learning

import numpy as np

n_epochs = 50
t0, t1 = 5, 50 #learning schedule hyperparameters

def learning_schedule(t)
    return t0 / (t + t1)

theta = np.random.randn(2,1) # random initialisation

for epoch in range(n_epochs)
    for i in range(m)
    random_index = np.random.randint
    xi = X_b[random_index:random_index+1]
    yi = y[random_index:random_index+1]
    gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
    eta = learning_schedule(epoch * m + i)
    theta = theta - eta * gradients


