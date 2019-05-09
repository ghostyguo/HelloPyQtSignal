
import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow, QMessageBox
from ConvertUI import *
import time
import threading 

class MyMainWindow(QMainWindow, Ui_MainWindow):    
        
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)              
      
    def close(self):
        print("Bye!")
        sys.exit()        
    
    def calc(self):
        print("calc begin!")
        degree = float(self.xEdit.text())*5/9
        self.yEdit.setText(str(degree))
        #new thread...
        print("call thread!")
        t = threading.Thread(target = self.runLongLong) 
        t.start()
        #...
        print("calc end!")
        
    def runLongLong(self):
        print("runLongLong begin!")
        for x in range(1000000000):
            pass
        print("runLongLong end!")
        
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
