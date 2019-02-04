import sys
import csv

#command line argument 
fName = sys.argv[1]

vendorDict = {}

with open(fName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        currVendor = row['Vendor']
        vendorDict[currVendor] = 
        print vendorDict[currVendor]


         

