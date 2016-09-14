"""A module to find the required attenuation."""
import decimal as dec


def attlist(self):
    """Generate a list of all the values in the attenuation sheet."""
    listatt = []
    for row in self.dsa.iter_rows(row_offset=2):
        if row[self.dsas2128].value is not None:
            listatt.append(row[self.dsas2128].value)
    return listatt


def closest(self, attlist):
    """Find closest attenuation to target."""
    closest = min(attlist, key=lambda x: abs(
        dec.Decimal(x) - dec.Decimal(self.targetatt)))
    closest = dec.Decimal(closest)
    return closest


def attenuationsearch(self, attlist, closest):
    """Search for the most accurate attenuation."""
    for row in self.dsa.iter_rows():
        if row[self.dsas2128].value == closest:
            att2128 = closest.quantize(dec.Decimal(
                '.001'), rounding=dec.ROUND_HALF_UP)
            row28 = row[self.dsastate28].value
            att2124 = dec.Decimal(row[self.dsas2124].value).quantize(
                dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
            att2132 = dec.Decimal(row[self.dsas2132].value).quantize(
                dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
            phase2124 = dec.Decimal(row[self.dsaphase2124].value).quantize(
                dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
            phase2128 = dec.Decimal(row[self.dsaphase2128].value).quantize(
                dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)
            phase2132 = dec.Decimal(row[self.dsaphase2132].value).quantize(
                dec.Decimal('.001'), rounding=dec.ROUND_HALF_UP)

    return {'row28': row28, 'att2124': att2124, 'att2128': att2128, 'att2132': att2132, 'phase2124': phase2124, 'phase2128': phase2128, 'phase2132': phase2132}
