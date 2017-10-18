# this will delete all the file in the directory. it also deletes subdirectories 

import os, shutil
folder = r'C:\Users\vra\Downloads'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
        
        
#simplified code is below: this will delete only a file will with certain extension       
        
import glob, os.path

filelist = glob.glob(os.path.join('C:\\Users\\vra\\Downloads', "*.tcmx"))
for f in filelist:
    os.remove(f)

# to check if the file exist and rasie exception use

import glob

if glob.glob('C:\\Program Files (x86)\\Google\\Chrome\\Application\\62.0.3202.62\\*.tcmx'):
            print 'The file exists, Ocular File is successfully downloaded'

 else:
       raise Exception ("No file exists, there might be some problem downloading the file!")
