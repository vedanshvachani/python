#!/usr/bin/python
import os
root_name = raw_input("enter the directories name with full path = ")

def dirsName(root_name):
    for root, dirs, files in os.walk(root_name,topdown=True):
        for i in files:
            print "Name of the directory = ",i
	    files_path = os.path.abspath(os.path.join(root,i))
	    print "Path of the directory = ",files_path
	    files_size = os.path.getsize(os.path.abspath(os.path.join(root,i)))
	    print "Size of the directory = ", str(files_size)

if(os.path.exists(root_name)):
    dirsName(root_name)
else:
    print("Invalid Path")
