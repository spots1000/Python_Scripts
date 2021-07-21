import os
import glob
import re
from pathlib import Path
from shutil import copyfile
import codecs
import sys

#Variables
textPath = "in.txt"
outPath = "out.txt"
weightList = []


# text file config
input("Please place all dimensions, one set of dimensions per line, into file '" + textPath + "' and then press any key to proceed.")

## Ensure before opening text file that we have a valid file to read.
if not (os.path.isfile(textPath)):
    print("A valid list file was not found, program will now exit.")
    input("Press any key to exit...")
    sys.exit()    
    
textFile = open(textPath, encoding="utf8")

## Make sure our output file is cleared
outFile = open(outPath, "w")
outFile.close()

print("Begining Processing...")

## Read the entire text file
for line in textFile:

    if (line == "\n"):
        continue
    
    totalWeight = 0
    
    ## split the line first by pipes
    indivDims = line.split("|")

    ## Run through the dims
    for dim in indivDims:
        splitDim = dim.split(";")
        print(splitDim )

        try:
            weight = int(splitDim[1])
        except:
            continue

        print("Data to enter - " + str(weight))
        totalWeight = totalWeight + weight 

    ## Add this to our weight list
    weightList.append(totalWeight)

textFile.close()

print("Reached EOF, processing remainder")

##Open the output file
outFile = open(outPath, "a")

##Output each weight
for txt in weightList:
    outFile.write(str(txt) + "\n")

## Close the output file
outFile.close()

##Final output
print("All processing completed. ")
input("Press any key to exit...")
sys.exit()
