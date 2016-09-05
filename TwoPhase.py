"""Module to test two phases"""
import Decimal as dec


def check1(self, s180, s90, set180, set90):
    dec.getcontext().prec = 6
    combined = [x + y for x, y in zip(set180, set90)]
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    for i in s180.iter_rows():
        for j in s90.iter_rows():
            total = i[self.phase28].value + j[self.phase28].value
            if total == closest:
                for row in s180:
                    if row[self.phase28].value == i:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in s90:
                    if row[self.phase28].value == j:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.att32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                print("The closest solution is state " + str(row1) + " " + str(row2))
                print(att1)
                print(att2)
                return {'phase1': i, 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j, 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's90', }


def check2(self, s180, s45, set180, set45):
    dec.getcontext().prec = 6
    combined = [x + y for x, y in zip(set180, set45)]
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    for i in s180.iter_rows():
        for j in s180.iter_rows():
            total = i[self.phase28].value + j[self.phase28].value
            if total == closest:
                for row in s180:
                    if row[self.phase28].value == i[self.phase28].value:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in s45:
                    if row[self.phase28].value == j[self.phase28].value:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                print("The closest solution is state " + str(row1) + " " + str(row2))
                print(att1)
                print(att2)
                return {'phase1': i, 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j, 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's90', }


def check3(self, s180, s225, set180, set225):
    dec.getcontext().prec = 6
    combined = [x + y for x, y in zip(set180, set225)]
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    for i in s180.iter_rows():
        for j in s225.iter_rows:
            total = i[self.phase28].value + j[self.phase28].value
            if total == closest:
                for row in s180:
                    if row[self.phase28].value == i[self.phase28].value:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in s225:
                    if row[self.phase28].value == j[self.phase28].value:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                print("The closest solution is state " + str(row1) + " " + str(row2))
                print(att1)
                print(att2)
                return {'phase1': i, 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j, 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's90', }
