import csv
import unittest
from selenium import webdriver
import time
import os


#the test removes the file first
try:
    os.remove(r'C:\Users\vra\Downloads\sync_check.csv') 
except OSError:
    pass

class excel(unittest.TestCase):
    
    
    def test_sync_excel(self):
        
        
        with open(r'C:\Users\vra\Downloads\sync_check.csv') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|', )
            
            
            
    
            spamList = []
            
            #acess the row in excel

            for row in spamreader:

                if len(row) != 0:
                    
                    
            
                    spamList = spamList + [row]      

            mystr1 = spamList[4][3]
        
            print mystr1
            
            mystr2 = spamList[3][2]
        
            print mystr2
            
            print spamList[2][2]
                    
            self.assertEqual(mystr1[-2:], 'ok', '') #takes last two strings of the output
            self.assertEqual(mystr2[-2:], 'ok', '')  #takes last two strings of the output
            
            


    
    def test_rows(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get('http://reg-es.gramjuhl/~tcm/sync_check.csv')
        
        time.sleep(3)
        
        cr = csv.reader(open(r'C:\Users\vra\Downloads\sync_check.csv'))


        print len(list(cr))

        
       
        
            
            