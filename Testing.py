import openpyxl as xl
from decimal import *


class Main:
    def __init__(self):
        print("Initialising")

    def main(self):
        getcontext().prec=6
        workbook = xl.load_workbook("Five RF Sections - Relative Effects.xlsx")
        s180 = workbook.get_sheet_by_name('180')
        s90 = workbook.get_sheet_by_name('90')
        s45 = workbook.get_sheet_by_name('45')
        s225 = workbook.get_sheet_by_name('22.5')

        frequency = input("What frequency are you using?")
        while frequency != "24GHz" and frequency != "28GHz" and frequency != "32GHz":
            frequency = input(
                'Sorry, that is not a valid frequency, please enter 24GHz, 28GHz or 32GHz')

        if (frequency == '24GHz'):
            phase = 1
            att = 5
            DSAState = 1
            DSAS11 = 2
            DSAS21 = 3
            DSAS22 = 4
        elif (frequency == '28GHz'):
            phase = 2
            att = 6
            DSAState = 6
            DSAS11 = 7
            DSAS21 = 8
            DSAS22 = 9
        elif (frequency == '32GHz'):
            phase = 3
            att = 7
            DSAState = 11
            DSAS11 = 12
            DSAS21 = 13
            DSAS22 = 14
        else:
            phase = 0
            att = 0
            DSAState = 0
            DSAS11 = 0
            DSAS21 = 0
            DSAS22 = 0

        list180 = []
        for row in s180.iter_rows(row_offset=2):
            if (row[phase].value != None):
                list180.append(Decimal(row[phase].value))
        set180 = set(list180)
        list90 = []
        for row in s90.iter_rows(row_offset=2):
            if (row[phase].value != None):
                list90.append(Decimal(row[phase].value))
        set90 = set(list90)
        list45 = []
        for row in s45.iter_rows(row_offset=2):
            if (row[phase].value != None):

                list45.append(Decimal(row[phase].value))
        set45 = set(list45)
        list225 = []
        for row in s225.iter_rows(row_offset=2):
            if row[phase].value != None:

                list225.append(Decimal(row[phase].value))
        set225 = set(list225)
        targetphase = Decimal(input("What phase do you want to achieve?"))
        targetatt = input("What attenuation do you want to achieve?")
        if targetphase in set180:
            print("Found it!")
            for row in s180.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att180 = Decimal(row[att].value)
            print("Optimal solution found, it is state " + str(optimalrow))
            print(att180)

        elif targetphase in set90:
            print("Found it!")
            for row in s90.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att90 = Decimal(row[att].value)
            print("Optimal solution found, it is state " + str(optimalrow))
            print(att90)

        elif targetphase in set45:
            print("Found it!")
            for row in s45.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att45 = Decimal(row[att].value)
            print("Optimal solution found, it is state " + str(optimalrow))
            print(att45)

        elif targetphase in set225:
            print("Found it!")
            for row in s225.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att225 = Decimal(row[att].value)
            print("Optimal solution found, it is state " + str(optimalrow))
            print(att225)

        else:
            sum2 = two_element_sum(s180, s90, s45, s225, set180, set90, set45, set225, targetphase, phase, att)
            sum2.Two_element_sum()




class two_element_sum(Main):
    def __init__(self, s180, s90, s45, s225, set180, set90, set45, set225, targetphase, phase, att):
        getcontext().prec=6
        self.s180 = s180
        self.s90 = s90
        self.s45 = s45
        self.s225 = s225
        self.set180 = set180
        self.set90 = set90
        self.set45 = set45
        self.set225 = set225
        self.targetphase = targetphase
        self.phase = phase
        self.att = att
    def Two_element_sum(self):
        getcontext().prec = 6
        for i in self.set180:
            for j in self.set90:

                result = i+j
                if result == self.targetphase:
                    solution1 = i
                    solution2 = j
                    print("Found it!")
                    for row in self.s180.iter_rows():
                        if row[self.phase].value == i:
                            row180 = int(row[0].value)
                            att180 = Decimal(row[self.att].value)
                            print(row180)
                            print(att180)

                    for row in self.s90.iter_rows():
                        if row[self.phase].value == j:
                            row90 = int(row[0].value)
                            att90 = Decimal(row[self.att].value)
                            print(row90)
                            print(att90)

        for i in self.set180:
            for j in self.set45:
                result = i+j
                if result == self.targetphase:
                    solution1 = i
                    solution2 = j
                    print("Found it!")
                    for row in self.s180.iter_rows():
                        if row[self.phase].value ==i:
                            row180 = int(row[0].value)
                            att180 = Decimal(row[self.att].value)
                            print(row180)
                            print(att180)

                    for row in self.s45.iter_rows():
                        if row[self.phase].value == j:
                            row45 = int(row[0].value)
                            att45 = Decimal(row[self.att].value)
                            print(row45)
                            print(att45)

        for i in self.set180:
            for j in self.set225:
                result = i+j
                if result == self.targetphase:
                    solution1 = i
                    solution2 = j
                    print("Found it!")
                    for row in self.s180.iter_rows():
                        if row[self.phase].value ==i:
                            row180 = int(row[0].value)
                            att180 = Decimal(row[self.att].value)
                            print(row180)
                            print(att180)




m = Main()
m.main()