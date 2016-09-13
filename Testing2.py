"""Module to work on more ideas for MPAC tuning."""
import decimal as dec
import openpyxl as xl
import extras as ex
import TwoPhase as tp
import ThreePhase as thp
import FourPhase as fp
import AttenuationSearch as ats
import lookuptablegenerator as lutg
import os
import minphasevariation as mpv


class Main:
    """Where the real magic happens."""

    def __init__(self):
        """Initialise class."""
        print("Initialising")
        print("Make sure when handing the program over that paths to directories aren't hard coded")
        self.phase24 = 1
        self.phase28 = 2
        self.phase32 = 3
        self.att24 = 4
        self.att28 = 5
        self.att32 = 6
        self.dsastate24 = 0
        self.dsas2124 = 2
        self.dsaphase2124 = 4
        self.dsastate28 = 6
        self.dsas2128 = 8
        self.dsaphase2128 = 10
        self.dsastate32 = 12
        self.dsas2132 = 14
        self.dsaphase2132 = 16
        self.targetphase = 0
        self.targetatt = 0
        self.workbook = xl.load_workbook(os.path.join(
            os.path.dirname(__file__), 'source.xlsx'))
        self.s180 = self.workbook.get_sheet_by_name('180')
        self.s90 = self.workbook.get_sheet_by_name('90')
        self.s45 = self.workbook.get_sheet_by_name('45')
        self.s225 = self.workbook.get_sheet_by_name('22.5')
        self.dsa = self.workbook.get_sheet_by_name('DSA')
        self.k = 0

    def main(self):
        """More magic."""
        dec.getcontext().prec = 6
        consent = input(
            "Would you like to calculate a specific (V)alue or generate a lookup (T)able?")
        if consent == 'V':
            minvarchoice = input(
                "Would you like to find the most (E)fficient value or the value with least (D)ifference across frequencies?")
            self.targetphase = input(
                "Please enter the desired phase shift for 28GHz")
            self.targetatt = input(
                "Please enter the desired attenuation for 28GHz")

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
            if minvarchoice == "D":
                self.k = input("How many values would you like to search?")
                minphase = mpv.minvariation(self, set180, set90, set45, set225)
                print(minphase)
            elif minvarchoice == "E":
                bestresult = ex.checkall(self, set180, set90, set45, set225)
                print(bestresult)
                bestresult2 = tp.checkall(self, set180, set90, set45, set225)
                print(bestresult2)
                bestresult3 = thp.checkall(self, set180, set90, set45, set225)
                print(bestresult3)
                bestresult4 = fp.check(self, set180, set90, set45, set225)
                print(bestresult4)
                sollist = [bestresult['total'], bestresult2['total'],
                           bestresult3['total'], bestresult4['total']]
                bestphase = ex.mostaccurate(
                    self, bestresult, bestresult2, bestresult3, bestresult4, sollist)
                bestatt = ats.attenuationsearch(self)
                print(bestatt)
            else:
                print("Not a valid option")
        elif consent == 'T':
            option = input("Generate a table for (A)ttenuation or (P)hase?")
            if option == "A":
                lutg.atttablegen(self)
            elif option == "P":
                lutg.tablegen(self)
            else:
                print("That is not an option")

TESTBENCH = Main()
TESTBENCH.main()
