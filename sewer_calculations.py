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


def theta_angle_in_pipe(fullness_ratio):
    theta_angle = 2*np.arccos((1-(2*fullness_ratio)))
    return theta_angle


def flow_ratio_calculation(fullness_ratio):
    theta_angle = theta_angle_in_pipe(fullness_ratio)
    numerator = (theta_angle-np.sin(theta_angle))**1.62
    denominator = (theta_angle+np.sin(theta_angle/2))**0.62
    q_qf = (1./2*np.pi)*(numerator/denominator)
    return q_qf/10.


def velocity_ratio_calculation(fullness_ratio):
    angle_theta = theta_angle_in_pipe(fullness_ratio)
    numerator = (angle_theta-np.sin(angle_theta))
    denominator = (angle_theta+np.sin(angle_theta/2.))
    velocity_ratio = (numerator/denominator)**0.62
    return velocity_ratio


def manning_coefficient_ratio_calculation(fullness_ratio):
    theta_angle = theta_angle_in_pipe(fullness_ratio)
    n_n0 = 1+2.31*(theta_angle/(2*np.pi))**1.2*(1-(theta_angle/(2*np.pi)))**2
    return n_n0


def diameter_from_available(computed_diameter):
    available_diameters = [0.35, 0.40, 0.45, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0, 1.1,
                           1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    for i, pipe_diameter in enumerate(available_diameters):
        if pipe_diameter < computed_diameter:
            pass
        else:
            computed_diameter = pipe_diameter
            break
    return computed_diameter


if __name__ == '__main__':
    print flow_ratio_calculation(0.5)