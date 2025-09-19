import sys
import csv
import os

import sqlite3
con = sqlite3.connect('schizo1')

cur = con.cursor()
cur.execute('SELECT * FROM obsymps;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('data/obsymps1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('obsymps1.csv file successfully created')
cur.execute('SELECT * FROM testsymps;')
names = [description[0] for description in cur.description]
rows = cur.fetchall()
fp = open('data/testsymps1.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows([names])
myFile.writerows(rows)
fp.close()
print('testsymps1.csv file successfully created')
con.commit()

