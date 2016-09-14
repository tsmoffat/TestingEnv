"""Find the minimum insertion loss, i.e., the minimum attenuation for a given phase."""
import decimal as dec
import os
from heapq import nsmallest
import FourPhase as fp


def mininsertloss(self, set180, set90, set45, set225):
    """Find minimum insertion loss for a phase."""
    dec.getcontext().prec = 6
    combined = set(map(dec.Decimal, open((os.path.join(
        os.path.dirname(__file__), '1809045225.txt')))))
    closest_values = nsmallest(int(self.k), combined, key=lambda x: abs(
        x - dec.Decimal(self.targetphase)))
    closest = [dec.Decimal(i) for i in closest_values]
    total_values = []
    insertlosslist = []
    del combined
    for item in closest:
        resultsdict = fp.check(self, set180, set90, set45, set225, item)
        insertlosslist.append(resultsdict['totalatt'])
        total_values.append(resultsdict)
    print(total_values)
    mininsertloss = min(abs(i) for i in insertlosslist)
    for m in total_values:
        print(m['totalatt'])
        if abs(m['totalatt']) == mininsertloss:
            return m
