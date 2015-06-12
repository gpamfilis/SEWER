__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import numpy as np


def pipe_diameter_calculation(n0, q0, s):
    numerator = (4**(5./3)*n0*q0)
    denominator = np.pi*s**(1/2.)
    return (numerator/denominator)**(3./8)


def flow_in_circular_pipe(n, d, s):
    return (np.pi/(4**(5./3)))*(1./n)*(d**(8./3))*(s**0.5)


def velocity_in_circular_pipe(q, d):
    return (4*q)/(np.pi*d**2)


def theta(y_d):
    theta = 2*np.arccos((1-(2*y_d)))
    return theta


def flow_ratio(h_d):
    angle_theta = theta(h_d)
    numerator = (angle_theta-np.sin(angle_theta))**1.62
    denominator = (angle_theta+np.sin(angle_theta/2))**0.62
    q_qf = (1./2*np.pi)*(numerator/denominator)
    return q_qf/10.


def velocity_ratio(h_d):
    angle_theta = theta(h_d)
    numerator = (angle_theta-np.sin(angle_theta))
    denominator = (angle_theta+np.sin(angle_theta/2.))
    V_Vf = (numerator/denominator)**0.62
    return V_Vf