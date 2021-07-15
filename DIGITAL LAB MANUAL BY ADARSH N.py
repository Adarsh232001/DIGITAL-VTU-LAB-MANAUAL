import sys,os,webbrowser
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QComboBox
from PyQt5.QtGui import  QStandardItemModel, QStandardItem, QFont, QTextOption
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

data = {
    'C PROGRAMMING LABORATORY(18CPL17/27)': ["1.Basics of C","2.Commercial Calculator","3.Roots of Quadratic Equation",
                                "4.Palindrome","5.Electricity Bill","6.1D Array","7.Prime Number",
                                "8.2D Array","9.Taylor series","10.String operations","11.Bubble sort","12.Square Root","13.Average Marks",
                                "14.Sum, Mean and Standard deviation","15.Binary to Decimal Conversion"],
    'DATA STRUCTURES LABORATORY(18CSL38)': ["1.Array operation","2.Strings","3.Stack","4.Infix to Postfix Expression",
                                "5.Suffix expression & Tower of Hanoi","6.Circular Queue","7.Singly Linked List",
                                "8.Doubly Linked List","9.Singly Circular Linked List","10.Binary Search Tree",
                                "11.Graph(G) of cities","12.Hash function"],
    'DESIGN AND ANALYSIS OF ALGORITHM LABORATORY(18CSL47)': ["1.Student Class & arrays","2.Superclass & Customer class","3.Reading Integers & multi-thread","4.Quicksort","5.MergeSort",
                                "6.Knapsack","7.Dijkstra's Algorithm","8.Kruskal's algorithm","9.Prim's algorithm",
                                "10.Floyd's & Travelling sales problem","11.Subset of given set","12.Hamiltonian Cycles"],
    'COMPUTER NETWORK LABORATORY(18CSL57)': ["1.Point-to-point Network                                      ","2.Ping message","3.Ethernet LAN","4.Wireless LAN",
                                "5.GSM","6.CDMA","7.CRC-CCITT","8.Bellman-ford algorithm","9.TCP/IP Socket",
                                "10.Datagram Socket","11.RSA Algorithm","12.Leaky Bucket Algorithm"],
    'DBMS LABORATORY WITH MINI PROJECT(18CSL58)' : ["1.Library Database","2.Order Database","3.Movie Database","4.College Database",
                                "5.Company Database"],
    'WEB TECHNOLOGY AND ITS APPLICAIONS(18CS63)' : ["1.Simple calculator in javascript","2.Squares and cubes in javascript","3.Text-growing and shrinking in javascript","4.String operations in javascript",
                                "5.Student data in XML","6.Number of visitors in php","7.Digital clock in php","8-A.Calculator operations in php","8-B.Transpose of matrix in php","8-C.Multiplication of two matrix","8-D.Addition of two matrix",
                                "9.Pattern matching with php","10.Student database with php and mysql"],
    'COMPUTER GRAPHICS LABORATORY(18CSL67)' : ["1.Brenham's line drawing algorithm","2.Triangle rotation","3.colour cube and spin","4.color cube with perspective viewing",
                                "5.Cohen-sutherland algorithm","6.Tea pot on a table","7.Sierpinski gasket","8.Bezier curve algorithm","9.Scan line algorithm"]

}
program_data = {
    'C PROGRAMMING LABORATORY(18CPL17/27)': ['LAB1.txt', 'LAB2.c', 'LAB3.c', 'LAB4.c', 'LAB5.c', 'LAB6.c', 'LAB7.c', 'LAB8.c', 'LAB9.c', 'LAB10.c', 'LAB11.c', 'LAB12.c', 'LAB13.c', 'LAB14.c', 'LAB15.c',],
    'DATA STRUCTURES LABORATORY(18CSL38)' : ['prog1.c','prog2.c','prog3.c','prog4.c','prog5.c','prog6.c','prog7.c','prog8.c','prog9.c','prog10.c','prog11.c','prog12.c'],
    'DESIGN AND ANALYSIS OF ALGORITHM LABORATORY(18CSL47)': ['prog1.java', 'prog2.java', 'prog3.java', 'prog4.java', 'prog5.java', 'prog6.java', 'prog7.java', 'prog8.java', 'prog9.java', 'prog10.java', 'prog11.java', 'prog12.java'],
    'COMPUTER NETWORK LABORATORY(18CSL57)': ['prog1.txt', 'prog2.txt', 'prog3.txt', 'prog4.txt', 'prog5.txt', 'prog6.txt', 'prog7.java', 'prog8.java', 'prog9.txt', 'prog10.txt', 'prog11.java', 'prog12.java'],
    'DBMS LABORATORY WITH MINI PROJECT(18CSL58)': ['0.txt','1.txt','2.txt','3.txt','4.txt'],
    'WEB TECHNOLOGY AND ITS APPLICAIONS(18CS63)' : ['1.txt', '2.txt', '3.txt', '4.txt', '5.xml', '6.php', '7.php', '8_A.php', '8_B.php', '8_C.php', '8_D.php', '9.php', '10.php'],
    'COMPUTER GRAPHICS LABORATORY(18CSL67)' : ['PRO1.txt', 'PRO2.txt', 'PRO3.txt', 'PRO4.txt', 'PRO5.txt', 'PRO6.txt', 'PRO7.txt', 'PRO8.txt', 'PRO9.txt']
}
program_path = {
    'C PROGRAMMING LABORATORY(18CPL17/27)' : 'data\c\source',
    'DATA STRUCTURES LABORATORY(18CSL38)' : 'data\ds\source',
    'DESIGN AND ANALYSIS OF ALGORITHM LABORATORY(18CSL47)' : 'data\daa\source',
    'COMPUTER NETWORK LABORATORY(18CSL57)' : 'data\cns\source',
    'DBMS LABORATORY WITH MINI PROJECT(18CSL58)' : 'data\dbms\source',
    'WEB TECHNOLOGY AND ITS APPLICAIONS(18CS63)' : 'data\web\source',
    'COMPUTER GRAPHICS LABORATORY(18CSL67)' : 'data\cgv\source'
}
image_path = {
    'C PROGRAMMING LABORATORY(18CPL17/27)' : 'data\c\output',
    'DATA STRUCTURES LABORATORY(18CSL38)' : 'data\ds\output',
    'DESIGN AND ANALYSIS OF ALGORITHM LABORATORY(18CSL47)' : 'data\daa\output',
    'COMPUTER NETWORK LABORATORY(18CSL57)' : 'data\cns\output',
    'DBMS LABORATORY WITH MINI PROJECT(18CSL58)' : 'data\dbms\output',
    'WEB TECHNOLOGY AND ITS APPLICAIONS(18CS63)' : 'data\web\output',
    'COMPUTER GRAPHICS LABORATORY(18CSL67)' : 'data\cgv\output'
}
image_data = {
    'C PROGRAMMING LABORATORY(18CPL17/27)' : ['0','0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png', '13.png'],
    'DATA STRUCTURES LABORATORY(18CSL38)' : [],
    'DESIGN AND ANALYSIS OF ALGORITHM LABORATORY(18CSL47)' : ['1.jpg', '2.jpg', '3.jpg', '4.png', '5.png', '6.jpg', '7.png', '8.png', '9.png', '10.jpg', '11.png', '12.png'],
    'COMPUTER NETWORK LABORATORY(18CSL57)' : ['1.JPG', '2.JPG', '3.png', '4.JPG', '5.JPG', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg'],
    'DBMS LABORATORY WITH MINI PROJECT(18CSL58)' : ['out0.txt', 'out1.txt', 'out2.txt', 'out3.txt', 'out4.txt'],
    'WEB TECHNOLOGY AND ITS APPLICAIONS(18CS63)' : ['0.png', '1.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8_A.png', '8_B.png', '8_C.png', '8_D.png', '9.png', '10.png'],
    'COMPUTER GRAPHICS LABORATORY(18CSL67)' : ['Pro-1.gif', 'Pro-2.gif', 'Pro-3.gif', 'Pro-4.gif', 'Pro-5.jpg', 'Pro-6.jpg', 'Pro-7.gif', 'Pro-8.gif', 'Pro-9.gif']
}
program = []
option_data = {}
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.model = QStandardItemModel()
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(150, 40, 514, 56))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(170, 255, 255);")
        self.label.setObjectName("label")
        self.label.setText("DIGITAL LAB MANUAL")
        self.course_label = QtWidgets.QLabel(self.frame)
        self.course_label.setGeometry(QtCore.QRect(130, 150, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Arieal")
        font.setPointSize(12)
        self.course_label.setFont(font)
        self.course_label.setText("SELECT THE COURSE:-")
        self.comboCourse = QComboBox(self.frame)
        self.comboCourse.setGeometry(QtCore.QRect(140, 180, 550, 31))
        self.comboCourse.setFont(QFont('', 12))
        self.comboCourse.setModel(self.model)
        self.subject_label = QtWidgets.QLabel(self.frame)
        self.subject_label.setGeometry(QtCore.QRect(130, 240, 281, 31))
        font.setFamily("Arieal")
        font.setPointSize(12)
        self.subject_label.setFont(font)
        self.subject_label.setText("SELECT THE PROGRAM NAME:-")
        self.comboSubject = QComboBox(self.frame)
        self.comboSubject.setGeometry(QtCore.QRect(240, 280, 411, 31))
        self.comboSubject.setFont(QFont('', 12))
        self.comboSubject.setModel(self.model)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(400, 575, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("DESIGNED AND DEVELOPED BY ADARSH N")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(470, 540, 271, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("VIEW SOURCE CODE")
        self.pushButton.clicked.connect(self. openlink)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 360, 191, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("SUBMIT")
        self.pushButton_2.clicked.connect(self. openprogram)
        # add data
        for k, v in data.items():
            course = QStandardItem(k)
            self.model.appendRow(course)
            for value in v:
                subject = QStandardItem(value)
                course.appendRow(subject)
        self.comboCourse.currentIndexChanged.connect(self.updateCourseCombo)
        self.comboSubject.currentIndexChanged.connect(self.updateSubject)
        self.updateCourseCombo(0)
        self.setWindowTitle("VTU 2018 SCHEME DIGITAL LAB MANUAL BY ADARSH N")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'data\ico.png'))


    def updateCourseCombo(self, index):
        indx = self.model.index(index, 0, self.comboCourse.rootModelIndex())
        self.comboSubject.setRootModelIndex(indx)
        self.comboSubject.setCurrentIndex(0)
        program.clear()

    def updateSubject(self):
        if len(program) > 0:
            program.clear()
            option_data.pop('course')
            option_data.pop('subject')
       
    def openlink(self):
        webbrowser.open('https://github.com/Adarsh232001/DIGITAL-VTU-LAB-MANAUAL')

    def openprogram(self):
        course = self.comboCourse.currentText()
        option_data.update({'course': course})
        program_name = self.comboSubject.currentText()
        option_data.update({'subject': program_name})
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog, course, program_name)
        Dialog.exec()

        

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog, course, program_name):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 650)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowIconText('logo')
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setWordWrapMode(QTextOption.NoWrap)
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 590, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 590, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self. copy_to_clipboard)
        self.pushButton_2.clicked.connect(self. open_output)
        self.retranslateUi(Dialog)
        
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        for i,k in data.items():
            if i == course:
                for values in k:
                    if values == program_name:
                        for a,b in program_data.items():
                            if a == i:
                                for vlaues_1 in b:
                                    if k.index(values) == b.index(vlaues_1):
                                        program.append(vlaues_1)

                        for c,d in image_data.items():
                            if c == i == course:
                                for vlaues_2 in d:
                                    if k.index(values) == d.index(vlaues_2):
                                        program.append(vlaues_2)                
        code(self,program)

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PROGRAM WINDOW DESIGNED AND DEVELOPED BY ADARSH N"))
        self.pushButton.setText(_translate("Dialog", "COPY TO CLIPBOARD"))
        self.pushButton_2.setText(_translate("Dialog", "OPEN SCREEN SHOT OF OUTPUT"))


    def copy_to_clipboard(self):
        QApplication.clipboard().setText(name)
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(name)
        msg=QMessageBox()
        msg.setText("copied on clipboard")
        msg.exec_()

    def open_output(self):
        imagepath(self)
        

def code(self,program):
    for i,k in data.items():
        for value in k:
            for a,b in program_data.items():
                if (a == i == option_data["course"]) and value == option_data["subject"]:
                    for value_1 in b:
                        for c,d in program_path.items():
                            if c == a and (program[0] == value_1 and k.index(value) == b.index(value_1)):
                                filename = os.path.dirname(__file__) + "\\" + d + '\\' +program[0]
                                if os.path.isfile(filename):
                                    text = open(filename).read()
                                    global name 
                                    name = text
                                    self.textBrowser.setText(text)
                                                                                            
def imagepath(self):
    for i,k in data.items():
                for value in k:
                    for a,b in image_data.items():
                        if (a == i == option_data["course"]) and (value == option_data["subject"]):
                            for value_1 in b:
                                for c,d in image_path.items():
                                    if (c == a == option_data["course"]) and ((program[1] == value_1) and (k.index(value) == b.index(value_1))):
                                        filename = os.path.dirname(__file__) + "\\" + d + '\\' + program[1]
                                        Dialog_1 = QtWidgets.QDialog()
                                        ui = Ui_Dialog_1()
                                        ui.setupUi(Dialog_1, filename)
                                        Dialog_1.exec()

class Ui_Dialog_1(QWidget):
    def setupUi(self, Dialog, filename):
                                        
        if filename.endswith('.txt'):
            Dialog_2 = QtWidgets.QDialog()
            ui = Ui_Dialog_2()
            ui.setupUi(Dialog_2)
            Dialog_2.exec()

        elif filename.endswith('.gif'):
            Dialog.setObjectName("Dialog")
            Dialog.resize(1200, 700)
            self.centralwidget = QtWidgets.QWidget(Dialog)
            self.centralwidget.setObjectName("centralwidget")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(0, 0, 1200, 700))
            self.label.setObjectName("label")
            self.movie = QMovie(filename)
            self.label.setMovie(self.movie)
            self.movie.start()
    

        elif os.path.isfile(filename):
            Dialog.setObjectName("Dialog")
            Dialog.resize(800,650)
            self.centralwidget = QtWidgets.QWidget(Dialog)
            self.centralwidget.setObjectName("centralwidget")
            self.retranslateUi(Dialog)
            self.photo = QtWidgets.QLabel(self.centralwidget)
            self.photo.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            self.photo.setGeometry(QtCore.QRect(0, 0, 800, 650))
            self.photo.setText("")
            self.photo.setPixmap(QtGui.QPixmap(filename))
            self.photo.setScaledContents(True)
            self.photo.setObjectName("photo")
            scriptDir = os.path.dirname(os.path.realpath(__file__))
            self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon.png'))                                          

            QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SCREEN SHOT DESIGNED AND DEVELOPED BY ADARSH N"))


class Ui_Dialog_2(QWidget):
    def setupUi(self, Dialog_2):
        Dialog_2.setObjectName("Dialog_2")
        Dialog_2.resize(800, 650)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 800, 650))
        self.textBrowser.setObjectName("textBrowser")
        for i,k in data.items():
            for value in k:
                for a,b in image_data.items():
                    if i==a:
                        for value_1 in b:
                            for c,d in image_path.items():
                                if c == a and (program[1] == value_1 and k.index(value) == b.index(value_1)):
                                    filename = os.path.dirname(__file__) + "\\" +  d + '\\' + program[1]
                                    if os.path.isfile(filename):
                                        text = open(filename).read()
                                        self.textBrowser.setText(text)

        self.retranslateUi(Dialog_2)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'icon.png'))
        QtCore.QMetaObject.connectSlotsByName(Dialog_2)

    def retranslateUi(self, Dialog_2):
        _translate = QtCore.QCoreApplication.translate
        Dialog_2.setWindowTitle(_translate("Dialog_2", "OUTPUT TEXT DESIGNED AND DEVELOPED BY ADARSH N"))


if __name__ == "__main__":
    app = QApplication(sys.argv)        
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())
