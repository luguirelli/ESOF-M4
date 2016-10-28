import os, shutil
#todo walk throuth a folder tree
os.chdir('C:\\')
for foldername, subfolders , filenames in os.walk('C:\\Users\\Gustavo\\Downloads'):
    print('the current folder is ' + foldername)
    for subfolder in subfolders:
        print('subfolder of ' + foldername + ':' + subfolder)
    for filename in filenames:
        print('file inside ' + foldername + ':' + filename)
        #todo shearches for a file with a certain extension
        if filename.endswith('.png') or filename.endswith('.jpeg'):
            print('this file is a image ' + filename)
        #todo copy these files from whatever they are into a new folder
            path = 'C:\\Users\\Gustavo\\Downloads\\'+ os.path.basename(filename)
            print(path)
            str(path)
            shutil.copy(path,'C:\\Users\Gustavo\Downloads\Imagens')

    print('')



