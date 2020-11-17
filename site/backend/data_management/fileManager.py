# pylint: disable=bare-except
"""to stop pylint from complainign about any excepts"""

import os
import glob

TARGETPATH = "data_management/../../frontend/dist/site/assets/Data"


def removeRun(pipeID, date):
    """removes images, and video for the targeted run"""

    global TARGETPATH

    direct = "{}/{}/{}/".format(TARGETPATH, pipeID, date)

    try:
        target = glob.glob("{}**/*".format(direct))
        remove(target)
        os.rmdir("{}tags/".format(direct))
    except:
        print("tags failed to delete.  Either already deleted, or images failed to delete")

    try:
        target = glob.glob("{}*".format(direct))
        remove(target)
        os.rmdir("{}".format(direct))
    except:
        print("run failed to delete.  Either already deleted, or failed to delete contents prior")

    try:
        os.rmdir("{}/{}/".format(TARGETPATH, pipeID))
    except:
        print("not empty, or does not exist")


def removeTag(pipeID, date, tagNumber):
    """Removes saved image of based upon the input"""
    direct = "{}/{}/{}/tags/".format(pipeID, date, tagNumber)

    remove(direct + "tag" + tagNumber)

    try:
        os.rmdir(direct)
    except:
        print("file doesn't exist or was not the last tag")


def remove(targets):
    """removes the file or directory that is sent"""
    for target in targets:
        try:
            os.remove(target)
        except:
            print('Error while deleteing target: ', target)
