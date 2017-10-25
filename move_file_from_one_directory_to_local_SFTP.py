import pysftp

remote_file = 'zmd-backend.log'
srv = pysftp.Connection(host="herkules", username="vra",
password="gj1017")

data = srv.listdir('/var/log')

for i in data:
    print i

remotepath = '/var/log/2011-10-04SyslogCatchAll.txt'  #file in sftp
localpath = 'C:/Users/vra/2011-10-04SyslogCatchAll.txt' #moves it to this location

srv.get(remotepath, localpath)

#serv.put(remotepath, localpath) use it to put file to remote from local

f = open(r"C:\Users\vra\2011-10-04SyslogCatchAll.txt")

print f.readlines(1) #reads the first line of file

srv.close()

