from collections import defaultdict
import sys
import csv

#command line argument 
fName = sys.argv[1]

vendorDict = defaultdict(dict)
#vendorDict = {}

with open(fName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        currVendor = row['Vendor']
        currProduct = row['Product']

        print row['Amount']

        vendorDict[currVendor][currProduct] = row['Amount']


print vendorDict

