import os
import sys

textPath = "in.txt"
outPath = "missing.txt"
manuStr = ""

skuList = []
missingList = []

numSKUs = 0
numImages = 0
numMatches = 0
numMissing = 0

## Anouncements
print("Welcome to the missing image identifier tool!")
print("The purpose of this tool is to compare all images in a selected directory with the file names listed in a text file and determine if any are missing.")
print("A manfuacturer part number should be supplied so that it can be removed from the output of the program.")

input("Please place a list of SKUs in a text file called '" + textPath + "' and then press any key to proceed.")

## Ensure before opening text file that we have a valid file to read.
if not (os.path.isfile(textPath)):
    print("A valid list file was not found, program will now exit.")
    input("Press any key to exit...")
    sys.exit()
    
textFile = open(textPath, "r")

## Place all the SKUs into a list for easy access
for line in textFile:
    lineSplit = line.split("\n")
    skuList.append(lineSplit[0])
    numSKUs = numSKUs + 1
    
textFile.close()

print("Total number of SKUs imported: " + str(numSKUs+1))

## Check for a manufacturer number so we can split the output properly.
newManu = input("Please enter the manufacturer number that the images use so that it can be removed from the missing output. >>>")

if (newManu != ""):
    manuStr = newManu
else:
    print("No manufacturer number was entered so no splitting of the output will occur.")

## Pull in the current directory
imgList = os.listdir()
numImages = len(imgList)
print("Number of items in this directory: " + str(numImages))

## Loop through SKUs to find ones without a match.
i = 0
for item in skuList:

    j = 0
    matchFound = 0
    for img in imgList:


        if (item in imgList[j]):
            numMatches = numMatches + 1
            matchFound = 1
            break;

        j = j+1
    
    if (matchFound == 0):
        numMissing = numMissing + 1
        missingList.append(item)
        

print("Search complete! " + str(numMatches) + " Matches were found while " + str(numMissing) + " items were not")

outFile = open(outPath, "w")

## Write statistics to out file for further reference
outFile.write("Total number of SKUs that were looked for: " + str(len(skuList)) + "\n")
outFile.write("Total number of items in the target directory: " + str(numImages) + "\n")
outFile.write("Total number of matches found: " + str(numMatches) + "\n")
outFile.write("Total number of missing items: " + str(numMissing) + "\n")
outFile.write("\n\n\n")

for item in missingList:

    if not(manuStr == ""):
        cnt = len(manuStr)+1
        outFile.write(item[cnt:] + "\n")
    else:
        outFile.write(item + "\n")
        
outFile.close()
print("Missing SKUs logged in file " + str(outPath) + ".")
input("Press any key to exit...")
