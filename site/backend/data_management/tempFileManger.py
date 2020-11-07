# pylint: disable=bare-except
"""to stop pylint from complainign about any excepts"""

import os
import glob

TARGETPATH = "data_management/../../frontend/dist/site/assets/Data"


def moveFiles(pipeID, dateTaken):
    """relocates the files out of temp files to thier permanent home"""
    global TARGETPATH

    try:
        os.mkdir("{}/{}/".format(TARGETPATH, pipeID))
    except:
        print(pipeID, " pipe already exists.")

    try:
        os.mkdir("{}/{}/{}/".format(TARGETPATH, pipeID, dateTaken))
        os.mkdir("{}/{}/{}/tags".format(TARGETPATH, pipeID, dateTaken))
    except:
        print(
            "failed to make directories {}/{}/{}/tags".format(TARGETPATH, pipeID, dateTaken))

    try:
        os.rename("data_management/temp/imageFront.jpg",
                  "{}/{}/{}/imageFront.jpg".format(TARGETPATH, pipeID, dateTaken))
    except:
        print(
            "Error renaming: {}/{}/{}/imageFront.jpg".format(TARGETPATH, pipeID, dateTaken))

    try:
        os.rename("data_management/temp/outputtedVideo.mp4",
                  "{}/{}/{}/outputtedVideo.mp4".format(TARGETPATH, pipeID, dateTaken))
    except:
        print("Error renaming: {}/{}/{}/outputtedVideo.mp4".format(TARGETPATH, pipeID, dateTaken))

    files = glob.glob("data_management/temp/tag*.jpg")
    for target in files:
        try:
            os.rename(target, ("{}/{}/{}/tags/{}".format(TARGETPATH,
                                                         pipeID, dateTaken, os.path.basename(target))))
        except:
            print('Error renaming: ', target)


def clearAll():
    """clears all files in the temp folder"""
    files = glob.glob('data_management/temp/*')
    remove(files)


def clearTagImages():
    """clears all tag images in the temp folder"""
    files = glob.glob('data_management/temp/data_management/temp/tag*.jpg')
    remove(files)


def clearVideo():
    """clears all video files in the temp folder"""
    files = glob.glob('data_management/temp/outputtedVideo.mp4')
    remove(files)
    files = glob.glob('data_management/temp/imageFront.jpg')
    remove(files)


def remove(targets):
    """removes targeted files or directory"""
    for target in targets:
        try:
            os.remove(target)
        except:
            print('Error while deleteing target: ', target)
