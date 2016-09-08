"""Test three phase solutions"""
import decimal as dec


def check1(self, set180, set90, set45):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('1809045.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set180:
        for j in set90:
            for k in set45:
                total = i + j + k
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
                            phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff2 = phasehigh2 - phaselow2

                    for row in self.s45:
                        if row[self.phase28].value == k:
                            row3 = int(row[0].value)
                            att3 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow3 = dec.Decimal(row[self.att24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh3 = dec.Decimal(row[self.att32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff3 = phasehigh3 - phaselow3

                    print("The closest solution is: ")
                    print(row1, row2, row3)
                    totalatt = att1 + att2 + att3
                    return {'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's90', 'phase3': k.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row3': row3, 'att3': att3, 'phasediff3': phasediff3, 'source3': 's45', 'total': total.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check2(self, set180, set90, set225):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('18090225.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set180:
        for j in set90:
            for k in set225:
                total = i + j + k
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
                            phasehigh2 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff2 = phasehigh2 - phaselow2

                    for row in self.s225:
                        if row[self.phase28].value == k:
                            row3 = int(row[0].value)
                            att3 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow3 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh3 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff3 = phasehigh3 - phaselow3

                    print("The closest solution is: ")
                    print(row1, row2, row3)
                    totalatt = att1 + att2 + att3
                    return {'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's90', 'phase3': k.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row3': row3, 'att3': att3, 'phasediff3': phasediff3, 'source3': 's225', 'total': total.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check3(self, set180, set45, set225):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('18045225.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set180:
        for j in set45:
            for k in set225:
                total = i + j + k
                if total == closest:
                    for row in self.s180:
                        if row[self.phase28].value == i:
                            row1 = int(row[0].value)
                            att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh1 = dec.Decimal(row[self.phase32].value).  quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff1 = phasehigh1 - phaselow1

                    for row in self.s45:
                        if row[self.phase28].value == j:
                            row2 = int(row[0].value)
                            att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow2 = dec.Decimal(row[self.att24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh2 = dec.Decimal(row[self.att32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff2 = phasehigh2 - phaselow2

                    for row in self.s225:
                        if row[self.phase28].value == k:
                            row3 = int(row[0].value)
                            att3 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow3 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh3 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff3 = phasehigh3 - phaselow3

                    print("The closest solution is: ")
                    print(row1, row2, row3)
                    totalatt = att1 + att2 + att3
                    return {'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's180', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's45', 'phase3': k.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row3': row3, 'att3': att3, 'phasediff3': phasediff3, 'source3': 's225', 'total': total.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def check4(self, set90, set45, set225):
    dec.getcontext().prec = 6
    combined = set(map(str.rstrip, open('9045225.txt')))
    closest = min(combined, key=lambda x: abs(dec.Decimal(x) - dec.Decimal(self.targetphase)))
    closest = dec.Decimal(closest)
    for i in set90:
        for j in set45:
            for k in set225:
                total = i + j + k
                if total == closest:
                    for row in self.s90:
                        if row[self.phase28].value == i:
                            row1 = int(row[0].value)
                            att1 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow1 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh1 = dec.Decimal(row[self.att32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff1 = phasehigh1 - phaselow1

                    for row in self.s45:
                        if row[self.phase28].value == j:
                            row2 = int(row[0].value)
                            att2 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow2 = dec.Decimal(row[self.att24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh2 = dec.Decimal(row[self.att32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff2 = phasehigh2 - phaselow2

                    for row in self.s225:
                        if row[self.phase28].value == k:
                            row3 = int(row[0].value)
                            att3 = dec.Decimal(row[self.att28].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phaselow3 = dec.Decimal(row[self.phase24].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasehigh3 = dec.Decimal(row[self.phase32].value).quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                            phasediff3 = phasehigh3 - phaselow3

                    print("The closest solution is: ")
                    print(row1, row2, row3)
                    totalatt = att1 + att2 + att3
                    return {'phase1': i.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row1': row1, 'att1': att1, 'phasediff1': phasediff1, 'source1': 's90', 'phase2': j.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row2': row2, 'att2': att2, 'phasediff2': phasediff2, 'source2': 's45', 'phase3': k.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'row3': row3, 'att3': att3, 'phasediff3': phasediff3, 'source3': 's225', 'total': total.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP), 'totalatt': totalatt.quantize(dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)}


def checkall(self, set180, set90, set45, set225):
    dec.getcontext().prec = 6
    sol1 = check1(self, set180, set90, set45)
    sol2 = check2(self, set180, set90, set225)
    sol3 = check3(self, set180, set45, set225)
    sol4 = check4(self, set90, set45, set225)

    sollist = [sol1['total'], sol2['total'], sol3['total'], sol4['total']]
    if sol1['total'] == self.targetphase:
        return sol1
    elif sol2['total'] == self.targetphase:
        return sol2
    elif sol3['total'] == self.targetphase:
        return sol3
    elif sol4['total'] == self.targetphase:
        return sol4
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
        else:
            return None
