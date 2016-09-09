"""To generate a look-up table"""
import decimal as dec
import extras as ex
import TwoPhase as twp
import ThreePhase as thp
import FourPhase as fp
import tabulate


def tablegen(self):
    list180 = []
    for row in self.s180.iter_rows(row_offset=2):
        if row[self.phase28].value is not None:
            list180.append(dec.Decimal(row[self.phase28].value))
    set180 = set(list180)

    list90 = []
    for row in self.s90.iter_rows(row_offset=2):
        if row[self.phase28].value is not None:
            list90.append(dec.Decimal(row[self.phase28].value))
    set90 = set(list90)

    list45 = []
    for row in self.s45.iter_rows(row_offset=2):
        if row[self.phase28].value is not None:
            list45.append(dec.Decimal(row[self.phase28].value))
    set45 = set(list45)

    list225 = []
    for row in self.s225.iter_rows(row_offset=2):
        if row[self.phase28].value is not None:
            list225.append(dec.Decimal(row[self.phase28].value))
    set225 = set(list225)
    headers = ["Target value", "180 Used", "90 Used", "45 Used", "22.5 Used", "180 Setting", "90 Setting", "45 Setting", "22.5 Setting"]
    table = []
    for i in range(1, 256):
        self.targetphase = (360 / 64) * i
        bestresult = ex.checkall(self, set180, set90, set45, set225)
        bestresult2 = twp.checkall(self, set180, set90, set45, set225)
        bestresult3 = thp.checkall(self, set180, set90, set45, set225)
        bestresult4 = fp.check(self, set180, set90, set45, set225)
        sollist = [bestresult['total'], bestresult2['total'], bestresult3['total'], bestresult4['total']]
        bestphase = ex.mostaccurate(self, bestresult, bestresult2, bestresult3, bestresult4, sollist)
        if bestphase['source1'] == 's180':
            s180present = 1
        else:
            s180present = 0
        if bestphase['source1'] == 's90':
            s90present = 1
        elif bestphase['source2'] == 's90':
            s90present = 2
        else:
            s90present = 0
        if bestphase['source1'] == 's45':
            s45present = 1
        elif bestphase['source2'] == 's45':
            s45present = 2
        elif bestphase['source3'] == 's45':
            s45present = 3
        else:
            s45present = 0
        if bestphase['source1'] == 's225':
            s225present = 1
        elif bestphase['source2'] == 's225':
            s225present = 2
        elif bestphase['source3'] == 's225':
            s225present = 3
        elif bestphase['source4'] == 's225':
            s225present = 4
        else:
            s225present = 0

        if s180present == 1:
            s180setting = "{0:2b}".format(bestresult['row1'])
        else:
            s180setting = "{0:2b}".format(2)

        if s90present == 1:
            s90setting = "{0:6b}".format(bestresult['row1'])
        elif s90present == 2:
            s90setting = "{0:6b}".format(bestresult['row2'])
            s90present = 1
        else:
            s90setting = "{0:6b}".format(32)

        if s45present == 1:
            s45setting = "{0:9b}".format(bestresult['row1'])
        elif s45present == 2:
            s45setting = "{0:9b}".format(bestresult['row2'])
            s45present = 1
        elif s45present == 3:
            s45setting = "{0:9b}".format(bestresult['row3'])
            s45present = 1
        else:
            s45setting = "{0:9b}".format(256)

        if s225present == 1:
            s45setting = "{0:9b}".format(bestresult['row1'])
        elif s225present == 2:
            s225setting = "{0:9b}".format(bestresult['row2'])
            s225present = 1
        elif s225present == 3:
            s225setting = "{0:9b}".format(bestresult['row3'])
            s225present = 1
        elif s225present == 4:
            s225setting = "{0:9b}".format(bestresult['row4'])
            s225present = 1
        else:
            s225setting = "{0:9b}".format(256)

        endlist = [self.targetphase, s180present, s90present, s45present, s225present, s180setting, s90setting, s45setting, s225setting]
        table.append(endlist)

    print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    return
