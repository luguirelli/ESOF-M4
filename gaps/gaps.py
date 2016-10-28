import shutil, os
prefix= input('What´s the central name of the file:')
suffix = input('What´s the extension of the file(ex: .zip ) :')
path = 'C:\Python\gaps\\'
for i,filename in enumerate(os.listdir(path)):
    if filename.startswith(prefix):
        num = int(filename[len(prefix):len(filename)-len(prefix):])
        if(num!=i+1):
            shutil.move( path + filename,path + prefix + str(i+1).zfill(3)+ suffix )
