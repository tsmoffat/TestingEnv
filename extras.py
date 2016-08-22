import decimal as dec


def check180(self, s180, set180):
        """180 degrees of magic"""
        dec.getcontext().prec = 6
        if self.targetphase in set180:
            print("Found it!")
            for row in s180.iter_rows():
                if row[self.phase28].value == self.targetphase:
                    row1 = int(row[0].value)
                    att1 = dec.Decimal(row[self.att28].value)
                    attlow = dec.Decimal(row[self.att24].value)
                    atthigh = dec.Decimal(row[self.att32].value)
                    attdiff = atthigh - attlow

            print("Optimal solution found, it is state " + str(row1))
            print(att1)
            return{'row1': row1, 'att1': att1, 'attdiff': attdiff}
        else:
            closest = min(set180, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
            for row in s180.iter_rows():
                if row[self.phase28].value == closest:
                    row1 = int(row[0].value)
                    att1 = dec.Decimal(row[self.att28].value)
                    phaselow = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                    phasehigh = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                    phasediff = phasehigh - phaselow
                    print(phaselow, phasehigh, phasediff)

            print("The closest current solution is " + str(row1))
            print(att1).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
            return {'phase1': closest, 'row1': row1, 'att1': att1, 'phasediff': phasediff}