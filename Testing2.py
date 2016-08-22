"""Module to work on more ideas for MPAC tuning"""
from decimal import Decimal, getcontext
import openpyxl as xl


class Main:
    """Where the real magic happens"""

    def __init__(self):
        print("Initialising")
        self.phase24 = 1
        self.phase28 = 2
        self.phase32 = 3
        self.att24 = 5
        self.att28 = 6
        self.att32 = 7
        self.dsastate24 = 1
        self.dsas2124 = 3
        self.dsastate28 = 6
        self.dsas2128 = 8
        self.dsastate32 = 11
        self.dsas2132 = 13
        self.targetphase = 0
        self.targetatt = 0

    def main(self):
        """More magic"""
        getcontext().prec = 6
        workbook = xl.load_workbook("Five RF Sections - Relative Effects.xlsx")
        s180 = workbook.get_sheet_by_name('180')
        s90 = workbook.get_sheet_by_name('90')
        s45 = workbook.get_sheet_by_name('45')
        s225 = workbook.get_sheet_by_name('225')

        self.targetphase = input("Please enter the desired phase shift for 28GHz")
        self.targetatt = input("Please enter the desired attenuation for 28GHz")

        list180 = []
        for row in s180.iter_rows(row_offset=2):
            if row[self.phase28].value is not None:
                list180.append(Decimal(row[self.phase28].value))
        set180 = set(list180)

        list90 = []
        for row in s90.iter_rows(row_offset=2):
            if row[self.phase28].value is not None:
                list90.append(Decimal(row[self.phase28].value))
        set90 = set(list90)

        list45 = []
        for row in s45.iter_rows(row_offset=2):
            if row[self.phase28].value is not None:
                list45.append(Decimal(row[self.phase28].value))
        set45 = set(list45)

        list225 = []
        for row in s225.iter_rows(row_offset=2):
            if row[self.phase28].value is not None:
                list225.append(Decimal(row[self.phase28].value))
        set225 = set(list225)

    def check180(self, s180, set180):
        """180 degrees of magic"""
        if self.targetphase in set180:
            print("Found it!")
            for row in s180.iter_rows():
                if row[self.phase28].value == self.targetphase:
                    row1 = int(row[0].value)
                    att1 = Decimal(row[self.att28].value)

            print("Optimal solution found, it is state " + str(row1))
            print(att1)
            return{'row1': row1, 'att1': att1}
        else:
            closest = min(set180, key=lambda x: abs(x - self.targetphase))
            for row in s180.iter_rows:
                if row[phase].value == closest:
                    
