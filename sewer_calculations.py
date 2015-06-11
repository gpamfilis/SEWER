__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import numpy as np


def pipe_diameter(n0, q0, s):
    numerator = (4**(5./3)*n0*q0)
    denomenator = np.pi*s**(1/2.)
    return (numerator/denomenator)**(3./8)


def flow_in_circular_pipe(n, d, s):
    return (np.pi/(4**(5./3)))*(1./n)*(d**(8./3))*(s**0.5)


def velocity_in_circular_pipe(q, d):
    return (4*q)/(np.pi*d**2)
