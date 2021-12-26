from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

#====================================Login System====================================
class LoginSystem(object):
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
                
                self.button_login.clicked.connect(self.login)
                self.button_register.clicked.connect(self.register_account)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle("Login System")
                self.label_2.setText(_translate("MainWindow", "LOGIN HERE"))
                self.label_3.setText(_translate("MainWindow", "Username"))
                self.label_4.setText(_translate("MainWindow", "Password"))
                self.button_login.setText(_translate("MainWindow", "Login"))
                self.password.setPlaceholderText(_translate("MainWindow", "password"))
                self.username.setPlaceholderText(_translate("MainWindow", "username"))
                self.button_register.setText(_translate("MainWindow", "Register"))
        
        def register_account(self):
                MainWindow.close()
                self.window = QtWidgets.QMainWindow()
                self.ui = RegisterAccount()
                self.ui.setupUi(self.window)
                self.window.show()
                
        def login(self):
                self.username_enter = self.username.text()
                self.password_enter = self.password.text()
                
                print(self.username_enter, self.password_enter)
                
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
                
                self.button_register.clicked.connect(self.register_user)

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
                
        def register_user(self):
                self.username_enter = self.username.text()
                self.password_enter = self.password.text()
                self.repeat_password_enter = self.repeat_password.text()
                self.name_enter = self.name.text().lower()

                self.error_with_data = []
                
                if len(self.username_enter) < 3:
                        self.error_with_data.append("• A valid username hasn't entered")
                
                if self.password_enter != self.repeat_password_enter:
                        self.error_with_data.append("• Passwords do not match")
                        
                if len(self.password_enter) < 3:
                        print("password")
                        self.error_with_data.append("• A valid password hasn't been entered")
                
                if len(self.name_enter) < 1:
                        print("name")
                        self.error_with_data.append("• A name has been entered")
                
                if len(self.error_with_data) > 0:
                        msg = QMessageBox()
                        msg.setWindowTitle("Invalid data")
                        msg.setText("Following errors that have occured: ")
                        
                        error_message = ""
                        i = 0
                        for i in range(len(self.error_with_data)):
                                error_message += self.error_with_data[i] + "\n"
                                
                        msg.setIcon(QMessageBox.Critical)
                        msg.setStandardButtons(QMessageBox.Retry)
                        msg.setInformativeText(error_message)
                        x = msg.exec_()
                else:
                        self.name_enter = self.name_enter[0].upper() + self.name_enter[1].lower()
                        pass
                        #to database
                        
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = LoginSystem()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
