import openpyxl as xl

class main:
    def __init__(self):
        print("Initialising")

    def main(self):
        wb = xl.load_workbook("Five RF Sections - Relative Effects.xlsx")
        s180 = wb.get_sheet_by_name('180')
        s90 = wb.get_sheet_by_name('90')
        s45 = wb.get_sheet_by_name('45')
        s225 = wb.get_sheet_by_name('225')

        nb = input("What frequency are you using?")
        while nb != "24GHz" and nb != "28GHz" and nb != "32GHz":
            nb = input('Sorry, that is not a valid frequency, please enter 24GHz, 28GHz or 32GHz')
            print(nb)
        if (nb == '24GHz'):
            phase = 1
            Att = 5
            DSAState = 1
            DSAS11 = 2
            DSAS21 = 3
            DSAS22 = 4
        elif (nb == '28GHz'):
            phase = 2
            Att = 6
            DSAState = 6
            DSAS11 = 7
            DSAS21 = 8
            DSAS22 = 9
        elif (nb == '32GHz'):
            phase = 3
            Att = 7
            DSAState = 11
            DSAS11 = 12
            DSAS21 = 13
            DSAS22 = 14
        else:
            phase = 0
            Att = 0
            DSAState = 0
            DSAS11 = 0
            DSAS21 = 0
            DSAS22 = 0

        list180 = []
        for row in s180.iter_rows(row_offset=2):
            if (row[phase].value != None):
                print(row[phase].value)
                list180.append(float(row[phase].value))

        list90 = []
        for row in s90.iter_rows(row_offset=2):
            if (row[phase].value != None):
                print(row[phase].value)
                list90.append(float(row[phase].value))

        list45 = []
        for row in s45.iter_rows(row_offset=2):
            if (row[phase].value != None):
                print(row[phase].value)
                list45.append(float(row[phase].value))

        list225 = []
        for row in s225.iter_rows(row_offset=2):
            if (row[phase].value != None):
                print(row[phase].value)
                list225.append(float(row[phase].value))