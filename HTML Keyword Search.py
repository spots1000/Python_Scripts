import os
import glob
import re

#Variables
fullImgList = "in.txt"
output = "out.txt"
fileNames = []
goodFiles = []
searchString = "Order #:"

#Announcements
print("-------------------------------------------------------------------------------------")
print("Welcome to the html finder tool")
print("This tool can help to find a specific html or phtml file by searching for a given keyword. This tool is not intended to be used without editing the source code.")
print("Please fill out the configuration below to continue.")
print("-------------------------------------------------------------------------------------\n\n\n")


#File Placement Requirements
print("-------------------------------------------------------------------------------------")
input("Please place a list of all html files into " + fullImgList + " in the same directory as this script then press any key to continue.")

## Ensure list file is present
if not (os.path.isfile(fullImgList)):
    print("A valid sku list file was not found, program will now exit.")
    input("Press any key to exit...")
    sys.exit()
    
#Open html list file
listFile = open(fullImgList, "r")

## Read in the target list file
for line in listFile:
    lineSplit = line.split("\n")
    fileNames.append(lineSplit[0])
    print(lineSplit[0])
    
listFile.close()

#Get desired paths
inPath = input("Please enter the root directory where all the images are located >>>")

#Verify Configuration
print("\n\n\n-------------------------------------------------------------------------------------")
print("Configuration:")
print("Parent Directory of images to be organized: " + str(inPath))
print("Output results will be listed in file " + str(output) + " in the same directory as this script.")
print("Search key: [" + str(searchString) + "] will be used for this search. If you want to change this please edit searchString in the source file.")
print("-------------------------------------------------------------------------------------\n\n\n")

#Begin looping
for file in fileNames:

    print("Reading File [" + str(file) + "]")

    #Open individual html file
    htmlFile = open(inPath + "/" + file, "r")

    ## Read each line, checking for the target words
    for line in htmlFile:
        lineSplit = line.split("\n")
        
        if(searchString in lineSplit[0]):
            goodFiles.append(file)
            print("File had the desired key.")
            break;

#Open Output File
outFile = open(output, "w")

for good in goodFiles:
    outFile.write(good)

outFile.close()
print("File output completed.")
