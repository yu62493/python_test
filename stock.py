import csv
import string
import codecs
import urllib.parse
import urllib.request
import os
import datetime
import shutil
url="http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php"
values = {'download' : 'csv',
          'qdate' : '104/08/03',
          'selectType' : 'ALLBUT0999' }

data = urllib.parse.urlencode(values)
req= urllib.request.Request(url, data.encode('utf-8'))
response = urllib.request.urlopen(req)

file1=open("qq.txt","w")
for line in response.read().decode('ISO-8859-1'):
    if len(line)>0:
        file1.writelines(line)
file1.close()
