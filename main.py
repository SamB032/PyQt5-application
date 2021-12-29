from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import backend

#====================================Login System====================================
class LoginSystem(object):
        
        logged_user_id = 0
        
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(845, 487)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-70, -30, 971, 551))
                self.label.setAutoFillBackground(False)
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("static/pebble.jpeg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(270, 70, 301, 341))
                self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 127); \n"
        "border: rgba(0, 0, 0, 127);\n"
        "border-radius: 20px;")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(90, 10, 131, 31))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 16pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(50, 60, 81, 16))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(50, 130, 81, 16))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_4.setObjectName("label_4")
                self.button_login = QtWidgets.QPushButton(self.frame)
                self.button_login.setGeometry(QtCore.QRect(80, 210, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.button_login.setFont(font)
                self.button_login.setStyleSheet("background-color: rgb(224, 27, 36);\n"
        "color: rgb(255, 255, 255);")
                self.button_login.setObjectName("button_login")
                self.password = QtWidgets.QLineEdit(self.frame)
                self.password.setGeometry(QtCore.QRect(50, 160, 201, 31))
                self.password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.password.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.password.setObjectName("password")
                self.username = QtWidgets.QLineEdit(self.frame)
                self.username.setGeometry(QtCore.QRect(50, 90, 201, 31))
                self.username.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.username.setObjectName("username")
                self.button_register = QtWidgets.QPushButton(self.frame)
                self.button_register.setGeometry(QtCore.QRect(80, 280, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.button_register.setFont(font)
                self.button_register.setStyleSheet("background-color: rgb(224, 27, 36);\n"
        "color: rgb(255, 255, 255);")
                self.button_register.setObjectName("button_register")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(-3, -3, 861, 501))
                self.label_5.setText("")
                self.label_5.setPixmap(QtGui.QPixmap("pebble.jpeg"))
                self.label_5.setScaledContents(True)
                self.label_5.setObjectName("label_5")
                self.label_5.raise_()
                self.label.raise_()
                self.frame.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                
                self.button_login.clicked.connect(lambda : self.login(MainWindow))
                self.button_register.clicked.connect(lambda : self.register_account(MainWindow))

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle("Login System")
                self.label_2.setText(_translate("MainWindow", " Login here"))
                self.label_3.setText(_translate("MainWindow", "Username"))
                self.label_4.setText(_translate("MainWindow", "Password"))
                self.button_login.setText(_translate("MainWindow", "Login"))
                self.password.setPlaceholderText(_translate("MainWindow", "password"))
                self.username.setPlaceholderText(_translate("MainWindow", "username"))
                self.button_register.setText(_translate("MainWindow", "Register"))
        
        def register_account(self, MainWindow):
                MainWindow.hide()
                self.window = QtWidgets.QMainWindow()
                self.ui = RegisterAccount()
                self.ui.setupUi(self.window)
                self.window.show()

        def login(self, MainWindow):
                self.username_enter = self.username.text()
                self.password_enter = self.password.text()
                
                self.is_correct_details = backend.UserTable.check_credentials(self.username_enter, self.password_enter)
                self.login_bool = self.is_correct_details[0]

                msg = QMessageBox()

                if self.login_bool == True:
                        msg.setWindowTitle("Success")
                        msg.setText("Logging in....")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        x = msg.exec_()
                        
                        LoginSystem.record_user(self.is_correct_details[1])
                        
                        MainWindow.hide()
                        self.window = QtWidgets.QMainWindow()
                        self.ui = NoteWindow()
                        self.ui.setupUi(self.window)                        
                        self.window.show()
                else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Incorrect username and/or Password")          
                        msg.setIcon(QMessageBox.Critical)
                        msg.setStandardButtons(QMessageBox.Retry)
                        x = msg.exec_()   
                        
        @classmethod
        def record_user(cls, user_id):
                cls.logged_user_id = user_id
              
#====================================Register Account====================================
class RegisterAccount(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(845, 487)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-70, -30, 971, 551))
                self.label.setAutoFillBackground(False)
                self.label.setText("")
                self.label.setPixmap(QtGui.QPixmap("static/pebble.jpeg"))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(270, 50, 311, 411))
                self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 127); \n"
        "border: rgba(0, 0, 0, 127);\n"
        "border-radius: 20px;")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(70, 10, 161, 31))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 16pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_2.setObjectName("label_2")
                self.label_3 = QtWidgets.QLabel(self.frame)
                self.label_3.setGeometry(QtCore.QRect(50, 60, 81, 16))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_3.setObjectName("label_3")
                self.label_4 = QtWidgets.QLabel(self.frame)
                self.label_4.setGeometry(QtCore.QRect(50, 130, 81, 16))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_4.setFont(font)
                self.label_4.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_4.setObjectName("label_4")
                self.password = QtWidgets.QLineEdit(self.frame)
                self.password.setGeometry(QtCore.QRect(50, 160, 201, 31))
                self.password.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.password.setObjectName("password")
                self.username = QtWidgets.QLineEdit(self.frame)
                self.username.setGeometry(QtCore.QRect(50, 90, 201, 31))
                self.username.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.username.setObjectName("username")
                self.button_register = QtWidgets.QPushButton(self.frame)
                self.button_register.setGeometry(QtCore.QRect(80, 350, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.button_register.setFont(font)
                self.button_register.setStyleSheet("background-color: rgb(224, 27, 36);\n"
        "color: rgb(255, 255, 255);")
                self.button_register.setObjectName("button_register")
                self.label_7 = QtWidgets.QLabel(self.frame)
                self.label_7.setGeometry(QtCore.QRect(50, 200, 121, 21))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_7.setFont(font)
                self.label_7.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_7.setObjectName("label_7")
                self.repeat_password = QtWidgets.QLineEdit(self.frame)
                self.repeat_password.setGeometry(QtCore.QRect(50, 230, 201, 31))
                self.repeat_password.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.repeat_password.setText("")
                self.repeat_password.setObjectName("repeat_password")
                self.label_6 = QtWidgets.QLabel(self.frame)
                self.label_6.setGeometry(QtCore.QRect(50, 270, 81, 16))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(12)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_6.setObjectName("label_6")
                self.name = QtWidgets.QLineEdit(self.frame)
                self.name.setGeometry(QtCore.QRect(50, 300, 201, 31))
                self.name.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.name.setText("")
                self.name.setObjectName("name")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(-3, -3, 861, 501))
                self.label_5.setText("")
                self.label_5.setPixmap(QtGui.QPixmap("pebble.jpeg"))
                self.label_5.setScaledContents(True)
                self.label_5.setObjectName("label_5")
                self.label_5.raise_()
                self.label.raise_()
                self.frame.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                
                self.password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.repeat_password.setEchoMode(QtWidgets.QLineEdit.Password)
                
                self.button_register.clicked.connect(lambda : self.register_user(MainWindow))

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle("Sign Up")
                self.label_2.setText(_translate("MainWindow", "Register Account"))
                self.label_3.setText(_translate("MainWindow", "Username"))
                self.label_4.setText(_translate("MainWindow", "Password"))
                self.password.setPlaceholderText(_translate("MainWindow", "password"))
                self.username.setPlaceholderText(_translate("MainWindow", "username"))
                self.button_register.setText(_translate("MainWindow", "Register"))
                self.label_7.setText(_translate("MainWindow", "Repeat Password"))
                self.repeat_password.setPlaceholderText(_translate("MainWindow", "repeat password"))
                self.label_6.setText(_translate("MainWindow", "Name"))
                self.name.setPlaceholderText(_translate("MainWindow", "name"))
   
        def register_user(self, MainWindow):
                self.username_enter = self.username.text()
                self.password_enter = self.password.text()
                self.repeat_password_enter = self.repeat_password.text()
                self.name_enter = self.name.text().lower()

                self.error_message = ""
                
                if len(self.username_enter) < 3:
                        self.error_message += "• A valid username hasn't entered\n"
                
                if backend.UserTable.user_name_exsist(self.username_enter) == True:
                        self.error_message +="• Username has already been taken\n"
                
                if self.password_enter != self.repeat_password_enter:
                        self.error_message += "• Passwords do not match\n"
                        
                if len(self.password_enter) < 3:
                        self.error_message += "• A valid password hasn't been entered\n"
                
                if len(self.name_enter) < 1:
                        self.error_message += "• A name hasn't been entered\n"
                
                if self.error_message != "":
                        msg = QMessageBox()
                        msg.setWindowTitle("Invalid data")
                        msg.setText("Following errors that have occured: ")                                
                        msg.setIcon(QMessageBox.Critical)
                        msg.setStandardButtons(QMessageBox.Retry)
                        msg.setInformativeText(self.error_message)
                        x = msg.exec_()
                else:
                        self.name_enter = self.name_enter[0].upper() + self.name_enter[1:].lower()
                        backend.UserTable().insert(self.name_enter, self.username_enter, self.password_enter)
                        
                        msg = QMessageBox()
                        msg.setWindowTitle("Account Created")
                        msg.setText("The account has been created, please login")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        x = msg.exec_()
                        
                        MainWindow.hide()
                        self.window = QtWidgets.QMainWindow()
                        self.ui = LoginSystem()
                        self.ui.setupUi(self.window)
                        self.window.show()
                        
class NoteWindow():
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(845, 487)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-10, -10, 1011, 591))
                self.label.setAutoFillBackground(False)
                self.label.setText("")
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(120, 60, 601, 401))
                self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 127); \n"
        "border: rgba(0, 0, 0, 127);\n"
        "border-radius: 20px;")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label_2 = QtWidgets.QLabel(self.frame)
                self.label_2.setGeometry(QtCore.QRect(270, 10, 61, 31))
                font = QtGui.QFont()
                font.setFamily("Noto Sans Khmer UI")
                font.setPointSize(16)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
        "border: rgba(0, 0, 0, 0);\n"
        "font: 75 16pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.label_2.setObjectName("label_2")
                self.button_delete = QtWidgets.QPushButton(self.frame)
                self.button_delete.setGeometry(QtCore.QRect(230, 340, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.button_delete.setFont(font)
                self.button_delete.setStyleSheet("background-color: rgb(224, 27, 36);\n"
        "color: rgb(255, 255, 255);")
                self.button_delete.setObjectName("button_delete")
                self.note_list = QtWidgets.QListWidget(self.frame)
                self.note_list.setGeometry(QtCore.QRect(40, 60, 521, 192))
                self.note_list.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.note_list.setObjectName("note_list")
                self.button_create = QtWidgets.QPushButton(self.frame)
                self.button_create.setGeometry(QtCore.QRect(50, 340, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.button_create.setFont(font)
                self.button_create.setStyleSheet("background-color: rgb(224, 27, 36);\n"
        "color: rgb(255, 255, 255);")
                self.button_create.setObjectName("button_create")
                self.note_box = QtWidgets.QLineEdit(self.frame)
                self.note_box.setGeometry(QtCore.QRect(40, 260, 521, 61))
                self.note_box.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.note_box.setObjectName("note_box")
                self.button_logout = QtWidgets.QPushButton(self.frame)
                self.button_logout.setGeometry(QtCore.QRect(410, 340, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.button_logout.setFont(font)
                self.button_logout.setStyleSheet("background-color: rgb(224, 27, 36);\n"
        "color: rgb(255, 255, 255);")
                self.button_logout.setObjectName("button_logout")
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(-3, -3, 861, 501))
                self.label_5.setText("")
                self.label_5.setPixmap(QtGui.QPixmap("static/pebble.jpeg"))
                self.label_5.setScaledContents(True)
                self.label_5.setObjectName("label_5")
                self.label_5.raise_()
                self.label.raise_()
                self.frame.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                
                self.button_create.clicked.connect(self.create_note)
                self.button_delete.clicked.connect(self.delete_note)
                self.button_logout.clicked.connect(lambda : self.logout(MainWindow))
                
                self.check_list()

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle("My Notes")
                self.label_2.setText(_translate("MainWindow", "Notes"))
                self.button_delete.setText(_translate("MainWindow", "Delete Note"))
                self.button_create.setText(_translate("MainWindow", "Create Note"))
                self.button_logout.setText(_translate("MainWindow", "Logout"))
        
        def create_note(self):
                self.note = self.note_box.text()
                if self.note == "":
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("A note hasn't been written")          
                        msg.setIcon(QMessageBox.Critical)
                        msg.setStandardButtons(QMessageBox.Retry)
                        x = msg.exec_()   
                else:   
                        backend.NoteTable().insert(self.note, LoginSystem.logged_user_id)
                        self.note_box.setText("")
                        self.check_list()
        
        def delete_note(self):
                try:
                        self.note_selected = self.note_list.currentItem().text()
                        self.note_is_selected = True
                except AttributeError:
                        self.note_is_selected = False
                
                if self.note_is_selected == True:
                        
                        msg = QMessageBox()
                        msg.setWindowTitle("Delete Note")
                        msg.setText("Would you like to delete selected note?")          
                        msg.setIcon(QMessageBox.Warning)
                        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
                        msg.setDefaultButton(QMessageBox.Cancel)
                        
                        x = msg.exec_()  
                        
                        if msg.clickedButton().text() == "&Yes":        
                                backend.NoteTable().delte_note(self.note_selected.split(".")[0])
                                self.check_list()
                else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("A note hasn't been selected")          
                        msg.setIcon(QMessageBox.Critical)
                        msg.setStandardButtons(QMessageBox.Retry)
                        x = msg.exec_()   
                
        def check_list(self):
                self.note_list.clear()
                self.query = backend.NoteTable().return_user_notes(LoginSystem.logged_user_id)
                try : 
                        for row in self.query:
                                self.note_list.addItem(QtWidgets.QListWidgetItem(f'{row.note_id}.   {row.data}'))
                except:
                        pass
                
        def logout(self, MainWindow):
                MainWindow.hide()
                self.window = QtWidgets.QMainWindow()
                self.ui = LoginSystem()
                self.ui.setupUi(self.window)
                self.window.show()
                        
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = LoginSystem()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
