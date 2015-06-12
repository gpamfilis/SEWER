from __future__ import division
__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import pandas as pd
from sewer_calculations import *
data = pd.read_excel('sewer_data.xlsx', sheetname='data-sewer')

class SewerDesign:
    """
    http://www.researchgate.net/publication/245336759_
    Simple_Formulae_for_Velocity_Depth_of_Flow_and_Slope_Calculations_in_Partially_Filled_Circular_Pipes

    """

    def __init__(self):
        self.n0 = 0.015
        pass

    def type_one(self, flow_rate, slope, fullness_ratio):
        """
        :param flow_rate: flow rate [m^3/sec]
        :param slope: slope [m/km]
        :param fullness_ratio: fullness ratio
        :return:
        """
        #step 1 full pipe flow
        flow_full_pipe = flow_rate/ flow_ratio(fullness_ratio)
        print 'Q0 is: {} [m^3/sec]'.format(flow_full_pipe)
        D = diameter_from_available(pipe_diameter_calculation(self.n0, flow_full_pipe, slope))
        if D < 0.4:
            print 'needs larger diameter', D
            dia = input('new diameter [m]: ')
            self.type_two(flow_rate, slope, dia)
        else:
            print 'diameter is ok: ', D
            dia = input('new diameter [m]: ')

            self.type_three(flow_rate, slope, dia)

    def type_two(self, q, s, d):
        #step 1
        q0 = flow_in_circular_pipe(self.n0, d, s)
        v0 = velocity_in_circular_pipe(q0, d)
        # step 2
        q_q0 = q/q0
        print 'the q/Q0 ratio is: {}'.format(q_q0)
        # step 3
        y_d = input('for q/q0 what is the ratio y/d: ')
        v_v0 = velocity_ratio(y_d)
        # step 4
        h = d*y_d
        # step 5
        v = v0*v_v0
        law_checks_pantoroika(d, y_d, v, v0)
        return None

    def type_three(self, flow_rate, slope, pipe_diameter):
        """
        :param flow_rate: flow rate [m^3/sec]
        :param slope: slope [m/km]
        :param pipe_diameter: pipe diameter [m]
        :return:
        """
        q0 = flow_in_circular_pipe(self.n0, pipe_diameter, slope)
        v0 = velocity_in_circular_pipe(q0, pipe_diameter)
        q_q0 = flow_rate/q0
        y_d = input('for Q/Q0 = {} what is the ratio y/pipe_diameter_calculation: '.format(q_q0))
        v_v0 = velocity_ratio(y_d)
        v = v_v0*v0
        law_checks_pantoroika(pipe_diameter, y_d, v, v0)





def law_checks_pantoroika(d, y_d, v, v0):
    vmax = 3.
    vmin = 0.6
    v0min = 1.11
    yd_law = 0.5
    if d >= 0.4:
        print '[1.] diameter ok {} [m]'.format(d)
    else:
        print '[1.] diameter not ok: ', d
    if y_d <= yd_law:
        print '[2.] y/D ok: {} [-] '.format(y_d)
    else:
        print('[2.] y/D ratio not OK {} [-]'.format(y_d))
    if v < vmax:
        print '[3.] below max velocity OK: {} [m/s]'.format(v)
    else:
        print('[3.] velocity above max: {} [m/s]'.format(v))
    if v > vmin:
        print '[4.] above min velocity OK!: {} [m/s]'.format(v)
    else:
        print('[4.] velocity below min!!!: {} [m/s]'.format(v))
    if v0 > v0min:
        print '[5.] elaxistes kliseis OK: {} [m/s]'.format(v0)


def diameter_from_available(theoretical_diameter):
    available_diameters = [0.35, 0.40, 0.45, 0.50, 0.60, 0.70, 0.80, 0.90, 1.0, 1.1,
                           1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0, 2.2, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    for i, D in enumerate(available_diameters):
        if D < theoretical_diameter:
            pass
        else:
            theoretical_diameter = D
            break
    return theoretical_diameter

if __name__ == '__main__':
    sd = SewerDesign()
    x = raw_input('from file [y] or one by one [n]: ')
    if x == 'y':
        for i, d in enumerate(data['Q']):
            print 'SECTION: ', data['Section'][i]
            print ''
            sd.type_one(d/1000., data['S'][i], 0.5)
            print ''
    else:

        q = input('enter flow rate [m^3/s]: ')
        s = input('enter slope [-]: ')
        y_d = input('enter fullness ratio y/D [-]: ')
        sd.type_one(q/1000., s, y_d)
