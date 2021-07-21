import os
import glob
import re
from pathlib import Path
from shutil import copyfile

#Variables
skuTxtPath = "newNames.txt"
fileNameTxtPath = "oldNames.txt"
skuList = []
nameList = []
skusUsed = []
dupPrevent = 0

#Announcements
print("-------------------------------------------------------------------------------------")
print("Welcome to the image renamer tool")
print("Please fill out the configuration below to continue.")
print("Note: Please specify all filetypes.")
print("-------------------------------------------------------------------------------------\n\n\n")

#File Placement Requirements
print("-------------------------------------------------------------------------------------")
input("Please place all SKUs that you want files to be renamed after into file " + skuTxtPath + " in the same directory as this script then press any key to continue.")

## Ensure sku file
if not (os.path.isfile(skuTxtPath)):
    print("A valid sku list file was not found, program will now exit.")
    input("Press any key to exit...")
    sys.exit()
    
input("Please place all file names that match SKUs into file " + fileNameTxtPath + " in the same directory as this script then press any key to continue.")

## Ensure file name file is valid
if not (os.path.isfile(fileNameTxtPath)):
    print("A valid sku list file was not found, program will now exit.")
    input("Press any key to exit...")
    sys.exit()

## File Processing ##
    
# Open SKU file
skuFile = open(skuTxtPath, "r")

## Place all the SKUs into a list for easy access
for line in skuFile:
    lineSplit = line.split("\n")
    skuList.append(lineSplit[0])
    
skuFile.close()

# Open names file
nameFile = open(fileNameTxtPath, "r")

## Place all the names into a list matching the indecies of the previous list
for line in nameFile:
    lineSplit = line.split("\n")
    nameList.append(lineSplit[0])
    
nameFile.close()

# Show the user the files and how they will line up
print("The following output represents the first 3 file names and their corisponding SKU they will be matched to. Please ensure these are correct before proceeding otherwise the output will not be accurate.")
print("Index " + str(0) +  "| Name: " + nameList[0] + "| SKU: " + skuList[0] + "|")
print("Index " + str(1) +  "| Name: " + nameList[1] + "| SKU: " + skuList[1] + "|")
print("Index " + str(2) +  "| Name: " + nameList[2] + "| SKU: " + skuList[2] + "|")
input("\n\n Press Any Key to Continue ... \n\n")

print("Please fill out the configuration below to continue.")
print("-------------------------------------------------------------------------------------\n\n\n")

#Get desired paths
inPath = input("Please enter the root directory where all the images are located >>>")
outPath = input("Please enter the directory where all named folders should be placed. >>>")

#Verify Configuration
print("\n\n\n-------------------------------------------------------------------------------------")
print("Configuration:")
print("Parent Directory of images to be organized: " + str(inPath))
print("Target Directory to make folders in: " + str(outPath))
print("-------------------------------------------------------------------------------------\n\n\n")

imageList = os.listdir(inPath)      

totProcessed = 0

i = 0
## Loop through our list of origional file names
for name in nameList:

    ##Look for an image that matches this name
    for image in imageList:

         if (name in image):

            totProcessed = totProcessed + 1

            ##Check if the sku has been used previously
            if (skuList[i] in skusUsed):
                
                ## Move the item to output and rename using a duplicate prevention number
                copyfile(inPath + "/" + image, outPath + "/" + skuList[i] + "-" + str(dupPrevent))
                dupPrevent = dupPrevent + 1
                #continue
    
            else:
                copyfile(inPath + "/" + image, outPath + "/" + skuList[i])
                skusUsed.append(skuList[i])
    
            print("Image of name " + image + " translated to SKU " + skuList[i])
            break
        
    i = i + 1
        
print("Placed " + str(totProcessed) + " items.")
print(str(dupPrevent) + " items were found to be under the same sku and were given a unique number to compensate")
input("Press any key to exit...")
    
    
