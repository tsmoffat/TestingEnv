"""Format numbers to be output as settings for MPAC."""


def phaseformat(self, bestphase):
    """Format phase settings correctly."""
    s180present = 0
    s90present = 0
    s45present = 0
    s225present = 0
    if 'source1' in bestphase:
        if bestphase['source1'] == 's180':
            s180present = 1
        elif bestphase['source1'] == 's90':
            s90present = 1
        elif bestphase['source1'] == 's45':
            s45present = 1
        elif bestphase['source1'] == 's225':
            s225present = 1
    if 'source2' in bestphase:
        if bestphase['source2'] == 's90':
            s90present = 2
        elif bestphase['source2'] == 's45':
            s45present = 2
        elif bestphase['source2'] == 's225':
            s225present = 2

    if 'source3' in bestphase:
        if bestphase['source3'] == 's45':
            s45present = 3
        elif bestphase['source3'] == 's225':
            s225present = 3

    if 'source4' in bestphase:
        if bestphase['source4'] == 's225':
            s225present = 4
    if s180present == 1:
        s180setting = '{0:02b}'.format(bestphase['row1'])
    else:
        s180setting = '{0:02b}'.format(2)

    if s90present == 1:
        s90setting = '{0:06b}'.format(bestphase['row1'])
    elif s90present == 2:
        s90setting = '{0:06b}'.format(bestphase['row2'])
        s90present = 1
    else:
        s90setting = '{0:06b}'.format(32)

    if s45present == 1:
        s45setting = '{0:09b}'.format(bestphase['row1'])
    elif s45present == 2:
        s45setting = '{0:09b}'.format(bestphase['row2'])
        s45present = 1
    elif s45present == 3:
        s45setting = '{0:09b}'.format(bestphase['row3'])
        s45present = 1
    else:
        s45setting = '{0:09b}'.format(256)

    if s225present == 1:
        s225setting = '{0:09b}'.format(bestphase['row1'])
    elif s225present == 2:
        s225setting = '{0:09b}'.format(bestphase['row2'])
        s225present = 1
    elif s225present == 3:
        s225setting = '{0:09b}'.format(bestphase['row3'])
        s225present = 1
    elif s225present == 4:
        s225setting = '{0:09b}'.format(bestphase['row4'])
        s225present = 1
    else:
        s225setting = '{0:09b}'.format(256)

    return {'s180setting': s180setting, 's90setting': s90setting, 's45setting': s45setting, 's225setting': s225setting}


def attformat(self, bestatt):
    """Format attenuation for the MPAC."""
    return '{0:012b}'.format(bestatt['row28'])
