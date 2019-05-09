
import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow, QMessageBox
from ConvertUI import *
import time
from PyQt5.QtCore import pyqtSignal

class MyMainWindow(QMainWindow, Ui_MainWindow):    
    
    longTask = pyqtSignal() 
    
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)      
        self.longTask.connect(self.runLongLong)        
        self.longTask.connect(self.runShort)           
      
    def close(self):
        print("Bye!")
        sys.exit()        
    
    def calc(self):
        print("calc begin!")
        degree = float(self.xEdit.text())*5/9
        self.yEdit.setText(str(degree))
        self.longTask.emit()  #
        print("calc end!")
        
    def runLongLong(self):
        print("runLongLong begin!")
        for x in range(1000000000):
            pass
        print("runLongLong end!")
		
    def runShort(self):
        print("runShort begin!")
        for x in range(100000000):
            pass
        print("runShort end!")
        
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
