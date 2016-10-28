#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY
import shutil, os , re
#Create a regex tha matches files with the American date format
#datePattern = re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""",re.VERBOSE)
datePattern = re.compile(r"""^(1)(2 (3) )-(4 (5) )-(6 (7) )(8)$""",re.VERBOSE)
#TODO : Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    #TODO : Skip files without a date
    if mo == None :
        continue
    #TODO : Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #TODO : Form The European-style filename
    euroFilename = beforePart + dayPart + '-' +  monthPart + '-' + yearPart + afterPart
    #TODO : Get the full , absolute file paths
    absworkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absworkingDir,amerFilename)
    euroFilename = os.path.join(absworkingDir,euroFilename)
    #TODO : Rename the files
    print('Renaming "%s to "%s" ...' %(amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename)
