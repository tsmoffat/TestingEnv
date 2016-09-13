"""A module to find the required attenuation."""
import decimal as dec


def attenuationsearch(self):
    """Search for the most accurate attenuation."""
    satt = self.workbook.get_sheet_by_name("DSA")
    print(self.targetatt)
    listatt = []
    for row in satt.iter_rows(row_offset=2):
        if row[self.dsas2128].value is not None:
            listatt.append(row[self.dsas2128].value)
    if self.targetatt in listatt:
        for row in satt.iter_rows():
            if row[self.dsas2128].value == self.targetatt:
                row28 = row[self.dsastate28].value
                att2128 = self.targetphase.quantize(
                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                att2124 = dec.Decimal(row[self.dsas2124].value).quantize(
                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                att2132 = dec.Decimal(row[self.dsas2132].value).quantize(
                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)

        return {'row28': row28, 'att2124': att2124, 'att2128': att2128, 'att2132': att2132}
    else:
        closest = min(listatt, key=lambda x: abs(
            dec.Decimal(x) - dec.Decimal(self.targetatt)))
        closest = dec.Decimal(closest)
        for row in satt.iter_rows():
            if row[self.dsas2128].value == closest:
                att2128 = closest.quantize(dec.Decimal(
                    '.001'), rounding=dec.ROUND_HALF_UP)
                row28 = row[self.dsastate28].value
                att2124 = dec.Decimal(row[self.dsas2124].value).quantize(
                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
                att2132 = dec.Decimal(row[self.dsas2132].value).quantize(
                    dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)

        return {'row28': row28, 'att2124': att2124, 'att2128': att2128, 'att2132': att2132}
