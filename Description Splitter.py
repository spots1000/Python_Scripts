import os
import glob
import re
from pathlib import Path
from shutil import copyfile
import codecs

#Variables
textPath = "in.txt"
outPath = "out.txt"
curText = []
outList = []
i = 0

#Announcements
print("-------------------------------------------------------------------------------------")
print("Welcome to the description fixer tool!")
print("The purpose of this tool is to transform feature lists seperated by newlines into lists seperated by <li> bullet points.")
print("Bullet points should appear seperated by a new line and full descriptions should be seperated by the indicator tag <splt>. Please ensure that the text contains no quotes at the begining and end.")
print("-------------------------------------------------------------------------------------\n\n\n")

# text file config
input("Please place a list of descriptions in a text file called '" + textPath + "' and then press any key to proceed.")

## Ensure before opening text file that we have a valid file to read.
if not (os.path.isfile(textPath)):
    print("A valid list file was not found, program will now exit.")
    input("Press any key to exit...")
    sys.exit()    

## Delimiter input and config
delim = input("Please enter the delimter that the description should be split on. Default is \n new line.")

if (delim == ""):
    delim = "\n"
    
textFile = open(textPath, encoding="utf8")

## Make sure our output file is cleared
outFile = open(outPath, "w")
outFile.close()

print("Begining Processing...")

## Read the entire text file
for line in textFile:

    try:
        ## Gather lines stage
        lineSplit = line.split("\n")
    except UnicodeDecodeError:
        pass
    
    ## Either do final processing if we have reached the end of this description or continue reading
    if (lineSplit[0] == "<splt>"):
        
        print("Detected end of one description, processing...")
        i = i + 1

        ##Open the output file
        outFile = open(outPath, "a")

        ##Write in our outfile the corrected data
        for txt in curText:
            try:
                outFile.write("<li>" + str(txt) + "</li>")
            except:
                outFile.write("<li></li>");
                print(txt);
                
        ## Finish up this item and reset
        outFile.write("\n")
        curText.clear()
        outFile.close()
        
    else:

        finalSplit = lineSplit[0].split("[" + "]")
        curText.append(finalSplit[0])

        
textFile.close()

print("Reached EOF, processing remainder")
i = i + 1

##Open the output file
outFile = open(outPath, "a")

##Write in our outfile the corrected data
for txt in curText:
    outFile.write("<li>" + str(txt) + "</li>")

## Finish up this item and reset
outFile.write("\n")
outFile.close()

##Final output
print("All processing completed. " + str(i) + " total descriptions processed.")
input("Press any key to exit...")
sys.exit()
