__author__ = 'giorgos'
__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'


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


