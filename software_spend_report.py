from collections import defaultdict
import sys
import csv
import math

# Function to format a number to dollar format e.g. 1234 -> $1,234
def numToDollars(amount):
    return str('${:,}'.format(amount))

# Function to truncate decimals
def truncateDecimals(amount):
    return math.trunc(amount)

# Function to parse a row and insert it into the dict
def insertRowToDict(row):
    currVendor = row['Vendor']
    currProduct = row['Product']

    #add the spending to the current spending
    vendorDict[currVendor][currProduct] += float(row['Amount'])

######################################################

#File name from command line
fName = sys.argv[1]

# Initialize vendorDict to a dict of dict, 
# and initialize each dict in vendorDict to a dict of int
vendorDict = defaultdict(lambda: defaultdict(float))

with open(fName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        insertRowToDict(row)

#Loop through vendorDict in alphabetical order
for vendor, productDict in sorted(vendorDict.items()):
    vendorAmount = 0
    vendorStr = '' 
    productStr = ''

    #Loop through productDict in alphabetical order
    for product, amount in sorted(productDict.items()):
        vendorAmount += amount;
        productStr += ' ' + product + ' ' + numToDollars(truncateDecimals(amount)) + '\n'


    vendorStr = vendor + ' ' + numToDollars(truncateDecimals(vendorAmount))

    #rstrip removes the last new line
    print (vendorStr + '\n' + productStr.rstrip())
