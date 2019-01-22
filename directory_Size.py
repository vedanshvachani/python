#!/usr/bin/python
#This program prins the name, path and the size of the direcotry. 
import os
dir_name = raw_input("enter the directories name with full path = ")

def dirsName(root_name):
    for root, dirs, files in os.walk(root_name,topdown=True):
        for i in dirs:
            print "Name of the directory = ",i
	    dirs_path = os.path.abspath(os.path.join(root,i))
	    print "Path of the directory = ",dirs_path
	    dirs_size = os.path.getsize(os.path.abspath(os.path.join(root,i)))
	    print "Size of the directory = ", str(dirs_size)

if(os.path.exists(dir_name)):
    dirsName(dir_name)
else:
    print("Invalid Path")
