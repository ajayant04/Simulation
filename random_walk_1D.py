import numpy as np
import matplotlib.pyplot as plt
import random

#Simple Random Walk, no barriers: Particle moves freely in a given time period n. P(X_i+1 | X_i) = P(X_i-1 | X_i) = 1/2.
def gen_srw(n):
    x,y = 0,0

    timepoints = np.arange(n+1)
    positions = [y]

    directions = [-1, 1]

    for i in range (1, n+1):

        step = random.choice(directions)
        y += step
        positions.append(y)

    return timepoints, positions


#Random walk with barriers: Particle must remain within L <= x <= N. 0 < P(X_i+1 | X_i) = p < 1
def bar_rw(N, L, p, k, tmax):
    x,y = 0,k 

    timepoints = [x]
    positions = [y]

    directions = [-1, 1]

    exp = expected(N - L, k - L, p)

    print ("Collision expected at t = " + str(exp))

    while y < N and y > L and x < tmax:   
        x += 1
        rand = random.random()
        if (p <= rand):
            y += directions[0]
        else:
            y += directions[1]
        timepoints.append(x)
        positions.append(y)

    maxcount = len(timepoints)



    if (y == N): 
        print ("Upper boundary was reached at move " + str(maxcount-1))
    elif (y == L):
        print ("Lower boundary was reached at move " + str(maxcount-1))
    else:
        print ("Time limit exceeded :(")

    return timepoints, positions



def expected(N, k, p):
    rh = (1.0-p)/p 
    if (rh == 1):
        return k * (N-k)
    else:
        return 1 / (1.0-2*p) * (k - N * ((1-rh**k)/(1-rh**N)))


rw1 = bar_rw(50, -50, 0.5, 0, 1000)

plt.plot(rw1[0], rw1[1], 'r-', label = "Random Walk")


"""
srw1 = gen_srw(100)
srw2 = gen_srw(100)
srw3 = gen_srw(100)

plt.plot(srw1[0], srw1[1], 'r-', label="srw1")
plt.plot(srw2[0], srw2[1], 'g-', label="srw2")
plt.plot(srw3[0], srw3[1], 'b-', label="srw3") 
"""

plt.show()
