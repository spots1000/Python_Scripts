import os
import glob
from shutil import copyfile

#Announcements
print("-------------------------------------------------------------------------------------")
print("Welcome to the Image in folder tool.")
print("This tool takes in a directory of named folders with un-named images and converts the images into sequentially named images based on that folder name and a given manufacturer number.")
print("Please fill out the configuration below to continue.")
print("-------------------------------------------------------------------------------------\n\n\n")

#Get desired paths
inPath = input("Please enter the root directory where all the folders are located >>>")
outPath = input("Please enter the directory where all processed images should be placed. (If you want them in a folder please include the folder in path) >>>")
ignoreFolder = input("If your destination folder is in the same directory as the input folders please specify it's name here: >>>")
prefix = input("Please specify the manufacturer number you want to use to generate the filenames correctly (EG XXX-ABCD123.jpg specify XXX). >>>")

#Verify Configuration
print("\n\n\n-------------------------------------------------------------------------------------")
print("Please verify the following configuration information:")
print("Parent Directory of folders to be searched: " + str(inPath))
print("Target Folder or Directory to place images in: " + str(outPath))
print("Folder that should be ignored (If applicable): " + str(ignoreFolder))
print("Desired manufacturer number: " + str(prefix))
print("-------------------------------------------------------------------------------------\n\n\n")

folderList = os.listdir(inPath)      
errorList = "Error Files: \n"
imageOut = ""

for folder in folderList:
    
    print("Processing Folder: " + str(folder) + "...")
    imageList = glob.glob(inPath + "/" + (folder) +"/*")

    if (folder == ignoreFolder):
        print("*** Folder is being ignored as destination folder ***")

    else:
        id = 1
        for image in imageList:
            print("Copying File " + str(image) )

            #Check to make sure the file is an image
            split = image.split(".")
            length = len(split)
            
            print(length)
            if (length == 2 and split[1].lower() == "jpg"):

                try:

                    ## Strip Leading Zeroes (Enable if needed)
                    newFolderName = folder
                    ##newFolderName = folder.lstrip("0")
                    
                    copyfile(image, str(outPath) + "/" + str(prefix) + "-" + str(newFolderName) + "-" + str(id) + ".jpg")
                    imageOut = imageOut + ("\n" + str(prefix) + "-" + str(newFolderName) + "-" + str(id) + ".jpg")
                    id = id+1
                except:
                    print("====================================================\nLocated a file that was not a jpg at: " + "Folder " + str(folder) + " Image " + str(image) + "\n====================================================")
                    errorList = errorList + ("\n[" + str(image) + "]\n")
                
            else:
                print("====================================================\nLocated a file that was not a jpg at: " + "Folder " + str(folder) + " Image " + str(image) + "\n====================================================")
                errorList = errorList + ("\n[" + str(image) + "]\n")


print("The program has processed all files it could find in the target folder. Errors will now be displayed. \n\n")

errFile = open(os.path.join(outPath, "errors.txt"), "w")
errFile.write(errorList)
errFile.close()

childFile = open(os.path.join(outPath, "out.txt"), "w")
childFile.write(imageOut)
childFile.close()

print("Output files have been printed.")


