import os

directory = os.path.normpath("C:\\Users\\vra\\Documents\\important")
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".tcmx"):
            f=open(os.path.join(subdir, file),'r')
            a = f.read()
            print a
            