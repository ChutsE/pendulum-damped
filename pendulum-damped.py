import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
import time

#preliminar stage
theta = math.pi/2
angular = 0
t_prev = time.time()

def pendulum():
    fig = plt.figure()
    ax = fig.gca()

    g = 9.81
    R = 2
    m = 1
    k = 80
    
    def animate(step):
        global theta, angular, t_prev
        ax.clear()
        plt.xlim(-R, R)
        plt.ylim(-(R + 1), 0)

        t = time.time()
        t_diff = t - t_prev
        alpha = (math.sin(theta)*(k/m - angular**2))/(-math.cos(theta) + (k*R)/(g*m))
        angular = alpha*t_diff + angular
        theta = angular*t_diff + theta
        t_prev = t

        x_ = g*math.sin(theta)/alpha**2 - R
        x = (angular**2 *R - g*(math.cos(theta))) / (k/m - angular**2)
        print(x_, x)

        x1 = (R+x)*math.sin(theta)
        y1 = (R+x)*math.cos(theta)
        x2 = R*math.sin(theta)
        y2 = R*math.cos(theta)
        X = [0, x1]
        Y = [0, y1]
        plt.plot(X, Y)
        plt.plot(x1, y1, 'bo', markersize = 10)
        plt.plot(x2, y2, 'ro')


        
    steps = np.arange(500)
    anim = animation.FuncAnimation(fig, animate, frames = steps, interval = 1)
    writergif = animation.PillowWriter(fps=30)
    anim.save('animation_pendulum_damped.gif',writer=writergif)
    
    
pendulum()

#def damper(coordinates = {"begin":[0,0], "end":[2,2]}, coils = 10):
    
