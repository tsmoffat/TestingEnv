"""Module to work on more ideas for MPAC tuning"""
import decimal as dec
import openpyxl as xl
import extras as ex
import TwoPhase as tp
import ThreePhase as thp
import FourPhase as fp
import AttenuationSearch as ats


class Main:
    """Where the real magic happens"""

    def __init__(self):
        print("Initialising")
        self.phase24 = 1
        self.phase28 = 2
        self.phase32 = 3
        self.att24 = 4
        self.att28 = 5
        self.att32 = 6
        self.dsastate24 = 0
        self.dsas2124 = 2
        self.dsastate28 = 5
        self.dsas2128 = 7
        self.dsastate32 = 10
        self.dsas2132 = 12
        self.targetphase = 0
        self.targetatt = 0
        self.workbook = xl.load_workbook("Five RF Sections - Relative Effects.xlsx")
        self.s180 = self.workbook.get_sheet_by_name('180')
        self.s90 = self.workbook.get_sheet_by_name('90')
        self.s45 = self.workbook.get_sheet_by_name('45')
        self.s225 = self.workbook.get_sheet_by_name('22.5')


    def main(self):
        """More magic"""
        dec.getcontext().prec = 6

        self.targetphase = input("Please enter the desired phase shift for 28GHz")
        self.targetatt = input("Please enter the desired attenuation for 28GHz")

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

        bestresult = ex.checkall(self, set180, set90, set45, set225)
        print(bestresult)
        bestresult2 = tp.checkall(self, set180, set90, set45, set225)
        print(bestresult2)
        bestresult3 = thp.checkall(self, set180, set90, set45, set225)
        print(bestresult3)
        bestresult4 = fp.check(self, set180, set90, set45, set225)
        print(bestresult4)
        sollist = [bestresult['total'], bestresult2['total'], bestresult3['total'], bestresult4['total']]
        bestphase = ex.mostaccurate(self, bestresult, bestresult2, bestresult3, bestresult4, sollist)
        bestatt = ats.attenuationsearch(self, bestphase)
        print(bestatt)



TESTBENCH = Main()
TESTBENCH.main()
