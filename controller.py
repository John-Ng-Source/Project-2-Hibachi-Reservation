from PyQt5.QtWidgets import *
from gui import *
from Hibachi import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)




class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)

        self.new_calender.selectionChanged.connect(self.grab_date_new_res)
        self.edit_calender.selectionChanged.connect(self.grab_date_edit_res)
        self.check_in_button.clicked.connect(lambda: self.current_res_checkin())

    def grab_date_new_res(self):
        self.new_res_lst.clear()
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            print(res_path)
        else:
            res_path = f'{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            print(res_path)
        
        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    entry = f'{line[0]}  -  Party Size: {line[1]}  -  Time: {line[2]}'
                    self.new_res_lst.addItem(entry)
        
        
        

    def grab_date_edit_res(self):
        self.edit_res_lst.clear()
        date_selected = self.edit_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            print(res_path)
        else:
            res_path = f'{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            print(res_path)
        
        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    entry = f'{line[0]}  -  Party Size: {line[1]}  -  Time: {line[2]}'
                    self.edit_res_lst.addItem(entry)
        

    def current_res_checkin(self):
        input_name = self.curr_name.text().strip()
        input_party_size = self.curr_party_size.text().strip()
        input_time = self.curr_time.text().strip()
        
        current_res_file_path = f'Reservations/{date_string}.csv'
        if os.path.isfile(current_res_file_path):
            with open(current_res_file_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    new_line_lst = line.split('  -  ')        #Fix me: Checkin Verification
                    
                    entry = f'{input_name}  -  Party Size: {input_party_size}  -  Time: {input_time}'
                    self.curr_res_lst.addItem(entry)

        

    

    

    




    
    
        
    