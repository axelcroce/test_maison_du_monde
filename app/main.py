import sys
import os
from SparseArray import SparseArray
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():


    queries = request.args.get('queries')
    
    try:
      queries = queries.split(',')
    except AttributeError:
      return("You did not pass the correct arguments")
    
    # Reading the strings from the environment variable
    strings = os.environ.get('STRINGS')
    strings = strings.split(',')

    # Create an instance of the class SparseArray and call the function matchingStrings
    sa = SparseArray(strings, queries)
    results = sa.matchingStrings()

    # Display the answer as a dict
    answer = dict(zip(queries, results))
    return(answer)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 
