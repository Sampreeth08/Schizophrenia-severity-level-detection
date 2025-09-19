import sys
import os
from schiz import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.testsymp)
     self.ui.pushButton_2.clicked.connect(self.crtcsv)
     self.ui.pushButton_3.clicked.connect(self.dtree2)
     self.ui.pushButton_4.clicked.connect(self.dtree1)
     self.ui.pushButton_5.clicked.connect(self.obsymp)
     

  def testsymp(self):
    os.system("python Python/testsymps1.py")

  def crtcsv(self):
    os.system("python Python/createcsv1h.py")

  def dtree2(self):
    os.system("python Python/dtc4.py")

  def dtree1(self):
    os.system("python Python/dtc3.py")

  def obsymp(self):
    os.system("python Python/obsymps1.py")



          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
