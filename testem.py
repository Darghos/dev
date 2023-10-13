import os
list=[]
directory_in_str="C:\Users\151\Downloads\emails"
directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     readfile=open(filename, "rt")
     contents=readfile.read()
     for line in contents:
	     if 'Delivery has failed to' in line:
    	   contents.readline()
    	   lol=contents.readline()
    	   list.append(lol)
         break
