# August Guang, February 2013
# corpSearch.py
# Takes in an input term (corporation name) and scrapes the InfluenceExplorer

# to run: python corpSearch.py -i <input>

from influenceexplorer import InfluenceExplorer
from dict2xml import dict2xml
import sys, getopt
import requests
import pprint

api = InfluenceExplorer('8f0d91c66d4e428da018c0eb0fa571fc')

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
    data = api.entities.search(i)
#    tmp = dict2xml(data)
    pprint.pprint(data)

if __name__ == "__main__":
    main(sys.argv[1:])
