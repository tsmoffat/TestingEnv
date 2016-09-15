"""Module to find setting with minimum variation across phases."""
import decimal as dec
import os
from heapq import nsmallest
import FourPhase as fp


def minvariation(self, set180, set90, set45, set225):
    """Find the closest value with the least variation across frequency."""
    dec.getcontext().prec = 6
    combined = set(map(dec.Decimal, open(
        (os.path.join(os.path.dirname(__file__), '1809045225.txt')))))  # Gets the path to the directory that the program is running in
    closest_values = nsmallest(int(self.k), combined, key=lambda x: abs(
        x - dec.Decimal(self.targetphase)))
    closest = [dec.Decimal(i) for i in closest_values]
    print(closest)
    total_values = []
    phasedifflist = []
    del combined
    for item in closest:
        resultsdict = fp.check(self, set180, set90, set45, set225, item)
        totalphasediff = resultsdict['phasediff1'] + resultsdict[
            'phasediff2'] + resultsdict['phasediff3'] + resultsdict['phasediff4']
        resultsdict['totalphasediff'] = totalphasediff
        phasedifflist.append(totalphasediff)
        total_values.append(resultsdict)
    print(total_values)
    minphasediff = min(phasedifflist)
    for m in total_values:
        print(m['totalphasediff'])
        if m['totalphasediff'] == minphasediff:
            return m
