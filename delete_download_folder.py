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
        
        
#simplified code is below:        
        
import glob, os.path

filelist = glob.glob(os.path.join('C:\\Users\\vra\\Downloads', "*.tcmx"))
for f in filelist:
    os.remove(f)
