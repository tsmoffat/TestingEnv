import openpyxl as xl

class main:
    def __init__(self):
        print("Initialising")

    def main(self):
        wb = xl.load_workbook("Five RF Sections - Relative Effects.xlsx")
        s180 = wb.get_sheet_by_name('180')
        s90 = wb.get_sheet_by_name('90')
        s45 = wb.get_sheet_by_name('45')
        s225 = wb.get_sheet_by_name('22.5')

        nb = input("What frequency are you using?")
        while nb != "24GHz" and nb != "28GHz" and nb != "32GHz":
            nb = input('Sorry, that is not a valid frequency, please enter 24GHz, 28GHz or 32GHz')
            print(nb)
        if (nb == '24GHz'):
            phase = 1
            att = 5
            DSAState = 1
            DSAS11 = 2
            DSAS21 = 3
            DSAS22 = 4
        elif (nb == '28GHz'):
            phase = 2
            att = 6
            DSAState = 6
            DSAS11 = 7
            DSAS21 = 8
            DSAS22 = 9
        elif (nb == '32GHz'):
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
                list180.append(float(row[phase].value))
        set180 = set(list180)
        list90 = []
        for row in s90.iter_rows(row_offset=2):
            if (row[phase].value != None):
                list90.append(float(row[phase].value))
        set90 = set(list90)
        list45 = []
        for row in s45.iter_rows(row_offset=2):
            if (row[phase].value != None):

                list45.append(float(row[phase].value))
        set45 = set(list45)
        list225 = []
        for row in s225.iter_rows(row_offset=2):
            if (row[phase].value != None):

                list225.append(float(row[phase].value))
        set225 = set(list225)
        targetphase = float(input("What phase do you want to achieve?"))
        targetatt = input("What attenuation do you want to achieve?")
        if targetphase in set180:
            print("Found it!")
            for row in s180.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att180 = float(row[att].value)
            print("Optimal solution found, it is state " + str(optimalrow))
            print(att180)

        elif targetphase in set90:
            print("Found it!")
            for row in s90.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att90 = float(row[att].value)
            print("Optimal solution found, it is state " + str(optimalrow))
            print(att90)
        elif targetphase in set45:
            print("Found it!")
            for row in s45.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att45 = float(row[att].value)
            print("Optimal solution found, it is state "  + str(optimalrow))
            print(att45)

        elif targetphase in set225
            print("Found it!")
            for row in list225.iter_rows():
                if row[phase].value == targetphase:
                    optimalrow = int(row[0].value)
                    att225 = float(row[att].value)
            print("Optimal solution found, it is state " + str(optimalrow))
            print(att225)


        else:
            print("Not found")


    def twoelementsum(self, ):


m = main()
m.main()
