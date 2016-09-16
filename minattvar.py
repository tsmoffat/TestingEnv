"""Module to find minimum attenuation variation across frequency."""
import decimal as dec
from heapq import nsmallest
import AttenuationSearch as ats


def minattvar(self):
    """Search for minimum amplitude variation across frequency."""
    listatt = []
    totallist = []
    attvar = []
    # Iterates through all the rows in the spreadsheet from the third row
    # onwards
    for row in self.dsa.iter_rows(row_offset=2):
        if row[self.dsas2128].value is not None:
            # Adds the value to a list if it actually has a value, and isn't
            # blank
            listatt.append(row[self.dsas2128].value)
    closest_values = nsmallest(int(self.k), listatt, key=lambda x: abs(
        dec.Decimal(x) - dec.Decimal(self.targetatt)))  # Finds the k closest numbers to a given value from the list
    # Converts the values in closest_values to a decimal from a float. This
    # makes it easier to work with as it adds in rounding
    closest = [dec.Decimal(i) for i in closest_values]
    print(closest)
    for i in closest:
        # Calls the AttenuationSearch module to search for the various values.
        # It does this for each item in the closest list
        resultsdict = ats.attenuationsearch(self, listatt, i)
        variation = resultsdict['att2132'] - resultsdict['phase2124']
        # Adds a new value to the dictionary, with the key variation
        resultsdict['variation'] = variation
        totallist.append(resultsdict)
        attvar.append(variation)
    print(totallist)
    print(attvar)
    # Finds the smallest number in the list
    minattdiff = min(abs(i) for i in attvar)
    for m in totallist:
        if abs(m['variation']) == minattdiff:
            # If the value in the dictionary/key combo m['variation'] matches
            # the minimum value, it gets returned and printed
            return m
