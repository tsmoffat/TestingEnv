"""Module to test two phases"""
import decimal as dec


def check1(self, set180, set90):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('18090.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    del combined
    for i in set180:
        for j in set90:
            total = i + j
            if total == closest:
                for row in self.s180:
                    if row[self.phase28].value == i:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in self.s90:
                    if row[self.phase28].value == j:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.att32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                totalatt = att1 + att2
                return{'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's90', 'total': dec.Decimal(total), 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check2(self, set180, set45):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('18045.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set180:
        for j in set45:
            total = i + j
            if total == closest:
                for row in self.s180:
                    if row[self.phase28].value == i:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in self.s45:
                    if row[self.phase28].value == j:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                totalatt = att1 + att2
                return{'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's45', 'total': total, 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check3(self, set180, set225):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('180225.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set180:
        for j in set225:
            total = i + j
            if total == closest:
                for row in self.s180:
                    if row[self.phase28].value == i:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in self.s225:
                    if row[self.phase28].value == j:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                totalatt = att1 + att2
                return{'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's225', 'total': total, 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check4(self, set90, set45):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('9045.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set90:
        for j in set45:
            total = i + j
            if total == closest:
                for row in self.s90:
                    if row[self.phase28].value == i:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in self.s45:
                    if row[self.phase28].value == j:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                totalatt = att1 + att2
                return{'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's90', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's45', 'total': total, 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check5(self, set90, set225):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('90225.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set90:
        for j in set225:
            total = i + j
            if total == closest:
                for row in self.s90:
                    if row[self.phase28].value == i:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in self.s225:
                    if row[self.phase28].value == j:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                totalatt = att1 + att2
                return {'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's90', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's225', 'total': total, 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check6(self, set45, set225):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('45225.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set45:
        for j in set225:
            total = dec.Decimal(i) + dec.Decimal(j)
            if total == closest:
                for row in self.s45:
                    if row[self.phase28].value == i:
                        row1 = int(row[0].value)
                        att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh1 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff1 = phasehigh1 - phaselow1

                for row in self.s225:
                    if row[self.phase28].value == j:
                        row2 = int(row[0].value)
                        att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phaselow2 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                        phasediff2 = phasehigh2 - phaselow2

                totalatt = att1 + att2
                return {'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's45', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's225', 'total': total, 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def checkall(self, set180, set90, set45, set225):
    dec.getcontext().prec = 6
    sollist = []
    sol1 = check1(self, set180, set90)
    sollist.append(sol1["total"])
    sol2 = check2(self, set180, set45)
    sollist.append(sol2['total'])
    sol3 = check3(self, set180, set225)
    sollist.append(sol3['total'])
    sol4 = check4(self, set90, set45)
    sollist.append(sol4['total'])
    sol5 = check5(self, set90, set225)
    sollist.append(sol5['total'])
    sol6 = check6(self, set45, set225)
    sollist.append(sol6['total'])

    if sol1['total'] == self.targetphase:
        return sol1
    elif sol2['total'] == self.targetphase:
        return sol2
    elif sol3['total'] == self.targetphase:
        return sol3
    elif sol4['total'] == self.targetphase:
        return sol4
    elif sol5['total'] == self.targetphase:
        return sol5
    elif sol6['total'] == self.targetphase:
        return sol6
    else:
        closest = min(sollist, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
        if sol1['total'] == closest:
            return sol1
        elif sol2['total'] == closest:
            return sol2
        elif sol3['total'] == closest:
            return sol3
        elif sol4['total'] == closest:
            return sol4
        elif sol5['total'] == closest:
            return sol5
        elif sol6['total'] == closest:
            return sol6
        else:
            return None
