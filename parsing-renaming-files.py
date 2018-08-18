import os
os.chdir('E:/Files/Test')
for files in os.listdir():
    fname,fext=os.path.splitext(files)
    ifile,fcourse,fno=fname.split(' - ')
    nfiles="{}-{}{}".format(fno[1:].zfill(2),ifile,fext)
    os.rename(files,nfiles)
    