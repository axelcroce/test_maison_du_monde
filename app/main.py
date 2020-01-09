import sys
import os
from SparseArray import *

if __name__ == '__main__':    
    # Reading the queries passed in argument and make a list out of the string
    queries = sys.argv[1]
    queries = queries.split(',')

    # Reading the strings from the environment variable
    strings = os.environ.get('STRINGS')
    strings = strings.split(',')

    # Create an instance of the class SparseArray and call the function matchingStrings
    sa = SparseArray(strings, queries)
    results = sa.matchingStrings()

    # Display the answer as a dict
    answer = dict(zip(queries, results))
    print(answer)