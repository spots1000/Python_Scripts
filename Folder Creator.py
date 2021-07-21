import os
import glob
from shutil import copyfile
import re
from pathlib import Path
import sys

#Variables
textPath = "in.txt"
folderNames = []
processAll = 0

#Announcements
print("-------------------------------------------------------------------------------------")
print("Welcome to the folder creation tool!")
print("This tool generates a number of empty folders in a given directory based on a supplied list.")
print("Please fill out the configuration below to continue.")
print("-------------------------------------------------------------------------------------\n\n\n")

# text file config
input("Please place a list of folder names in a file named '" + textPath + "' and then press any key to proceed.")

## Ensure before opening text file that we have a valid file to read.
if not (os.path.isfile(textPath)):
    print("A valid list file was not found, program will exit.")
    sys.exit()

else:
    
    textFile = open(textPath, "r")

    ## Place all the MPN numbers
    for line in textFile:
        lineSplit = line.split("\n")
        folderNames.append(lineSplit[0])
    
    textFile.close()
    
#Get desired paths
outPath = input("Please enter the directory where all folders should be placed >>>")

#Check for a blank dicectory
if (outPath == ""):
    yesNo = input("Please confirm that you would like to place all folders on the C Drive base folder of this machine ( Y / N ) >>>")
    if (yesNo == "N" or yesNo == "n"):
        print("Wrong file path entered, program will now exit.")
        input("Press any key to exit...")
        sys.exit()
    
#Verify Configuration
print("\n\n\n-------------------------------------------------------------------------------------")
print("Please verify the following configuration information:")
print("Target Folder or Directory to place images in: " + str(outPath))
print("-------------------------------------------------------------------------------------\n\n\n")

# Create folders
for name in folderNames:

    print("Trying to place folder " + name)
    
    ##check if a folder exists and create one if not
    Path(outPath + "/" + name).mkdir(parents=True, exist_ok=True)

print("The program has created all folders possible. \n\n")
input("Press any key to exit...")


