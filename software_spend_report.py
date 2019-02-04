from collections import defaultdict
import sys
import csv

#command line argument 
fName = sys.argv[1]

# Initialize vendorDict to a dict of dict, 
# and initialize each dict in vendorDict to a dict of int
vendorDict = defaultdict(lambda: defaultdict(int))

with open(fName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        currVendor = row['Vendor']
        currProduct = row['Product']

        #add the spending to the current spending
        vendorDict[currVendor][currProduct] += int(row['Amount'])


print vendorDict

