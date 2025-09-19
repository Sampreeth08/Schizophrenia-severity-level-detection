import sys
import csv
import os

import sqlite3
con = sqlite3.connect('schizo1')

cur = con.cursor()
cur.execute('SELECT * FROM obsymps;')
rows = cur.fetchall()
fp = open('data/obsymps1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
print('obsymps1.csv file successfully created')
cur.execute('SELECT * FROM testsymps;')
rows = cur.fetchall()
fp = open('data/testsymps1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
print('testsymps1.csv file successfully created')
con.commit()

