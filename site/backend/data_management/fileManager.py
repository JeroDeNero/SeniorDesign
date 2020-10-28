# pylint: disable=bare-except
"""to stop pylint from complainign about any excepts"""

import os
import glob

TARGETPATH = "data_management/../../frontend/src/assets/Data"


def removeRun(pipeID, date):
    """removes images, and video for the targeted run"""

    global TARGETPATH

    target = glob.glob("{}/{}/{}".format(TARGETPATH, pipeID, date))
    remove(target + "/*")
    os.rmdir(target)


def removeTag(pipeID, date, tagNumber):
    """Removes saved image of based upon the input"""
    target = "{}/{}/{}".format(pipeID, date, tagNumber)
    remove(target + "/*")
    os.rmdir(target)


def remove(targets):
    """removes the file or directory that is sent"""
    for target in targets:
        try:
            os.remove(target)
        except:
            print('Error while deleteing target: ', target)
