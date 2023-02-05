from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
import os
import sys
os.system("cls")
class Col(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Phyton")
    self.resize(1268,960)
    self.move(100,100)
    self.setStyleSheet("""
    background-color: rgb(128,128,128);""")
    self.setGeometry(100,50,400,800)
    self.setStyleSheet("""
    color: rgb("green");
    background-color: rgb(0,0,0);
    border-color: rgb(255,255,255);
    border-width: 1px;
    border-radius: 29px;
    border-style: outset;""")
    self.dastur()
    self.show()
  def dastur(self):
    self.label = QLabel(self)
    self.label.setGeometry(30,220,340,80)
    self.label.setWordWrap(True)
    self.label.setStyleSheet("""
        background-color: rgb(255,255,255);
        border-color: rgb(255,255,255);""")
    self.label.setAlignment(Qt.AlignRight)
    self.label.setFont(QFont('Arial', 40))

    bol=QPushButton(self)
    bol.setGeometry(300,320,70,70)
    bol.setStyleSheet("""
    background-color: rgb(255,165,0)""")
    bol.setFont(QFont("clibri",20))
    bol.setText("/")
    #bol.setAlignment(Qt.AlignCenter)


    kop=QPushButton(self)
    kop.setGeometry(300,410,70,70)
    kop.setStyleSheet("""
    background-color: rgb(255,165,0)""")
    kop.setFont(QFont("clibri",20))
    kop.setText("*")

    ayr=QPushButton(self)
    ayr.setGeometry(300,500,70,70)
    ayr.setStyleSheet("""
    background-color: rgb(255,165,0)""")
    ayr.setFont(QFont("clibri",20))
    ayr.setText("-")

    qosh=QPushButton(self)
    qosh.setGeometry(300,590,70,70)
    qosh.setStyleSheet("""
    background-color: rgb(255,165,0)""")
    qosh.setFont(QFont("clibri",20))
    qosh.setText("+")

    bar=QPushButton(self)
    bar.setGeometry(300,680,70,70)
    bar.setStyleSheet("""
    background-color: rgb(255,165,0)""")
    bar.setFont(QFont("clibri",20))
    bar.setText("=")

    nu=QPushButton(self)
    nu.setGeometry(210,680,70,70)
    nu.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    nu.setFont(QFont("clibri",20))
    nu.setText(".")

    
    nul=QPushButton(self)
    nul.setGeometry(30,680,140,70)
    nul.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    nul.setFont(QFont("clibri",20))
    nul.setText("0")
 
    uc=QPushButton(self)
    uc.setGeometry(210,590,70,70)
    uc.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    uc.setFont(QFont("clibri",20))
    uc.setText("3")

    ik=QPushButton(self)
    ik.setGeometry(120,590,70,70)
    ik.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    ik.setFont(QFont("clibri",20))
    ik.setText("2")
    
    br=QPushButton(self)
    br.setGeometry(30,590,70,70)
    br.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    br.setFont(QFont("clibri",20))
    br.setText("1")

    ol=QPushButton(self)
    ol.setGeometry(210,500,70,70)
    ol.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    ol.setFont(QFont("clibri",20))
    ol.setText("6")
    
    be=QPushButton(self)
    be.setGeometry(120,500,70,70)
    be.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    be.setFont(QFont("clibri",20))
    be.setText("5")

    to=QPushButton(self)
    to.setGeometry(30,500,70,70)
    to.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    to.setFont(QFont("clibri",20))
    to.setText("4")

    ye=QPushButton(self)
    ye.setGeometry(30,410,70,70)
    ye.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    ye.setFont(QFont("clibri",20))
    ye.setText("7")

    sa=QPushButton(self)
    sa.setGeometry(120,410,70,70)
    sa.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    sa.setFont(QFont("clibri",20))
    sa.setText("8")

    tq=QPushButton(self)
    tq.setGeometry(210,410,70,70)
    tq.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    tq.setFont(QFont("clibri",20))
    tq.setText("9")

    oc=QPushButton(self)
    oc.setGeometry(30,320,70,70)
    oc.setStyleSheet("""
    background-color: rgb(162,162,162)""")
    oc.setFont(QFont("clibri",20))
    oc.setText("AC")

    ayr.clicked.connect(self.action_minus)
    bar.clicked.connect(self.action_equal)
    nul.clicked.connect(self.action0)
    br.clicked.connect(self.action1)
    ik.clicked.connect(self.action2)
    uc.clicked.connect(self.action3)
    to.clicked.connect(self.action4)
    be.clicked.connect(self.action5)
    ol.clicked.connect(self.action6)
    ye.clicked.connect(self.action7)
    sa.clicked.connect(self.action8)
    tq.clicked.connect(self.action9)
    bol.clicked.connect(self.action_div)
    kop.clicked.connect(self.action_mul)
    qosh.clicked.connect(self.action_plus)
    nu.clicked.connect(self.action_point)
    oc.clicked.connect(self.action_del)

  def action_equal(self):
    equation = self.label.text()
    try:
        ans = eval(equation)
        self.label.setText(str(ans))
    except:
        self.label.setText("Xato kiritildi")

  def action_plus(self):
        self.label.setText(self.label.text() + " + ")
  def action_minus(self):
        self.label.setText(self.label.text() + " - ")
  def action_div(self):
        self.label.setText(self.label.text() + " / ")
  def action_mul(self):
        self.label.setText(self.label.text() + " * ")
  def action_point(self):
        self.label.setText(self.label.text() + ".")
  def action0(self):
        self.label.setText(self.label.text() + "0")
  def action1(self):
        self.label.setText(self.label.text() + "1")
  def action2(self):
        self.label.setText(self.label.text() + "2")
  def action3(self):
        self.label.setText(self.label.text() + "3")
  def action4(self):
        self.label.setText(self.label.text() + "4")
  def action5(self):
        self.label.setText(self.label.text() + "5")
  def action6(self):
        self.label.setText(self.label.text() + "6")
  def action7(self):
        self.label.setText(self.label.text() + "7")
  def action8(self):
        self.label.setText(self.label.text() + "8")
  def action9(self):
        self.label.setText(self.label.text() + "9")
  def action_del(self):
        print(self.label.text()[:len(self.label.text())-1])
        self.label.setText(self.label.text()[:len(self.label.text())-1])

App = QApplication(sys.argv)
window = Col()
sys.exit(App.exec())
                                                                                                                                                                                                                                                                                                                                          