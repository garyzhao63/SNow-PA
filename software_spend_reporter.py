from collections import defaultdict
import sys
import csv
import math

# Function to format a number to its dollar format e.g. 1234 -> $1,234
def numToDollars(amount):
    return str('${:,}'.format(amount))

# Function to truncate decimals
def truncateDecimals(amount):
    return math.trunc(amount)

####################################################################

#File name from command line
fName = sys.argv[1]

# Initialize vendorDict as a dict of dict and
# Initialize each dict in vendorDict as a dict of float
vendorDict = defaultdict(lambda: defaultdict(float))

with open(fName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        currVendor = row['Vendor']
        currProduct = row['Product']

        # add the spending of the same product to that product's total spending
        vendorDict[currVendor][currProduct] += float(row['Amount'])

## Loop through vendorDict in alphabetical order
for vendor, productDict in sorted(vendorDict.items()):
    vendorAmount = 0
    vendorStr = '' 
    productStr = ''

    ## Loop through productDict in alphabetical order
    for product, productAmount in sorted(productDict.items()):
        # Add the product spending to the vendor's total spending
        vendorAmount += productAmount;
        productStr += '  ' + product + ' ' + numToDollars(truncateDecimals(productAmount)) + '\n'

    vendorStr = vendor + ' ' + numToDollars(truncateDecimals(vendorAmount))

    # rstrip() removes the last new line
    print (vendorStr + '\n' + productStr.rstrip())
