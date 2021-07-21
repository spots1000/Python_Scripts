from zipfile import ZipFile
import sys
import os

#Variables
textPath = "in.txt"
outPath = "out.txt"


## Announcements
print("Welcome to the Zip Finder Program!")
print("This program will take a supplied zip file and locate within said file any single item matching the strings placed in an accompanying text file.")
input("To use this program please place the desired skus or other identifies in a folder called \"" + textPath + "\" and then press Enter to continue.\n")

## Ensure before opening text file that we have a valid file to read.
if not (os.path.isfile(textPath)):
    print("A valid text file was not found, program will now exit.")
    input("Press any key to exit...")
    sys.exit()

## Attempt to open our text file and read in the data
targetList = []
textFile = open(textPath, encoding="utf8")

for line in textFile:

    strippedLine = line.strip("\n")
    strippedLine = strippedLine.strip("\t")
    targetList.append(strippedLine)

print("Text File successfully read in with " + str(len(targetList)) + " items.")
textFile.close()

## Get the filename
fileName = input("Please enter the name of the zip file without any extensions. >>>")
fileName = fileName + ".zip"

## Make sure the file exists
try:
    zip = ZipFile(fileName, 'r')
except:
    print("Zip File Was Not Opened Successfully")
    print("Program will exit")
    sys.exit()

print("Zip file was read successfully, processing will now comence")

## Read the zip file
fileData = zip.infolist()
errorList = []

## Loop through the data for the relevant
for target in targetList:
    print("Attemtping to locate " + target)
    found = "false"
    
    for dat in fileData:
        if (target in dat.filename):
            print("Located target file")
            path = zip.extract(dat)
            found = "true"
            break;

    if(found == "false"):
        print("Target was not found.")
        errorList.append(target)

## output to the output file
outFile = open(outPath, "a")

for err in errorList:
    outFile.write(err + "\n")

outFile.close()

i = len(targetList) - len(errorList)

##Final output
print("All processing completed. " + str(i) + " total folders successfully processed while " + str(len(errorList)) + " folders were not able to be found.")
input("Press any key to exit...")
sys.exit()


    
        
        
