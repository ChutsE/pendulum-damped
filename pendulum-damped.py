import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
import time

def pendulum(Xs = [0.5, 9.5], Ys = [0, 0.01], frames = 150, num_linspace = 10000):
    fig = plt.figure()
    ax = fig.gca()
    xs = np.linspace(Xs[0], Xs[1], frames)
    ys = np.linspace(Ys[0], Ys[1], frames)

    g = 9.81
    R = 2
    m = 1
    k = 10

    theta = 0
    angular = 0
    t = time.time()
    alpha = (math.sin(theta)*(k/m - angular**2))/(math.cos(theta) + (k*R)/(g*m) -1)
    angular = alpha*(time.time() - t) - angular
    theta = angular*(time.time() - t) - theta
    
    x = g*math.sin(theta)/alpha - R
    
    def frame(t):
        ax.clear()
        plt.xlim(-.5, 10)
        plt.ylim(-5, 1)

        x = np.linspace(0, xs[t], num_linspace)
        y = catenaria(x, B = [xs[t], ys[t]], L = 10)
        
        plt.plot(x,y)
        
    T = np.arange(frames)
    anim = animation.FuncAnimation(fig, frame, T)
    writergif = animation.PillowWriter(fps=30)
    anim.save('animation_chain.gif',writer=writergif)

    plt.show()


#def damper(coordinates = {"begin":[0,0], "end":[2,2]}, coils = 10):
    