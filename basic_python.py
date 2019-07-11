import os,sys

# get home path
def getHomePath():
    homepath=os.environ['USERPROFILE']
    # homepath1=os.path.expanduser('~')
    reture homepath