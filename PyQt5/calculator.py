import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow, QLabel, QLineEdit, QPushButton

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(250,250,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QLabel(self)
        self.lbl_sayi1.setText('Number 1: ')
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.lbl_sayi2 = QLabel(self)
        self.lbl_sayi2.setText('Number 2: ')
        self.lbl_sayi2.move(50,80)

        self.txt_sayi2 = QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_plus = QPushButton(self)
        self.btn_plus.setText('Collection')
        self.btn_plus.move(150,130)
        self.btn_plus.clicked.connect(self.collect)

        self.btn_minus = QPushButton(self)
        self.btn_minus.setText('Subtraction')
        self.btn_minus.move(250,130)
        self.btn_minus.clicked.connect(self.subtract)

        self.btn_mltp = QPushButton(self)
        self.btn_mltp.setText('Multiplication')
        self.btn_mltp.move(150,170)
        self.btn_mltp.clicked.connect(self.multi)

        self.btn_divide = QPushButton(self)
        self.btn_divide.setText('Divide')
        self.btn_divide.move(250,170)
        self.btn_divide.clicked.connect(self.divid)

        self.lbl_result = QLabel(self)
        self.lbl_result.setText('Result: ')
        self.lbl_result.move(230,210)

    def collect(self):
        result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        self.lbl_result.setText('Sonuc \n'+ str(result))  
    def subtract(self):
        result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        self.lbl_result.setText('Sonuc \n'+ str(result))  
    def multi(self):
        result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        self.lbl_result.setText('Sonuc \n'+ str(result))  
    def divid(self):
        result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_result.setText('Sonuc \n' + str(result))  

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()