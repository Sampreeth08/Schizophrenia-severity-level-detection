import sys
import os
from testsymps import *
from PyQt5 import QtWidgets, QtGui, QtCore

import sqlite3
con = sqlite3.connect('schizo1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)
     #self.ui.pushButton_2.clicked.connect(self.testdetails)

  def insertvalues(self):
    with con:
      cur = con.cursor()
      id = str(self.ui.lineEdit_9.text())
      s1 = str(self.ui.lineEdit_3.text())
      s2 = str(self.ui.lineEdit_4.text())
      s3 = str(self.ui.lineEdit_5.text())
      s4 = str(self.ui.lineEdit_6.text())
      cur.execute('INSERT INTO testsymps(id,s1,s2,s3,s4) VALUES(?,?,?,?,?)',(id,s1,s2,s3,s4))
      con.commit()

#  def testdetails(self):
#    os.system("python ptests1.py")     

if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
