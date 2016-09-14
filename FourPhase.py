"""Test all four phases in one."""
import decimal as dec
import os


def closest_finder(self):
    """Find the closest value to a given value."""
    combined = set(map(str.rstrip, open(
        (os.path.join(os.path.dirname(__file__), '1809045225.txt')))))
    closest = min(combined, key=lambda x: abs(
        dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    print(closest)
    return closest
    del combined


def check(self, set180, set90, set45, set225, closest):
    """Check to find the most accurate four phase solution."""
    dec.getcontext().prec = 6
    for i in set180:
        for j in set90:
            for k in set45:
                for l in set225:
                    total = i + j + k + l
                    if total == closest:
                        for row in self.s180:
                            if row[self.phase28].value == i:
                                row1 = int(row[0].value)
                                att1 = dec.Decimal(row[self.att28].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phaselow1 = dec.Decimal(row[self.phase24].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasediff1 = phasehigh1 - phaselow1

                        for row in self.s90:
                            if row[self.phase28].value == j:
                                row2 = int(row[0].value)
                                att2 = dec.Decimal(row[self.att28].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phaselow2 = dec.Decimal(row[self.phase24].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasehigh2 = dec.Decimal(row[self.att32].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasediff2 = phasehigh2 - phaselow2

                        for row in self.s45:
                            if row[self.phase28].value == k:
                                row3 = int(row[0].value)
                                att3 = dec.Decimal(row[self.att28].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phaselow3 = dec.Decimal(row[self.att24].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasehigh3 = dec.Decimal(row[self.att32].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasediff3 = phasehigh3 - phaselow3

                        for row in self.s225:
                            if row[self.phase28].value == l:
                                row4 = int(row[0].value)
                                att4 = dec.Decimal(row[self.att28].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phaselow4 = dec.Decimal(row[self.phase24].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasehigh4 = dec.Decimal(row[self.phase32].value).quantize(
                                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                                phasediff4 = phasehigh4 - phaselow4

                        totalatt = att1 + att2 + att3 + att4
                        return {'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's90', 'phase3': k.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row3': row3, 'att3': att3, 'phasediff3': phasediff3, 'source3': 's45', 'phase4': l.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row4': row4, 'att4': att4, 'phasediff4': phasediff4, 'source4': 's225', 'total': total.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}
