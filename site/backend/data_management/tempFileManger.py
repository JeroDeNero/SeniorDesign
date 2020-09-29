import os
import glob


def clearAll():
    files = glob.glob('data_management/temp/*')
    remove(files)


def clearTagImages():
    files = glob.glob('data_management/temp/data_management/temp/tag*.jpg')
    remove(files)


def clearVideo():
    files = glob.glob('data_management/temp/outputtedVideo.avi')
    remove(files)
    files = glob.glob('data_management/temp/imageFront.jpg')
    remove(files)


def remove(targets):
    for target in targets:
        try:
            os.remove(target)
        except:
            print('Error while deleteing target: ', target)
