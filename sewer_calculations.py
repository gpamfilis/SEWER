__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import numpy as np


def pipe_diameter_calculation(manning_coefficient, flow_full_pipe, slope):
    numerator = (4**(5./3)*manning_coefficient*flow_full_pipe)
    denominator = np.pi*slope**(1/2.)
    return (numerator/denominator)**(3./8)


def flow_in_circular_pipe(manning_coefficient, pipe_diameter, slope):
    return (np.pi/(4**(5./3)))*(1./manning_coefficient)*(pipe_diameter**(8./3))*(slope**0.5)


def velocity_in_circular_pipe(flow_full_pipe, pipe_diameter):
    return (4*flow_full_pipe)/(np.pi*pipe_diameter**2)


def theta(fullness_ratio):
    theta_angle = 2*np.arccos((1-(2*fullness_ratio)))
    return theta_angle


def flow_ratio(fullness_ratio):
    theta_angle = theta(fullness_ratio)
    numerator = (theta_angle-np.sin(theta_angle))**1.62
    denominator = (theta_angle+np.sin(theta_angle/2))**0.62
    q_qf = (1./2*np.pi)*(numerator/denominator)
    return q_qf/10.


def velocity_ratio(fullness_ratio):
    angle_theta = theta(fullness_ratio)
    numerator = (angle_theta-np.sin(angle_theta))
    denominator = (angle_theta+np.sin(angle_theta/2.))
    v_vf = (numerator/denominator)**0.62
    return v_vf