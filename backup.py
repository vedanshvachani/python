#!/usr/bin/python
import os
import shutil
path = "/root/Downloads/backup/"
def copyPath(path,path1):
	for root,dirs,files in os.walk(path1,topdown=True):
		for i in files:
			ab = os.path.abspath(os.path.join(root,i))
			os.system("cp -r "+ab+" "+path)
path1 = raw_input("enter the path : ")
if(os.path.exists(path1)):
	if(os.path.exists(path)):
		print "yes"
		print path
		copyPath(path,path1)
		os.system("zip -r /root/Downloads/backup.zip /root/Downloads/backup")
	else:
		os.system("mkdir /root/Downloads/backup")
		print "done"
		copyPath(path,path1)
		os.system("zip -r /root/Downloads/backup.zip /root/Downloads/backup")

