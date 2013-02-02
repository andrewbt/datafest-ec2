# August Guang, February 2013
# corpSearch.py
# Takes in an input term (corporation name) and scrapes the InfluenceExplorer
# API to pull out all relevant information (does not format)

# to run: python corpSearch.py -i <input>

import sys, getopt
import requests
import pprint
import urllib2

def main(argv):
    i = ''
    out = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:", ["input="])
    except getopt.error, msg:
        print "corpSearch.py -i <input> -o <output>"
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "-input"):
            i = arg
#        elif opt in ("-o", "-output"):
#            out = arg

    query_params = { 'apikey' : '8f0d91c66d4e428da018c0eb0fa571fc',
                     'per_page': 3,
                 'phrase' : i
                     }

    endpoint = "http://transparencydata.com/api/1.0/contributions.json"

    response = requests.get( endpoint, params=query_params)
    data = response.json()    

    pprint.pprint(data)

if __name__ == "__main__":
    main(sys.argv[1:])
