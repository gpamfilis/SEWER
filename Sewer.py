from __future__ import division
__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'

import numpy as np
import matplotlib.pyplot as plt

class SewerDesign:

    def __init__(self):
        self.n0 = 0.015
        pass

    @staticmethod
    def theta(y_d):
        theta = 2*np.arccos((1-(2*y_d)))
        return theta

    def q_qf_y_d(self, h_d):
        theta = self.theta(h_d)
        numerator = (theta-np.sin(theta))**1.62
        denominator = (theta+np.sin(theta/2))**0.62
        q_qf = (1./2*np.pi)*(numerator/denominator)
        return q_qf/10.

    def v_vf_h_d(self, h_d):
        theta = self.theta(h_d)
        numerator = (theta-np.sin(theta))
        denomenator = (theta+np.sin(theta/2.))
        V_Vf = (numerator/denomenator)**0.62
        return V_Vf

    @staticmethod
    def pipe_diameter(n0, Q0, S):
        numerator = (4**(5./3)*n0*Q0)
        denomenator = np.pi*S**(1/2.)
        return (numerator/denomenator)**(3./8)

    @staticmethod
    def Q_pipe_circular(n, D, S):
        return (np.pi/(4**(5./3)))*(1./n)*(D**(8./3))*(S**0.5)

    @staticmethod
    def V_pipe_circular(Q, D):
        return (4*Q)/(np.pi*D**2)

    @staticmethod
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
            print '[2.] y/D ok: ',y_d
        else:
            print('[2.] y/D ratio not OK {}'.format(y_d))
        if v < vmax:
            print '[3.] below max velocity OK: {}'.format(v)
        else:
            print('[3.] velocity above max:  {}'.format(v))
        if v > vmin:
            print '[4.] above min velocity OK!'
        else:
            print('[4.] velocity below min!!!:  {}'.format(v))
        if v0 > v0min:
            print '[5.] elaxistes kliseis OK: {}'.format(v0)

    def type_one(self, q, s, y_d):
        """
        :param q: flow rate [m^3/s]
        :param s: slope [m/km]
        :param y_d: fullness ratio
        :return:
        """
        #step 1 full pipe flow
        Q0 = q/self.q_qf_y_d(y_d)
        print 'Q0 is: {}'.format(Q0)
        D = self.pipe_diameter(self.n0, Q0, s)
        if D < 0.4:
            print 'needs larger diameter', D
            self.type_two(q, s, 0.4)
        else:
            print 'diameter is ok: ', D
            self.type_three()

    def type_two(self, q, s, d):
        #step 1
        q0 = self.Q_pipe_circular(self.n0, d, s)
        v0 = self.V_pipe_circular(q0, d)
        # step 2
        q_q0 = q/q0*10**-3
        print 'the q/Q0 ratio is: {}'.format(q_q0)
        # step 3
        y_d = input('for q/q0 what is the ratio y/d: ')
        v_v0 = self.v_vf_h_d(y_d)
        # step 4
        h = d*y_d
        # step 5
        v = v0*v_v0
        self.law_checks_pantoroika(d, y_d, v, v0)
        return None

    def type_three(self, q, s, d):
        """
        :param q: flow rate [m^3/s]
        :param s: slope [m/km]
        :param d: pipe diameter [m]
        :return:
        """
        q0 = self.Q_pipe_circular(self.n0, d, s)
        v0 = self.V_pipe_circular(q0, d)
        q_q0 = q/q0
        y_d = input('for Q/Q0 = {} what is the ratio y/d: '.format(q_q0))
        v_v0 = self.v_vf_h_d(y_d)
        v = v_v0*v0
        self.law_checks_pantoroika(d, y_d, v, v0)

if __name__ == '__main__':
    sd = SewerDesign()
    #print sd.type_one(0.718, 0.004, 0.7)
    print sd.type_three(0.718, 0.004, 1)
