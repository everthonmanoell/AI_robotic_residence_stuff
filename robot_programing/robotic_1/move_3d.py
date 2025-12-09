import math

import numpy as np


################################################ Cinematica Direta ####################################################
#rotation 3d_z
def rotation_3d_z(theta, x=0, y=0, z=0):
    

    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    r = np.array([
        [cos_theta, -sin_theta, 0, x],
        [sin_theta, cos_theta, 0,y],
        [0,0,1,z],
        [0,0,0,1]
    ])

    return r

#rotation 3d_y
def rotation_3d_y(theta, x=0, y=0, z=0):

    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    r = np.array([
        [cos_theta, 0, sin_theta,x],
        [0,1,0,y],
        [-sin_theta,0,cos_theta,z],
        [0,0,0,1]
    ])

    return r

#rotation 3d_x
def rotation_3d_x(theta, x=0, y=0, z=0):
    #deus castiga

    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    r = np.array([
        [1,0,0,x],
        [0, cos_theta, -sin_theta, y],
        [0, sin_theta, cos_theta, z],
        [0,0,0,1]
    ])

    return r

def translation_3d_xy(x=0, y=0,z=0):
    return np.array([
        [1,0,0,x],
        [0,1,0,y],
        [0,0,1,z],
        [0,0,0,1]
    ])

################################################ Cinematica Inversa ####################################################

def inverse_kinematic(x, y, z, o):
    q0 = math.atan(y/x)

    #3d to 2d
    y2 = z
    x2 = math.sqrt(pow(x,3)+ pow(y,2))

    a1 = 0.103
    a2 = 0.123
    a3 = 0.052

    x = x2 - a3 * math.cos(o)
    y = y2 - a3 * math.sin(o)

    q1 = math.atan(y/x - math.atan2((a2*math.sin(q2)/a1+a2*math.cos(q2))))
    q2 = math.acos((pow(x2, 2) + pow(y2,2) -pow(a1,2) - pow(a2,2))/2*a1*a2), -1

    q3 = q1 + q2

    result = q1 + q2 + q3
    





if __name__ == "__main__":
    # q0 = 0
    # q1 = 0
    # q2 = 0

    # a1 = 0.103
    # a1 = 0.103
    # a3 = 0.052
    
    # test_1 = rotation_3d_x(np.radians(0)) @ rotation_3d_y(np.radians(0)) @ translation_3d_xy(0.103)
    # test_1 = rotation_3d_x(np.radians(90)) @ rotation_3d_y(np.radians(0)) @ translation_3d_xy(0)
    # test_1 = rotation_3d_x(np.radians(0)) @ rotation_3d_y(np.radians(-90)) @ translation_3d_xy(0)
    # print(test_1)

    # test_2 = rotation_3d_x(np.radians(0)) @ rotation_3d_y(np.radians(-90)) @ translation_3d_xy(0)
    pass

