"""Module to find minimum attenuation variation across frequency."""
import decimal as dec
from heapq import nsmallest
import AttenuationSearch as ats


def minattvar(self):
    """Search for minimum amplitude variation across frequency."""
    listatt = []
    totallist = []
    attvar = []
    for row in self.dsa.iter_rows(row_offset=2):
        if row[self.dsas2128].value is not None:
            listatt.append(row[self.dsas2128].value)
    closest_values = nsmallest(int(self.k), listatt, key=lambda x: abs(
        dec.Decimal(x) - dec.Decimal(self.targetatt)))
    closest = [dec.Decimal(i) for i in closest_values]
    print(closest)
    for i in closest:
        resultsdict = ats.attenuationsearch(self, listatt, i)
        variation = resultsdict['att2132'] - resultsdict['phase2124']
        resultsdict['variation'] = variation
        totallist.append(resultsdict)
        attvar.append(variation)

    print(totallist)
    print(attvar)
    minattdiff = min(abs(i) for i in attvar)
    for m in totallist:
        if abs(m['variation']) == minattdiff:
            return m
