import math
import os
import random
import re
import sys

class SparseArray :

    def __init__(self, strings, queries):
        self.strings = strings
        self.queries = queries


    def matchingStrings(self):
        """
        Return an Array containing the number of times each element of the queries appear in the strings
        """
        results = []
        for query in self.queries:
            count = self.strings.count(query)
            results.append(count)
        return results
