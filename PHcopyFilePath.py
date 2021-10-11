import os
import shutil

fromFolder = r'C:\Users\pharsh\Desktop\MyFiles\cobaltFolder'

toFolder = r'C:\Users\pharsh\Desktop\MyFiles\daveFolder'

for fromFile, directory, files in os.walk(fromFolder):
    toFile = fromFile.replace(fromFolder, toFolder, 1)
    if not os.path.exists(toFile):
        os.makedirs(toFile)
    for file_ in files:
        source_file = os.path.join(fromFile, file_)
        destination_file = os.path.join(toFile, file_)
        fromTime = os.path.getmtime(os.path.join(fromFile,file_))
        if os.path.exists(destination_file):
            toTime = os.path.getmtime(os.path.join(toFile,file_))
            if os.path.basename(source_file) ==  os.path.basename(destination_file):
                if fromTime < toTime:
                    continue
                else: shutil.copy(source_file, toFile)
        else:shutil.copy(source_file, toFile)
            ##os.remove(dst_file)

for toFile, directory, files in os.walk(toFolder):
    fromFile = toFile.replace(toFolder, fromFolder, 1)
    if not os.path.exists(fromFile):
        os.makedirs(fromFile)
    for file_ in files:
        source_file = os.path.join(toFile, file_)
        destination_file = os.path.join(fromFile, file_)
        fromTime = os.path.getmtime(os.path.join(toFile,file_))
        if os.path.exists(destination_file):
            toTime = os.path.getmtime(os.path.join(fromFile,file_))
            if os.path.basename(source_file) ==  os.path.basename(destination_file):
                if fromTime < toTime:
                    continue
                else: shutil.copy(source_file, fromFile)
        else:shutil.copy(source_file, fromFile)
            ##os.remove(dst_file)
print('script complete')