from __future__ import division
__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import pandas as pd
from sewer_calculations import *
from law_guidelines import *
data = pd.read_excel('sewer_data.xlsx', sheetname='data-sewer')


class SewerDesign:
    """
    http://www.researchgate.net/publication/245336759_
    Simple_Formulae_for_Velocity_Depth_of_Flow_and_Slope_Calculations_in_Partially_Filled_Circular_Pipes

    """

    def __init__(self):
        self.n0 = 0.015
        pass

    def type_one(self, flow_rate, slope, fullness_ratio, network_type='pantoroiko'):
        """
        :param flow_rate: flow rate [m^3/sec]
        :param slope: slope [m/km]
        :param fullness_ratio: fullness ratio
        :return:
        """
        flow_rate /= 1000.
        print '[1.T1] Q is: {} [m^3/sec]'.format(flow_rate)
        diameter_min = 0.4
        # step 1 full pipe flow
        flow_full_pipe = flow_rate / flow_ratio_calculation(fullness_ratio)
        print '[1.T1] Q0 is: {} [m^3/sec]'.format(flow_full_pipe)
        pipe_diameter = diameter_from_available(pipe_diameter_calculation(self.n0, flow_full_pipe, slope))
        print '[2.T1] The pipe diameter is: {} [m]'.format(pipe_diameter)
        if pipe_diameter < diameter_min:
            print '[3.T1] needs diameter >= {} [m]'.format(diameter_min)
            new_diameter = input('new diameter? (start with 0.4 [m]): ')
            self.type_two(flow_rate, slope, new_diameter)
        else:
            print 'diameter is ok: ', pipe_diameter
            #new_diameter = input('new diameter [m]: ')
            print '[4.T1] Proceeding for TYPE-3 hydraulics problem (check whether the diameter is fit for our case'
            self.type_three(flow_rate, slope, pipe_diameter)

    def type_two(self, flow_rate, slope, pipe_diameter):
        #step 1
        flow_full_pipe = flow_in_circular_pipe(self.n0, pipe_diameter, slope)
        velocity_full_pipe = velocity_in_circular_pipe(flow_full_pipe, pipe_diameter)
        # step 2
        flow_ratio = flow_rate/flow_full_pipe
        print 'the Q/Q0 ratio is: {}'.format(flow_ratio)
        # step 3
        fullness_ratio = input('for flow_rate/q0 what is the ratio y/pipe_diameter: ')
        velocity_ratio = velocity_ratio_calculation(fullness_ratio)
        # step 4
        h = pipe_diameter*fullness_ratio
        # step 5
        velocity = velocity_full_pipe*velocity_ratio
        law_checks_pantoroika(pipe_diameter, fullness_ratio, velocity, velocity_full_pipe)
        return None

    def type_three(self, flow_rate, slope, pipe_diameter):
        """
        :param flow_rate: flow rate [m^3/sec]
        :param slope: slope [m/km]
        :param pipe_diameter: pipe diameter [m]
        :return:
        """
        flow_full_pipe = flow_in_circular_pipe(self.n0, pipe_diameter, slope)
        velocity_full_pipe = velocity_in_circular_pipe(flow_full_pipe, pipe_diameter)
        flow_ratio = flow_rate/flow_full_pipe
        fullness_ratio = input('for Q/Q0 = {} what is the ratio y/pipe_diameter_calculation: '.format(flow_ratio))
        velocity_ratio = velocity_ratio_calculation(fullness_ratio)
        velocity = velocity_ratio*velocity_full_pipe
        law_checks_pantoroika(pipe_diameter, fullness_ratio, velocity, velocity_full_pipe)




if __name__ == '__main__':
    sd = SewerDesign()
    x = raw_input('from file [y] or one by one [n]: ')
    if x == 'y':
        for i, d in enumerate(data['Q']):
            print 'SECTION: ', data['Section'][i]
            print ''
            sd.type_one(d/1000., data['S'][i], 0.5)  # divide with 1000 to convert to m^3/sec
            print ''
    else:

        q = input('enter flow rate [L/s]: ')
        s = input('enter slope [-]: ')
        y_d = input('enter fullness ratio y/D [-]: ')
        sd.type_one(q, s, y_d)
