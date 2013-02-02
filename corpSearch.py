# August Guang, February 2013
# corpSearch.py
# Takes in an input term (corporation name) and scrapes the InfluenceExplorer

# to run: python corpSearch.py -i <input>

from influenceexplorer import InfluenceExplorer
from dict2xml import dict2xml
import sys, getopt
import requests
import pprint
import itertools

api = InfluenceExplorer('8f0d91c66d4e428da018c0eb0fa571fc')

def readIn(inFile):
    with open(inFile, 'r') as fin:
        # format is:
        # Catcode Catname Catorder Industry Sector Sector_Long
        tmp = fin.readlines()
        sectData = tmp[1:]

def sectorDict(sectData):
    sectDict = {}
    for i in sectData:
        sector = i.split()[4]
        code = i.split()[0]
        if sector in sectDict:
            sectDict[sector].append(code)
        else:
            sectDict[sector] = [code]
    return sectDict

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

    sectData = readIn("CRP_Categories.txt")
    sectDict = sectorDict(sectData)
    print sectDict

    pprint.pprint(data)

if __name__ == "__main__":
    main(sys.argv[1:])
