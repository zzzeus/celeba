import os,sys

# get home path
def getHomePath():
    homepath=os.environ['USERPROFILE']
    # homepath1=os.path.expanduser('~')
    return homepath

# get download path
def getDownloadPath():
    homepath=os.environ['USERPROFILE']
    # homepath1=os.path.expanduser('~')
    return os.path.join(getHomePath(),'Downloads')

# if file is existed
def isExisted(filepath):
    return os.path.exist(filepath)




