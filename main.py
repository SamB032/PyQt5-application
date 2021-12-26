from PyQt5 import QtCore, QtGui, QtWidgets

#====================================Login System====================================
class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(845, 487)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(-70, -30, 971, 551))
                self.label.setAutoFillBackground(False)
                self.label.setText("")
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(270, 70, 301, 331))
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
                self.label_4.setGeometry(QtCore.QRect(50, 150, 81, 16))
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
                self.button_login.setGeometry(QtCore.QRect(80, 250, 141, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(False)
                font.setWeight(50)
                self.button_login.setFont(font)
                self.button_login.setStyleSheet("background-color: rgb(224, 27, 36);\n"
        "color: rgb(255, 255, 255);")
                self.button_login.setObjectName("button_login")
                self.password = QtWidgets.QLineEdit(self.frame)
                self.password.setGeometry(QtCore.QRect(50, 180, 201, 31))
                self.password.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.password.setObjectName("password")
                self.password.setEchoMode(QtWidgets.QLineEdit.Password)
                self.username = QtWidgets.QLineEdit(self.frame)
                self.username.setGeometry(QtCore.QRect(50, 90, 201, 31))
                self.username.setStyleSheet("font: 75 12pt \"Noto Sans Khmer UI\";\n"
        "color: rgb(255, 255, 255);")
                self.username.setObjectName("username")
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
                
                self.button_login.clicked.connect(self.login)

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

        def login(self):
                self.username_enter = self.username.text()
                self.password_enter = self.password.text()
                
                print(self.username_enter, self.password_enter)
                
#====================================Main Menu====================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
