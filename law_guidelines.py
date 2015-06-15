__author__ = 'giorgos'
__author__ = 'George Pamfilis'
__version__ = '1.0'
__contact__ = 'gpamfilis@gmail.com'


def law_checks_mixed_flow(pipe_diameter, fullness_ratio, velocity, velocity_full):
    max_velocity = 3.
    min_velocity = 0.6
    v0min = 1.11
    fullness_ratio_law = 0.5
    if pipe_diameter >= 0.4:
        print '[1.] diameter is OK {} [m]'.format(pipe_diameter)
    else:
        print '[1.] diameter is NOT OK!!: ', pipe_diameter
    if fullness_ratio <= fullness_ratio_law:
        print '[2.] y/D is OK: {} [-] '.format(fullness_ratio)
    else:
        print('[2.] y/D ratio is NOT OK!! {} [-]'.format(fullness_ratio))
    if velocity < max_velocity:
        print '[3.] Velocity is below max is OK: {} [m/s]'.format(velocity)
    else:
        print('[3.] Velocity is above max is NOT OK!!: {} [m/s]'.format(velocity))
    if velocity > min_velocity:
        print '[4.] Velocity is above min is OK: {} [m/s]'.format(velocity)
    else:
        print('[4.] Velocity is below min is NOT OK!!: {} [m/s]'.format(velocity))
    if velocity_full > v0min:
        print '[5.] elaxistes kliseis OK: {} [m/s]'.format(velocity_full)


