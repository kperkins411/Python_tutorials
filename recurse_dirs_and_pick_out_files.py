import os as os
import shutil
import errno
import zipfile

def setup(targetdir):
    # empty target
    try:
        shutil.rmtree(targetdir)
    except OSError as e:
        print( e.errno )
    # crete targetdir
    os.makedirs(targetdir)

def findFile(directory,targetfile):
    # recurse dirs, build a list of dirs
    for directory1, subdirs, files in os.walk(directory):
        if targetfile in files:
            return os.path.join(directory,targetfile)
        for dir in subdirs:
            res = findFile(os.path.join(directory,dir),targetfile)
            if res is not None:
                return res
        return None

def copyfiles(files,targetdir):
    for file in files:
        try:
            tokens= file.split('/')
            student_id= next((x for x in tokens if x.startswith("00")), [None])+'_'
            filename = "1_" +student_id +tokens[len(tokens)-1]

            dest = os.path.join(targetdir,filename)
            import shutil
            shutil.copy2(file, dest)  # complete target filename given
        except Exception as e:
            print (e.args)

def unzip_to_dir(zippedfile,dest_directory):
    try:
        #unzip into directory(make it if necessary)
        tmpZip = zipfile.ZipFile(zippedfile)
        tmpZip.extractall(dest_directory)
    except Exception as e:
        print(e.args)

def extractall(targetdir, harvestdir):
    # lets get a list of the files
    all = os.listdir(harvestdir)

    # create a dir for each
    for file in all:
        id = file.split("_")[1]
        dir = os.path.join(targetdir, id)
        if not os.path.exists(dir):
            os.makedirs(dir)

        # extract zip to the dir
        zippedfile = os.path.join(targetdir, file)
        unzip_to_dir(zippedfile, dir)

        # get rid of zip
        os.remove(zippedfile)

def getfile(targetfile,targetdir, harvestdir):
    files = []

    # recurse dirs, build a list of dirs
    subdirs = os.listdir(harvestdir)
    for directory in subdirs:
        dir1 = os.path.join(harvestdir, directory)
        file1 = findFile(dir1, targetfile)
        files.append(file1)

    copyfiles(files, targetdir)

if __name__=='__main__':
    # define harvest from dir and target dir
    harvestdir = '/home/keith/Desktop/327_proj5/class2/bits/'

    # extract all the zips
    extractall(harvestdir, harvestdir)

    # file to look for
    targetfile1 = 'data_store.cpp'
    # targetdir1 = '/home/keith/Desktop/410/proj4_jplag/' + os.path.splitext(targetfile1)[0]

    targetfile2 = 'data_store_file.cpp'
    # targetdir2 = '/home/keith/Desktop/410/proj4_jplag/' + os.path.splitext(targetfile2)[0]

    targetfile3 = 'string_database.cpp'
    # targetdir3 = '/home/keith/Desktop/410/proj4_jplag/' + os.path.splitext(targetfile3)[0]

    targetfile4 = 'MED_Tester.cpp'

    getfile(targetfile1, harvestdir, harvestdir)
    getfile(targetfile2, harvestdir, harvestdir)
    getfile(targetfile3, harvestdir, harvestdir)
    getfile(targetfile4, harvestdir, harvestdir)

