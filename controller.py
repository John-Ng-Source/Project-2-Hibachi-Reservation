from PyQt5.QtWidgets import *
from gui import *
from Hibachi import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


current_res_file_path = f'Reservations/{date_string}.csv'
time_slots = ['4:00', '4:30','5:00', '5:30','6:00', '6:30','7:00', '7:30','8:00', '8:30']

class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setupUi(self)
        self.new_calender.selectionChanged.connect(self.grab_date_new_res)
        self.edit_calender.selectionChanged.connect(self.grab_date_edit_res)
        self.check_in_button.clicked.connect(lambda: self.current_res_checkin)
        self.curr_res_lst.itemDoubleClicked.connect(self.alt_current_res_checkin)
        self.rad_400.clicked.connect(self.disp_res_aval_400)
        self.rad_430.clicked.connect(self.disp_res_aval_430)
        self.rad_500.clicked.connect(self.disp_res_aval_500)
        self.rad_530.clicked.connect(self.disp_res_aval_530)
        self.rad_600.clicked.connect(self.disp_res_aval_600)
        self.rad_630.clicked.connect(self.disp_res_aval_630)
        self.rad_700.clicked.connect(self.disp_res_aval_700)
        self.rad_730.clicked.connect(self.disp_res_aval_730)
        self.rad_800.clicked.connect(self.disp_res_aval_800)
        self.rad_830.clicked.connect(self.disp_res_aval_830)

        self.new_res_button.clicked.connect(self.set_new_res)
        self.edit_del_button.clicked.connect(self.del_res)
        self.edit_set_button.clicked.connect(self.set_res)


    def grab_date_new_res(self):
        self.new_res_lst.clear()
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            
        
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
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
        
        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    entry = f'{line[0]}  -  Party Size: {line[1]}  -  Time: {line[2]}'
                    self.edit_res_lst.addItem(entry)
        

    def current_res_checkin(self):
        items = []
        for index in range(self.curr_res_lst.count()):
            items.append(self.curr_res_lst.item(index))
        
        input_name = self.curr_name.text().strip()
        print(input_name)
        input_party_size = self.curr_size.text().strip()
        print(input_party_size)
        input_time = self.curr_time.text().strip()
        print(input_time)
        input_text = f'{input_name}  -  Party Size:  {input_party_size}  -  Time:  {input_time}'
        for list_item in items:
            print(list_item.text())
            
            print(input_text)
            if list_item.text() == input_text:
                print('True')
                self.curr_res_lst.setCurrentItem(list_item)
                self.curr_res_lst.currentItem().setText(f'{input_name}  -  Party Size:  {input_party_size}  -  Time:  {input_time}  -  CHECKED-IN')


    def alt_current_res_checkin(self):
        curr_text = self.curr_res_lst.currentItem()
        print(curr_text.text())
        if len(curr_text.text().split('  -  ')) < 4:
            curr_text.setText((curr_text.text() + '  -  CHECKED-IN'))
                      
        else:
            temp_lst = curr_text.text().split('  -  ')
            print(temp_lst)
            temp_lst.pop()
            curr_text.setText('  -  '.join(temp_lst))


    def disp_res_aval_400(self):
        four_00 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '4:00':
                        four_00.aval_seats -= int(line[1])
                

            if four_00.aval_seats > 48:
                four_00.aval_tables = 5
            elif four_00.aval_seats > 36:
                four_00.aval_tables = 4
            elif four_00.aval_seats > 24:
                four_00.aval_tables = 3
            elif four_00.aval_seats > 12:
                four_00.aval_tables = 2
            elif four_00.aval_seats > 0:
                four_00.aval_tables = 1
            else:
                four_00.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(four_00.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(four_00.aval_tables)}')
        return int(four_00.aval_seats)    

    def disp_res_aval_430(self):
        four_30 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile, delimiter =',')
                for line in content:
                    if line[2] == '4:30':
                        four_30.aval_seats -= int(line[1])
                print(four_30.aval_seats)

            if four_30.aval_seats > 48:
                four_30.aval_tables = 5
            elif four_30.aval_seats > 36:
                four_30.aval_tables = 4
            elif four_30.aval_seats > 24:
                four_30.aval_tables = 3
            elif four_30.aval_seats > 12:
                four_30.aval_tables = 2
            elif four_30.aval_seats > 0:
                four_30.aval_tables = 1
            else:
                four_30.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(four_30.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(four_30.aval_tables)}')
        return int(four_30.aval_seats)    

    def disp_res_aval_500(self):
        five_00 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '5:00':
                        five_00.aval_seats -= int(line[1])
                print(five_00.aval_seats)

            if five_00.aval_seats > 48:
                five_00.aval_tables = 5
            elif five_00.aval_seats > 36:
                five_00.aval_tables = 4
            elif five_00.aval_seats > 24:
                five_00.aval_tables = 3
            elif five_00.aval_seats > 12:
                five_00.aval_tables = 2
            elif five_00.aval_seats > 0:
                five_00.aval_tables = 1
            else:
                five_00.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(five_00.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(five_00.aval_tables)}')
        return int(five_00.aval_seats)    

    def disp_res_aval_530(self):
        five_30 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '5:30':
                        five_30.aval_seats -= int(line[1])
                print(five_30.aval_seats)

            if five_30.aval_seats > 48:
                five_30.aval_tables = 5
            elif five_30.aval_seats > 36:
                five_30.aval_tables = 4
            elif five_30.aval_seats > 24:
                five_30.aval_tables = 3
            elif five_30.aval_seats > 12:
                five_30.aval_tables = 2
            elif five_30.aval_seats > 0:
                five_30.aval_tables = 1
            else:
                five_30.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(five_30.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(five_30.aval_tables)}')
        return int(five_30.aval_tables)    

    def disp_res_aval_600(self):
        six_00 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '6:00':
                        six_00.aval_seats -= int(line[1])
                print(six_00.aval_seats)

            if six_00.aval_seats > 48:
                six_00.aval_tables = 5
            elif six_00.aval_seats > 36:
                six_00.aval_tables = 4
            elif six_00.aval_seats > 24:
                six_00.aval_tables = 3
            elif six_00.aval_seats > 12:
                six_00.aval_tables = 2
            elif six_00.aval_seats > 0:
                six_00.aval_tables = 1
            else:
                six_00.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(six_00.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(six_00.aval_tables)}')
        return int(six_00.aval_seats)    

    def disp_res_aval_630(self):
        six_30 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '6:30':
                        six_30.aval_seats -= int(line[1])
                print(six_30.aval_seats)

            if six_30.aval_seats > 48:
                six_30.aval_tables = 5
            elif six_30.aval_seats > 36:
                six_30.aval_tables = 4
            elif six_30.aval_seats > 24:
                six_30.aval_tables = 3
            elif six_30.aval_seats > 12:
                six_30.aval_tables = 2
            elif six_30.aval_seats > 0:
                six_30.aval_tables = 1
            else:
                six_30.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(six_30.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(six_30.aval_tables)}')
        return int(six_30.aval_seats)    

    def disp_res_aval_700(self):
        seven_00 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '7:00':
                        seven_00.aval_seats -= int(line[1])
                print(seven_00.aval_seats)

            if seven_00.aval_seats > 48:
                seven_00.aval_tables = 5
            elif seven_00.aval_seats > 36:
                seven_00.aval_tables = 4
            elif seven_00.aval_seats > 24:
                seven_00.aval_tables = 3
            elif seven_00.aval_seats > 12:
                seven_00.aval_tables = 2
            elif seven_00.aval_seats > 0:
                seven_00.aval_tables = 1
            else:
                seven_00.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(seven_00.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(seven_00.aval_tables)}')                    
        return int(seven_00.aval_seats)    
                
    def disp_res_aval_730(self):
        seven_30 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '7:30':
                        seven_30.aval_seats -= int(line[1])
                print(seven_30.aval_seats)

            if seven_30.aval_seats > 48:
                seven_30.aval_tables = 5
            elif seven_30.aval_seats > 36:
                seven_30.aval_tables = 4
            elif seven_30.aval_seats > 24:
                seven_30.aval_tables = 3
            elif seven_30.aval_seats > 12:
                seven_30.aval_tables = 2
            elif seven_30.aval_seats > 0:
                seven_30.aval_tables = 1
            else:
                seven_30.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(seven_30.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(seven_30.aval_tables)}')
        return int(seven_30.aval_seats)    

    def disp_res_aval_800(self):
        eight_00 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '8:00':
                        eight_00.aval_seats -= int(line[1])
                print(eight_00.aval_seats)

            if eight_00.aval_seats > 48:
                eight_00.aval_tables = 5
            elif eight_00.aval_seats > 36:
                eight_00.aval_tables = 4
            elif eight_00.aval_seats > 24:
                eight_00.aval_tables = 3
            elif eight_00.aval_seats > 12:
                eight_00.aval_tables = 2
            elif eight_00.aval_seats > 0:
                eight_00.aval_tables = 1
            else:
                eight_00.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(eight_00.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(eight_00.aval_tables)}')
        return int(eight_00.aval_seats)    

    def disp_res_aval_830(self):
        eight_30 = Reservation()
            
        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        if os.path.isfile(res_path):
            with open(res_path, 'r') as csvfile:
                content = csv.reader(csvfile,delimiter =',')
                for line in content:
                    if line[2] == '8:30':
                        eight_30.aval_seats -= int(line[1])
                print(eight_30.aval_seats)

            if eight_30.aval_seats > 48:
                eight_30.aval_tables = 5
            elif eight_30.aval_seats > 36:
                eight_30.aval_tables = 4
            elif eight_30.aval_seats > 24:
                eight_30.aval_tables = 3
            elif eight_30.aval_seats > 12:
                eight_30.aval_tables = 2
            elif eight_30.aval_seats > 0:
                eight_30.aval_tables = 1
            else:
                eight_30.aval_tables = 0

        self.avail_seats.setText(f'Available Seats: {int(eight_30.aval_seats)}')
        self.avail_tables.setText(f'Available Tables: {int(eight_30.aval_tables)}')
        return int(eight_30.aval_seats)    

    res_functions = [disp_res_aval_400, disp_res_aval_430, disp_res_aval_500, disp_res_aval_530, disp_res_aval_600, disp_res_aval_630, disp_res_aval_700, disp_res_aval_730, disp_res_aval_800, disp_res_aval_830]

    def set_new_res(self):
        input_name = self.new_name.text().strip()
        input_phone = int(self.new_number.text().strip())
        input_size = int(self.new_size.text().strip())

        date_selected = self.new_calender.selectedDate()
        date = str(date_selected.toString())
        date_lst = date.split(' ')
        if int(date_lst[2]) < 10:
            res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)
        else:
            res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'
            #print(res_path)

        
        if os.path.isfile(res_path):
            if self.rad_400.isChecked() == True:
                aval_seats = self.disp_res_aval_400()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '4:00', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_400()
                    self.grab_date_new_res()
            
            elif self.rad_430.isChecked() == True:
                aval_seats = self.disp_res_aval_430()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '4:30', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_430()
                    self.grab_date_new_res()
            elif self.rad_500.isChecked() == True:
                aval_seats = self.disp_res_aval_500()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '5:00',input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_500()
                    self.grab_date_new_res()

            elif self.rad_530.isChecked() == True:
                aval_seats = self.disp_res_aval_530()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '5:30', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_530()
                    self.grab_date_new_res()

            elif self.rad_600.isChecked() == True:
                aval_seats = self.disp_res_aval_600()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '6:00', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_600()
                    self.grab_date_new_res()


            elif self.rad_630.isChecked() == True:
                aval_seats = self.disp_res_aval_630()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '6:30', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_630()
                    self.grab_date_new_res()

            elif self.rad_700.isChecked() == True:
                aval_seats = self.disp_res_aval_700()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '7:00', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_700()
                    self.grab_date_new_res()

            elif self.rad_730.isChecked() == True:
                aval_seats = self.disp_res_aval_730()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '7:30', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_730()
                    self.grab_date_new_res()


            elif self.rad_800.isChecked() == True:
                aval_seats = self.disp_res_aval_800()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '8:00', input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_800()
                    self.grab_date_new_res()

            elif self.rad_830.isChecked() == True:
                aval_seats = self.disp_res_aval_830()
                if input_size > aval_seats:
                    self.new_res_output_label.setText('Party Size > Current Available Seating')
                else:
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '8:30',input_phone]
                        content.writerow(entry)
                    self.disp_res_aval_830()
                    self.grab_date_new_res()
            else:
                self.new_res_output_label.setText('Please Select A Time Slot.')

        else:
            radios = [self.rad_400, self.rad_430, self.rad_500, self.rad_530, self.rad_600, self.rad_630, self.rad_700, self.rad_730, self.rad_800, self.rad_830]
            for radio in radios:
                if radio.isChecked():
                    with open(res_path, 'a', newline='') as csvfile:
                        content = csv.writer(csvfile)
                        entry = [input_name, input_size, '8:30',input_phone]
                        content.writerow(entry)
                    self.grab_date_new_res()
                    break
                self.new_res_output_label.setText('Please Select A Time Slot.')

    def del_res(self):
        try:
            self.edit_output_label.setText('')
            input_name = self.edit_name.text().strip()
            input_size = self.edit_size.text().strip()
            input_phone = self.edit_phone.text().strip()
            input_time = self.edit_time.text().strip()   
            date_selected = self.edit_calender.selectedDate()

            error_catch_size = int(input_size)

            if (len(input_name) == 0):
                raise RuntimeError
            if input_time not in time_slots:
                raise IndexError
            if  (0 < len(input_phone) < 10):
                raise ValueError
            elif (len(input_phone) > 10):
                raise ValueError
            
            

            date = str(date_selected.toString())
            date_lst = date.split(' ')
            if int(date_lst[2]) < 10:
                res_path = f'Reservations/{date_lst[1]}-{str(0) + date_lst[2]}-{date_lst[3]}.csv'
                #print(res_path)
            else:
                res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'        
            if os.path.isfile(res_path):
                lines = []
                with open(res_path, 'r') as csvfile:
                    content = csv.reader(csvfile,delimiter =',')
                    for line in content:
                        if line[0] == input_name and line[1] == input_size and line[2] == input_time:
                            self.edit_output_label.setText('Reservation Successfully Deleted')
                            continue
                        else:
                            lines.append(line)
                
                with open(res_path, 'w', newline='') as csvfile:
                    content = csv.writer(csvfile)
                    for line in lines:
                        content.writerow(line)
                self.grab_date_edit_res()
                self.edit_name.setText('')
                self.edit_size.setText('')
                self.edit_time.setText('')
                self.edit_phone.setText('')
            
        
        except RuntimeError:
            self.edit_output_label.setText('Please Fill In Name * Field.')
        except ValueError:
            self.edit_output_label.setText('Please Enter (10) or (ZERO) Digit Phone Number for Phone Number Field. Please Enter Numbers for Party Size.')
        except IndexError:
            self.edit_output_label.setText('Please Enter Valid Time Slot (4:00 PM ---> 8:30 PM), in 30 min incraments.')
        except TypeError:
            self.edit_output_label.setText('Reservation Does Not Exist.')

    def set_res(self):
        try:           
            input_name = self.edit_name.text().strip()
            input_size = self.edit_size.text().strip()
            input_phone = self.edit_phone.text().strip()
            input_time = self.edit_time.text().strip()

            new_name = self.edit_new_name.text().strip()
            new_size = self.edit_new_size.text().strip()
            new_time = self.edit_new_time.text().strip()
            new_phone = self.edit_new_number.text().strip()

            error_catch_size = int(input_size)
            error_catch_phone = int(input_size)
            error_catch_size2 = int(new_size)
            
            if (len(input_name) == 0) or (len(new_name) == 0):
                raise KeyError

            if  (0 < len(input_phone) < 10):
                raise TypeError
            elif (len(input_phone) > 10):
                raise TypeError

            if  (0 < len(new_phone) < 10):
                raise TypeError
            elif (len(new_phone) > 10):
                raise TypeError

            if input_time not in time_slots or (new_time not in time_slots):
                raise IndexError
            
            

            date_selected = self.edit_calender.selectedDate()
            date = str(date_selected.toString())
            date_lst = date.split(' ')
            if int(date_lst[2]) < 10:
                res_path = f'Reservations/{date_lst[1]}-{str(0)+ date_lst[2]}-{date_lst[3]}.csv'
                #print(res_path)
            else:
                res_path = f'Reservations/{date_lst[1]}-{date_lst[2]}-{date_lst[3]}.csv'

            if os.path.isfile(res_path):
                
                lines = []
                with open(res_path, 'r') as csvfile:
                    content = csv.reader(csvfile,delimiter =',')
                    for line in content:
                        if line[0] == input_name and line[1] == input_size and line[2] == input_time:    
                            if new_time in time_slots:
                                if new_time == input_time:
                                    item_index = time_slots.index(new_time)
                                    new_difference = int(input_size) - int(new_size)
                                    print(self.res_functions[item_index](self))
                                    if (self.res_functions[item_index](self) + new_difference) < 0:
                                        raise RuntimeError(f'{self.res_functions[item_index](self)}')
                                    else:
                                        new_entry = [new_name, new_size, new_time, new_phone]
                                        lines.append(new_entry)
                                else:
                                    new_item_index = time_slots.index(new_time)
                                    if self.res_functions[new_item_index](self) < int(new_size):
                                        raise RuntimeError(f'{self.res_functions[new_item_index](self)}')    
                                    else:
                                        new_entry = [new_name, new_size, new_time, new_phone]
                                        lines.append(new_entry)                      
                        else:
                            lines.append(line)      
                with open(res_path, 'w', newline='') as csvfile:
                    content = csv.writer(csvfile)
                    for line in lines:
                        content.writerow(line)
                self.grab_date_edit_res()
                self.edit_name.setText('')
                self.edit_size.setText('')
                self.edit_time.setText('')
                self.edit_phone.setText('')
                self.edit_new_name.setText('')
                self.edit_new_number.setText('')
                self.edit_new_size.setText('')
                self.edit_new_time.setText('')
                self.edit_new_number.setText('')

        except TypeError:
            self.edit_output_label.setText('Please Enter a (10) Digit Phone Number Phone Numbers OR NO PHONE NUMBER.')
        except IndexError:
            self.edit_output_label.setText('Please Enter Valid Time Slot (4:00 PM ---> 8:30 PM), in 30 min incraments.')

        except RuntimeError as e:
            self.edit_output_label.setText(f'Time Slot Currently has {e} Available Seats. Not Enough Space.')   
        
        except KeyError:
            self.edit_output_label.setText(f'Please Fill In All Name Fields.')
        
        except ValueError:
            self.edit_output_label.setText(f'Please Enter Numbers for (Party Size) Fields.')


