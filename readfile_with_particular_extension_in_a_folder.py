
#the code will read all the files ending with .tcmx in particular directory

import os

directory = os.path.normpath("C:\\Users\\vra\\Documents\\important")
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".tcmx"):
            f=open(os.path.join(subdir, file),'r')
            a = f.read()
            print a
            
            
#simplified code


path = 'C:\\Users\\vra\\Downloads\\*.tcmx'   
        files=glob.glob(path)   
        for file in files:     # @ReservedAssignment
            f=open(file, 'r')
            print f.read() 
