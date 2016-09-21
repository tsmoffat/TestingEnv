"""A module to find the minimum variation in phase across frequency"""
import decimal as dec
from heapq import nsmallest
from src import AttenuationSearch as ats


def minampvar(self):
    """Search for minimum variation in phase across attenuation frequency."""
    listatt = []
    totallist = []
    ampvar = []
    for row in self.dsa.iter_rows(row_offset=2):
        if row[self.dsas2128].value is not None:
            listatt.append(row[self.dsas2128].value)
    closest_values = nsmallest(int(self.k), listatt, key=lambda x: abs(
        dec.Decimal(x) - dec.Decimal(self.targetatt)))
    closest = [dec.Decimal(i) for i in closest_values]
    for i in closest:
        resultsdict = ats.attenuationsearch(self, listatt, i)
        # Finds total variation in phase
        variation = resultsdict['phase2132'] - resultsdict['phase2124']
        resultsdict['variation'] = variation
        totallist.append(resultsdict)
        ampvar.append(variation)
    minampdiff = min(abs(i) for i in ampvar)
    for m in totallist:
        if abs(m['variation']) == minampdiff:
            return m  # Returns the dictionary with the minimum phase variation in it
