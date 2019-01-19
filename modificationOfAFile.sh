#! /usr/bin/python
import os, stat
import datetime as dt
import pwd

path = raw_input("enter the path = ")
def modifiedFiles(path):
    now = dt.datetime.now()
    ago = now-dt.timedelta(minutes=60)
    for root, dirs,files in os.walk(path):  
        for fname in files:
            loc = os.path.join(root, fname)
            st = os.stat(loc)
            size = os.path.getsize(os.path.abspath(loc))
            user_id = st.st_uid
            user_name = pwd.getpwuid(user_id).pw_name
            ctime = dt.datetime.fromtimestamp(st.st_ctime)
	    size = os.path.getsize(os.path.abspath(loc))
            read = os.access(loc, os.R_OK)
            write = os.access(loc, os.W_OK)
            execute = os.access(loc, os.X_OK)
            if ctime > ago:
                print("Files whoes permissions and file size have been changed")
                print ("File name = "+fname)
                print ("Path = "+ path)
                print ("Last change time = " + str(ctime))
		print ("File size = "+ str(size))
                print ("Ownership of a file = "+ user_name)
                print ("Owner Permissions of file = "+ loc) 
                if(read):
                    readFile = "Read (r) (4)"
                else:
                    readFile = "Read (-)"
                if(write):
                    writeFile = "Write (w) (2)"
                else:
                    writeFile = "Write (-)"
                if(execute):
                    executeFile = "Execute (x) (1)"
                else:
                    executeFile = "Execute (-)"
                print readFile
                print writeFile
                print executeFile
if (os.path.exists(path)):
    modifiedFiles(path)
else:
    print "Invalid path"
