import os
list=[]
directory_in_str="C:\Users\cdg0000151\Downloads\emails"
directory = os.fsencode(directory_in_str)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     readfile = open(filename, "rt")
     contents = readfile.read()
     for line in contents:
	if 'Delivery has failed to these recipients or groups' in line:
    	   skip=contents.readline()
    	   lol=contents.readline()
    	   list.append(lol)
           break
		
for i in list:
   writefile=open('results.txt','w')
   writefile.writeline(i)
wriefile.close()
