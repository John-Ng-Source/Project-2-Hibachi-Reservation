from controller import *
from gui import *


            
            
            

def main():
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()




if __name__ == '__main__':
    main()