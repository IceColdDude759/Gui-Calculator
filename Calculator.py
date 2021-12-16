from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt



class Ui_Calculator(object):

    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(487, 340)
        Calculator.setWindowIcon(QtGui.QIcon('iicon.png'))
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(10,self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 486, 91))
        self.lcdNumber.setStyleSheet("QLCDNumber {color: blue;}")
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 100, 81, 51))
        self.pushButton_7.setFont(QFont('Arial', 17))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 100, 91, 51))
        self.pushButton_8.setFont(QFont('Arial', 17))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 100, 91, 51))
        self.pushButton_9.setFont(QFont('Arial', 17))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 160, 91, 51))
        self.pushButton_6.setFont(QFont('Arial', 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 160, 81, 51))
        self.pushButton_4.setFont(QFont('Arial', 17))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 160, 91, 51))
        self.pushButton_5.setFont(QFont('Arial', 17))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 220, 91, 51))
        self.pushButton_3.setFont(QFont('Arial', 17))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 220, 81, 51))
        self.pushButton_1.setFont(QFont('Arial', 17))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 220, 91, 51))
        self.pushButton_2.setFont(QFont('Arial', 17))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(200, 280, 91, 51))
        self.pushButton_10.setFont(QFont('Arial', 20))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 280, 81, 51))
        self.pushButton_11.setFont(QFont('Arial', 15))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(100, 280, 91, 51))
        self.pushButton_0.setFont(QFont('Arial', 17))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_plu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plu.setGeometry(QtCore.QRect(400, 220, 81, 51))
        self.pushButton_plu.setFont(QFont('Arial', 17))
        self.pushButton_plu.setObjectName("pushButton_plu")
        c_effect = QGraphicsColorizeEffect() 
        c_effect.setColor(Qt.blue) 
        self.pushButton_eql = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_eql.setGeometry(QtCore.QRect(300, 280, 181, 51))
        self.pushButton_eql.setObjectName("pushButton_eql")
        self.pushButton_eql.setGraphicsEffect(c_effect)
        self.pushButton_eql.setFont(QFont('Arial', 25))
        self.pushButton_sub = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sub.setGeometry(QtCore.QRect(300, 220, 91, 51))
        self.pushButton_sub.setFont(QFont('Arial', 17))
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_mul = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mul.setGeometry(QtCore.QRect(400, 160, 81, 51))
        self.pushButton_mul.setFont(QFont('Arial', 17))
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_bac = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bac.setGeometry(QtCore.QRect(300, 100, 181, 51))
        self.pushButton_bac.setObjectName("pushButton_bac")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(300, 160, 91, 51))
        self.pushButton_div.setFont(QFont('Arial', 17))
        self.pushButton_div.setObjectName("pushButton_div")
        Calculator.setCentralWidget(self.centralwidget)
             

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

        
        

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.pushButton_7.setText(_translate("Calculator", "7"))
        self.pushButton_8.setText(_translate("Calculator", "8"))
        self.pushButton_9.setText(_translate("Calculator", "9"))
        self.pushButton_6.setText(_translate("Calculator", "6"))
        self.pushButton_4.setText(_translate("Calculator", "4"))
        self.pushButton_5.setText(_translate("Calculator", "5"))
        self.pushButton_3.setText(_translate("Calculator", "3"))
        self.pushButton_1.setText(_translate("Calculator", "1"))
        self.pushButton_2.setText(_translate("Calculator", "2"))
        self.pushButton_10.setText(_translate("Calculator", "."))
        self.pushButton_11.setText(_translate("Calculator", "+/-"))
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_plu.setText(_translate("Calculator", "+"))
        self.pushButton_eql.setText(_translate("Calculator", "="))
        self.pushButton_sub.setText(_translate("Calculator", "-"))
        self.pushButton_mul.setText(_translate("Calculator", "*"))
        self.pushButton_div.setText(_translate("Calculator", "/"))
        self.pushButton_bac.setIcon(QtGui.QIcon('image.png'))
        self.pushButton_bac.setIconSize(QtCore.QSize(200,200))



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.click()
        self.decimal=0
        self.equation=''
        self.back=0


    def click(self):
        self.ui.pushButton_0.clicked.connect(self.a0)
        self.ui.pushButton_1.clicked.connect(self.a1)
        self.ui.pushButton_2.clicked.connect(self.a2)
        self.ui.pushButton_3.clicked.connect(self.a3)
        self.ui.pushButton_4.clicked.connect(self.a4)
        self.ui.pushButton_5.clicked.connect(self.a5)
        self.ui.pushButton_6.clicked.connect(self.a6)
        self.ui.pushButton_7.clicked.connect(self.a7)
        self.ui.pushButton_8.clicked.connect(self.a8)
        self.ui.pushButton_9.clicked.connect(self.a9)
        self.ui.pushButton_10.clicked.connect(self.dot)
        self.ui.pushButton_11.clicked.connect(self.neg)
        self.ui.pushButton_plu.clicked.connect(self.add)
        self.ui.pushButton_sub.clicked.connect(self.sub)
        self.ui.pushButton_mul.clicked.connect(self.mul)
        self.ui.pushButton_div.clicked.connect(self.div)
        self.ui.pushButton_eql.clicked.connect(self.eql)
        self.ui.pushButton_bac.clicked.connect(self.bac)
       

        
    def eql(self):
        try:
            self.decimal=0
            self.equation=self.equation+str(self.ui.lcdNumber.value())
            res=eval(self.equation)
            self.equation=""
            self.ui.lcdNumber.display(res)
        except :
            self.ui.lcdNumber.display(0)
    
    def bac(self):
        digits=str(self.ui.lcdNumber.value())
        
        if digits==0:
            digits=0
        else:
            if self.back>4:
                self.back=0
                digits=0
                self.decimal=0
            elif self.decimal>0:
                digits=digits[:-1]
                self.back+=1
            else:
                digits=digits[:-3]
                self.back+=0.7
        self.ui.lcdNumber.display(digits)
    
    def div(self):
        self.decimal=0
        self.equation=self.equation+str(self.ui.lcdNumber.value())+"/"
        self.ui.lcdNumber.display(0)
    
    def mul(self):
        self.decimal=0
        self.equation=self.equation+str(self.ui.lcdNumber.value())+"*"
        self.ui.lcdNumber.display(0)
    
    def add(self):
        self.decimal=0
        self.equation=self.equation+str(self.ui.lcdNumber.value())+"+"
        self.ui.lcdNumber.display(0)
    
    def sub(self):
        self.decimal=0
        self.equation=self.equation+str(self.ui.lcdNumber.value())+"-"
        self.ui.lcdNumber.display(0)
    
    def neg(self):
        digits=str(self.ui.lcdNumber.value())
        if (digits[0]=='-'):
            self.ui.lcdNumber.display(int(digits[1:-2]))
        else :
            self.ui.lcdNumber.display(int("-"+digits[:-2]))

    def dot(self):
        digits=str(self.ui.lcdNumber.value())
        digits=digits[:-2]+"."
        self.ui.lcdNumber.display(digits)
        self.ui.lcdNumber.setSmallDecimalPoint(0)
        self.decimal=1


    def a0(self):
        digits=self.ui.lcdNumber.value()*10 +0.00000
        if self.decimal>0:
            digits=self.ui.lcdNumber.value() +float(0/pow(10,self.decimal))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a1(self):
        digits=self.ui.lcdNumber.value()*10 +1
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(1/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a2(self):
        digits=self.ui.lcdNumber.value()*10 +2
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(2/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a3(self):
        digits=self.ui.lcdNumber.value()*10 +3
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(3/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a4(self):
        digits=self.ui.lcdNumber.value()*10 +4
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(4/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a5(self):
        digits=self.ui.lcdNumber.value()*10 +5
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(5/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a6(self):
        digits=self.ui.lcdNumber.value()*10 +6
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(6/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a7(self):
        digits=self.ui.lcdNumber.value()*10 +7
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(7/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a8(self):
        digits=self.ui.lcdNumber.value()*10 +8
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(8/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)

    def a9(self):
        digits=self.ui.lcdNumber.value()*10 +9
        if self.decimal>0:
            digits=float(self.ui.lcdNumber.value() +float(9/pow(10,self.decimal)))
            self.decimal+=1
        self.ui.lcdNumber.display(digits)


    def keyPressEvent(self, event):
        #print(event.key())
        
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.eql()  
        if event.key() == Qt.Key_Backspace:
            self.bac()
        if event.key() == Qt.Key_Plus:
            self.add()
        if event.key() == Qt.Key_Minus:
            self.sub()
        if event.key() == Qt.Key_Asterisk:
            self.mul()
        if event.key() == Qt.Key_Slash or event.key() == Qt.Key_Backslash:
            self.div()
       

        if event.key() == Qt.Key_0:
            self.a0()
        if event.key() == Qt.Key_1:
            self.a1()
        if event.key() == Qt.Key_2:
            self.a2()
        if event.key() == Qt.Key_3:
            self.a3()
        if event.key() == Qt.Key_4:
            self.a4()
        if event.key() == Qt.Key_5:
            self.a5()
        if event.key() == Qt.Key_6:
            self.a6()
        if event.key() == Qt.Key_7:
            self.a7()
        if event.key() == Qt.Key_8:
            self.a8()
        if event.key() == Qt.Key_9:
            self.a9()
        

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Window()
    MainWindow.show()
    sys.exit(app.exec())