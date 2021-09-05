import os
import shutil
import time

def main():
    deletedFoldersCount = 0
    deletedFilesCount = 0

    path = input("enter path here: ")

    days = 30
    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds > getFile(rootFolder):
                removeFolder(rootFolder)
                deletedFoldersCount = deletedFoldersCount + 1
                break

            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)

                    if seconds > getFile(rootFolder):
                        removeFolder(rootFolder)
                        deletedFoldersCount = deletedFoldersCount + 1
                        break
                    else:
                        if seconds > getFile(path):
                            removeFile(path)
                            deletedFilesCount = deletedFilesCount + 1
    else:
        print("No Path Found")

    print("total files deleted: ", deletedFilesCount)
    print("total folders deleted: ", deletedFoldersCount)

def removeFolder(path):
    if not shutil.rmtree(path):
        print("path is removed successfully")
    else:
        print("unable to delete")

def removeFile(path):
    if not os.remove(path):
        print("file removed successfully")
    else:
        print("unable to delete file")

def getFile(path):
    cTime = os.stat(path).st_ctime
    return cTime

main()