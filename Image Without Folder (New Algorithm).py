import os
import glob
import re
from pathlib import Path
from shutil import copyfile

#Announcements
print("-------------------------------------------------------------------------------------")
print("Welcome to the image without folder tool!")
print("The purpose of this tool is to take images named after an MPN and a non-standard delimeter system and place them into folders named after the MPN.")
print("The suggested workflow is to use this tool first and then use the Image In Folder tool to name all images properly with the standard convention.")
print("Please fill out the configuration below to continue.")
print("-------------------------------------------------------------------------------------\n\n\n")

#Get desired paths
inPath = input("Please enter the root directory where all the images are located >>>")
outPath = input("Please enter the directory where all named folders should be placed. >>>")
splitChar = input("Please designate charecters that can be used to completely split up the sku string. >>>")
reconChar = input("Please designate one charecter that can be used to reconstruct the wanted sku. >>>")
unincStr = input("If there is any string you do not want to be joined into the output please enter it now. >>>")
stopChar = input("If you want the program to stop reading a filename after a certain charecter please enter it here. >>>")

#Verify Configuration
print("\n\n\n-------------------------------------------------------------------------------------")
print("Configuration:")
print("Parent Directory of images to be organized: " + str(inPath))
print("Target Directory to make folders in: " + str(outPath))
print("Delimeter: " + str(splitChar))
print("Reconstructor: " + str(reconChar))
print("Unincluded String : " + unincStr)
print("Stop Char: " + stopChar)
print("-------------------------------------------------------------------------------------\n\n\n")

## Check our value in the uninlcusion string to see if we are using it
uninc = "true"
if (unincStr == ""):
    print("No valid entry was made for unincluded string so it will be skipped.")
    uninc = "false"

imageList = os.listdir(inPath)      

i = 0
for image in imageList:

    print("\nUnsplit image - " + str(image))
    
    ##Split the image so that we can get the SKU
    imageSplit = re.split("[" + splitChar + "]",image)

    ##Output all parts of the array
##    print("Outputting all image split components")
##    for split in imageSplit:
##        print("(" + split + ")")
        
    ##Look through all splits and attempt to identify the delimter spot
    jpgLoc = 0
    fileLoc = 0
    loc = 0
    for split in imageSplit:
        if(split.lower() == "jpg"):
            jpgLoc = loc
            break
        loc = loc + 1

    fileLoc = jpgLoc - 1

    ##Check to make sure we actually found the file loc
    if(jpgLoc == 0):
        print("File extension was not found successfully, this item will be skipped as it is not a jpg file.")
        continue
    
    ##Reconstruction
    q = 0
    reString = ""
    skugen = "false"
    
    for split in imageSplit:
        if (q == fileLoc):
            if (skugen == "false"):
                reString = reString + split
            break

        if (uninc == "true" and (split in unincStr or unincStr in split)):
            print("Value |" + split + "| is being skipped due to matching our uninclusion string |" + unincStr + "|.")
            skugen = "true"
            q = q + 1
            continue
        
        if (q == 0):
            reString = reString + split
        else:
            reString = reString + reconChar + split

        skugen = "true"
        q = q + 1


    ##Check the completed string for our stop charecter
    if (stopChar is not "" and stopChar in reString):

        conSplit = re.split(stopChar, reString)
        reString = conSplit[0]
        
    print("Attempting to place sku " + str(reString) + "\n")

    try: 
        ##check if a folder exists and create one if not
        Path(outPath + "/" + reString).mkdir(parents=True, exist_ok=True)

        ##Move the item to that folder
        print("Copying to path |" + outPath + "/" + reString + "|") 
        copyfile(inPath + "/" + image, outPath + "/" + reString + "/" + str(i) + ".jpg")
    except:
        print("Failed to process this file.")
        
    i = i+1

print("Placed " + str(i) + " items.")
input("Press any key to exit...")
    
    
