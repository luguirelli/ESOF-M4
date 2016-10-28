#! python3
#backupToZip.py - Copies an entire folder and its contentes into a Zip file whose filename increments
import zipfile , os
def backupToZip(folder):
    #backup the entire contents of the folder into a Zip file
    folder = os.path.abspath(folder)  #make sure folder is absolute
    #Figure out the filename this code should use based on what file already exist
    number=1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number=number + 1
    #TODO : Create the ZIP file
    print('Creating %s ...'%(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')
    #TODO : Walk the entire folder tree and compress the files in each folder
    for foldername , subfolders , filenames in os.walk(folder):
        print('Adding files in %s...' %(foldername))
        #Add the current folder to the ZIP file
        backupZip.write(foldername)
        #Add all the files in this folder to the ZIP file
        for filename in filenames:
            newBase= os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't backup the backup ZIP files
            backupZip.write((foldername,filename))
    backupZip.close()
    print('Done')
backupToZip('C:\\delicious')
