import send2trash,os
#todo shearch for file that have at least 100MB
#todo walk throuth a folder tree
os.chdir('C:\\')
for foldername, subfolders , filenames in os.walk('C:\Python'):
    print('the current folder is ' + foldername)
    for subfolder in subfolders:
        print('subfolder of ' + foldername + ':' + subfolder)

    for filename in filenames:
        print('file inside ' + foldername + ':' + filename)
        if(os.path.getsize(foldername+"/"+filename)>=104857600):
            print(os.path.abspath(filename) + ' O arquivo é maior que 100 MB')

    print('')


#todo print these files names with their absolute paht to the screen
