from PyQt5.QtWidgets import *
from gui import *
from Hibachi import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)




class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)


    

    




    
    
        
    