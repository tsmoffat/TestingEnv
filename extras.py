"""Literally some magic"""
import decimal as dec


def check180(self, set180):
    """180 degrees of magic"""
    dec.getcontext().prec = 6
    if self.targetphase in set180:
        print("Found it!")
        for row in self.s180.iter_rows():
            if row[self.phase28].value == self.targetphase:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow

        print("Optimal solution found, it is state " + str(row1))
        print(att1)
        return {'phase1': self.targetphase, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's180'}
    else:
        closest = min(set180, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
        for row in self.s180.iter_rows():
            if row[self.phase28].value == closest:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow
                print(phaselow, phasehigh, phasediff)

        print("The closest current solution is " + str(row1))
        print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
        return {'phase1': closest, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's180'}


def check90(self, set90):
    """90 degrees of magic"""
    dec.getcontext().prec = 6
    if self.targetphase in set90:
        print("Found it!")
        for row in self.s90.iter_rows():
            if row[self.phase28].value == self.targetphase:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow

        print("Optimal solution found, it is state " + str(row1))
        print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
        return {'phase1': self.targetphase, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's180'}

    else:
        closest = min(set90, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
        for row in self.s90.iter_rows():
            if row[self.phase28].value == closest:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow

        print("The closest current solution is state " + str(row1))
        print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
        return {'phase1': closest, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's180'}


def check45(self, set45):
    """45 Degrees of magic

        Parameters
        ----------
        self, set45, set45
        Returns
        -------
        phase1, row1, att1, phasediff
        """

    dec.getcontext().prec = 6
    if self.targetphase in set45:
        print("Found it!")
        for row in self.s45.iter_rows():
            if row[self.phase28].value == self.targetphase:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow

        print("Optimal solution found, it is state " + str(row1))
        print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
        return {'phase1': self.targetphase, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's180'}

    else:
        closest = min(set45, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
        for row in self.s45.iter_rows():
            if row[self.phase28].value == closest:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow

        print("The closest current solution is state " + str(row1))
        print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
        return {'phase1': closest, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's180'}


def check225(self, set225):
    """22.5 degrees of magic

    Parameters
    ----------
    self, s225, set225
    Returns
    -------
    phase1, row1, att1, phasediff
    """

    dec.getcontext().prec = 6
    if self.targetphase in set225:
        print("Found it!")
        for row in self.s225.iter_rows():
            if row[self.phase28].value == self.targetphase:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow

        print("Optimal solution found, it is state " + str(row1))
        print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
        return {'phase1': self.targetphase, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's180'}

    else:
        closest = min(set225, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
        for row in self.s225.iter_rows():
            if row[self.phase28].value == closest:
                row1 = int(row[0].value)
                att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                phasediff = phasehigh - phaselow

            print("The closest solution is state " + str(row1))
            print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
            return {'phase1': closest, 'row1': row1, 'att1': att1, 'phasediff': phasediff, 'source': 's225'}


def checkall(self, set180, set90, set45, set225):
    """Checks to find most accurate solution so far

    Parameters
    ----------
    self
    Returns
    -------
    bestsol data dict
    """

    dec.getcontext().prec = 6
    sol180 = check180(self, set180)
    sol90 = check90(self, set90)
    sol45 = check45(self, set45)
    sol225 = check225(self, set225)

    sollist = [sol180, sol90, sol45, sol225]
    for phase1 in sollist:
    #Can't remember what I was going for here, will come back to it

        if phase1 == self.targetphase:
            return

