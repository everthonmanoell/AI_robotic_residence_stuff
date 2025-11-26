import math

import numpy as np


# contruir a matrix de transformação quando tem apenas uma translação em 2d
def SE2_xy(x,y):
    theta = 0
    

    t = np.array([
        [1, 0, x],
        [0, 1, y],
        [0, 0, 1]   
    ])

    return t

print(SE2_xy(2,4))
    



# A função que representa unicamente uma única rotação em 2d
def SE2_theta(theta):
    x = 0
    y = 0

    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    r = np.array([
        [cos_theta, -sin_theta, x],
        [sin_theta, cos_theta, y],
        [0,0,1]
    ])

    return r

attempt1 = np.radians(90)
attempt2 = np.radians(-90)

print(SE2_theta(attempt1))
print(SE2_theta(attempt2))

def resolution1():
    x1 = SE2_xy(1, 0.25)
    x2 = np.array([
        [0.5],
        [0.5],
        [1],
    ])

    return np.matmul(x1, x2)

print(resolution1())


def resolution2():
    x1 = SE2_xy(1, 0.25)
    x1_inverse = np.linalg.inv(x1)
    
    x2 = np.array([
        [0.5],
        [0.5],
        [1],
    ])

    result = np.matmul(x1_inverse, x2)

    return result

print(f'Resolution2: \n{resolution2()}')

def resolution3():
    x1 = SE2_xy(1, 0.25)
    x2 = np.array([
        [0.5],
        [0.5],
        [1],
    ])

    translation = np.matmul(x1, x2)
    
    rotation = SE2_theta(np.radians(45))

    result = np.matmul(translation, rotation)

    return result

print(f'Resolution3: \n{resolution3}')






