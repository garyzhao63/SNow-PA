from collections import defaultdict
import sys
import csv

# Function to format a number to dollar format e.g. 1234 -> $1,234
def formatToDollars(amount):
    return str('${:,}'.format(amount))

######################################################

#File name from command line
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

#Loop through vendorDict in alphabetical order
for vendor, productDict in sorted(vendorDict.items()):
    vendorAmount = 0
    vendorStr = '' 
    productStr = ''

    #Loop through productDict in alphabetical order
    for product, amount in sorted(productDict.items()):
        vendorAmount += amount;
        productStr += ' ' + product + ' ' + formatToDollars(amount) + '\n'


    vendorStr = vendor + ' ' + formatToDollars(vendorAmount)

    #rstrip removes the last new line
    print (vendorStr + '\n' + productStr.rstrip())
