import random
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("XO game")
        self.initUI()
        self.allEmptyButtons = [self.Pbutton1_1, self.Pbutton1_2, self.Pbutton1_3, self.Pbutton2_1, self.Pbutton2_2,
                                self.Pbutton2_3, self.Pbutton3_1, self.Pbutton3_2, self.Pbutton3_3]
        self.nameOfAllEmptyButtons = ["Pbutton1_1", "Pbutton1_2", "Pbutton1_3", "Pbutton2_1", "Pbutton2_2",
                                      "Pbutton2_3", "Pbutton3_1", "Pbutton3_2", "Pbutton3_3"]

    def initUI(self):

        self.ComputerPushButton = QtWidgets.QPushButton(self)
        self.ComputerPushButton.setAccessibleName("ComputerPushButton")
        self.ComputerPushButton.setGeometry(170, 295, 60, 30)
        self.ComputerPushButton.clicked.connect(self.computerTurn)
        self.ComputerPushButton.setText("computer turn")
        self.ComputerPushButton.setFont(QFont('Times', 5))

        self.Pbutton1_1 = QtWidgets.QPushButton(self)
        self.Pbutton1_1.setAccessibleName("Pbutton1_1")
        self.Pbutton1_1.setGeometry(155, 155, 30, 30)
        self.Pbutton1_1.clicked.connect(self.clickPushButton1_1ForPlayer)

        self.Pbutton1_2 = QtWidgets.QPushButton(self)
        self.Pbutton1_2.setAccessibleName("Pbutton1_2")
        self.Pbutton1_2.setGeometry(185, 155, 30, 30)
        self.Pbutton1_2.clicked.connect(self.clickPushButton1_2ForPlayer)

        self.Pbutton1_3 = QtWidgets.QPushButton(self)
        self.Pbutton1_3.setAccessibleName("Pbutton1_3")
        self.Pbutton1_3.setGeometry(215, 155, 30, 30)
        self.Pbutton1_3.clicked.connect(self.clickPushButton1_3ForPlayer)

        self.Pbutton2_1 = QtWidgets.QPushButton(self)
        self.Pbutton2_1.setAccessibleName("Pbutton2_1")
        self.Pbutton2_1.setGeometry(155, 185, 30, 30)
        self.Pbutton2_1.clicked.connect(self.clickPushButton2_1ForPlayer)

        self.Pbutton2_2 = QtWidgets.QPushButton(self)
        self.Pbutton2_2.setAccessibleName("Pbutton2_2")
        self.Pbutton2_2.setGeometry(185, 185, 30, 30)
        self.Pbutton2_2.clicked.connect(self.clickPushButton2_2ForPlayer)

        self.Pbutton2_3 = QtWidgets.QPushButton(self)
        self.Pbutton2_3.setAccessibleName("Pbutton2_3")
        self.Pbutton2_3.setGeometry(215, 185, 30, 30)
        self.Pbutton2_3.clicked.connect(self.clickPushButton2_3ForPlayer)

        self.Pbutton3_1 = QtWidgets.QPushButton(self)
        self.Pbutton3_1.setAccessibleName("Pbutton3_1")
        self.Pbutton3_1.setGeometry(155, 215, 30, 30)
        self.Pbutton3_1.clicked.connect(self.clickPushButton3_1ForPlayer)

        self.Pbutton3_2 = QtWidgets.QPushButton(self)
        self.Pbutton3_2.setAccessibleName("Pbutton3_2")
        self.Pbutton3_2.setGeometry(185, 215, 30, 30)
        self.Pbutton3_2.clicked.connect(self.clickPushButton3_2ForPlayer)

        self.Pbutton3_3 = QtWidgets.QPushButton(self)
        self.Pbutton3_3.setAccessibleName("Pbutton3_3")
        self.Pbutton3_3.setGeometry(215, 215, 30, 30)
        self.Pbutton3_3.clicked.connect(self.clickPushButton3_3ForPlayer)

    def anyOneIsWinner(self):
        if (self.Pbutton1_1.text() == "X" and self.Pbutton1_2.text() == "X" and self.Pbutton1_3.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton1_2.text() == "O" and self.Pbutton1_3.text() == "O"):
            self.Pbutton1_1.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton1_2.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton1_3.setStyleSheet("color : blue ; background-color : green")
            # self.close()
        elif (self.Pbutton1_1.text() == "X" and self.Pbutton2_1.text() == "X" and self.Pbutton3_1.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton2_1.text() == "O" and self.Pbutton3_1.text() == "O"):
            self.Pbutton1_1.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton2_1.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton3_1.setStyleSheet("color : blue ; background-color : green")
            # self.close()
        elif (self.Pbutton1_1.text() == "X" and self.Pbutton2_2.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton2_2.text() == "O" and self.Pbutton3_3.text() == "O"):
            self.Pbutton1_1.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton2_2.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton3_3.setStyleSheet("color : blue ; background-color : green")
            # self.close()
        elif (self.Pbutton3_1.text() == "X" and self.Pbutton3_2.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton3_2.text() == "O" and self.Pbutton3_3.text() == "O"):
            self.Pbutton3_1.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton3_2.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton3_3.setStyleSheet("color : blue ; background-color : green")
            # self.close()
        elif (self.Pbutton1_3.text() == "X" and self.Pbutton2_3.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton3_3.text() == "O" and self.Pbutton2_3.text() == "O" and self.Pbutton1_3.text() == "O"):
            self.Pbutton1_3.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton2_3.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton3_3.setStyleSheet("color : blue ; background-color : green")
            # self.close()
        elif (self.Pbutton1_3.text() == "X" and self.Pbutton2_2.text() == "X" and self.Pbutton3_1.text() == "X") or (
                self.Pbutton1_3.text() == "O" and self.Pbutton2_2.text() == "O" and self.Pbutton3_1.text() == "O"):
            self.Pbutton1_3.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton2_2.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton3_1.setStyleSheet("color : blue ; background-color : green")
            # self.close()
        elif (self.Pbutton1_2.text() == "X" and self.Pbutton2_2.text() == "X" and self.Pbutton3_2.text() == "X") or (
                self.Pbutton1_2.text() == "O" and self.Pbutton2_2.text() == "O" and self.Pbutton3_2.text() == "O"):
            self.Pbutton1_2.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton2_2.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton3_2.setStyleSheet("color : blue ; background-color : green")
            # self.close()
        elif (self.Pbutton2_1.text() == "X" and self.Pbutton2_2.text() == "X" and self.Pbutton2_3.text() == "X") or (
                self.Pbutton2_1.text() == "O" and self.Pbutton2_2.text() == "O" and self.Pbutton2_3.text() == "O"):
            self.Pbutton2_1.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton2_2.setStyleSheet("color : blue ; background-color : green")
            self.Pbutton2_3.setStyleSheet("color : blue ; background-color : green")
            # self.close()

    def checkIfIsDualSame(self):

        if ((self.Pbutton1_1.text() == "X" and self.Pbutton1_2.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton1_2.text() == "O")) and (
                self.Pbutton1_3.isEnabled() == True):
            return True

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton1_2.text() == "X") or (
                self.Pbutton1_3.text() == "O" and self.Pbutton1_2.text() == "O")) and (
                self.Pbutton1_1.isEnabled() == True):
            return True

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton1_3.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton1_3.text() == "O")) and (
                self.Pbutton1_2.isEnabled() == True):
            return True

        elif ((self.Pbutton2_1.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton2_1.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton2_3.isEnabled() == True):
            return True

        elif ((self.Pbutton2_3.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton2_3.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton2_1.isEnabled() == True):
            return True

        elif ((self.Pbutton2_1.text() == "X" and self.Pbutton2_3.text() == "X") or (
                self.Pbutton2_1.text() == "O" and self.Pbutton2_3.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            return True

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton3_2.text() == "X") or (
                self.Pbutton3_1.text() == "X" and self.Pbutton3_2.text() == "X")) and (
                self.Pbutton3_3.isEnabled() == True):
            return True

        elif ((self.Pbutton3_3.text() == "X" and self.Pbutton3_2.text() == "X") or (
                self.Pbutton3_3.text() == "X" and self.Pbutton3_2.text() == "X")) and (
                self.Pbutton3_1.isEnabled() == True):
            return True

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton3_3.text() == "O")) and (
                self.Pbutton3_2.isEnabled() == True):
            return True

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton2_1.text() == "X") or (
                self.Pbutton1_1.text() == "X" and self.Pbutton2_1.text() == "X")) and (
                self.Pbutton3_1.isEnabled() == True):
            return True

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton2_1.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton2_1.text() == "O")) and (
                self.Pbutton1_1.isEnabled() == True):
            return True

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton3_1.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton3_1.text() == "O")) and (
                self.Pbutton2_1.isEnabled() == True):
            return True

        elif ((self.Pbutton1_2.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton1_2.text() == "X" and self.Pbutton2_2.text() == "X")) and (
                self.Pbutton3_2.isEnabled() == True):
            return True

        elif ((self.Pbutton3_2.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton3_2.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton1_2.isEnabled() == True):
            return True

        elif ((self.Pbutton1_2.text() == "X" and self.Pbutton3_2.text() == "X") or (
                self.Pbutton1_2.text() == "O" and self.Pbutton3_2.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            return True

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton2_3.text() == "X") or (
                self.Pbutton1_3.text() == "O" and self.Pbutton2_3.text() == "O")) and (
                self.Pbutton3_3.isEnabled() == True):
            return True

        elif ((self.Pbutton3_3.text() == "X" and self.Pbutton2_3.text() == "X") or (
                self.Pbutton3_3.text() == "O" and self.Pbutton2_3.text() == "O")) and (
                self.Pbutton1_3.isEnabled() == True):
            return True

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton1_3.text() == "O" and self.Pbutton3_3.text() == "O")) and (
                self.Pbutton2_3.isEnabled() == True):
            return True

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton1_3.text() == "X" and self.Pbutton2_2.text() == "X")) and (
                self.Pbutton3_1.isEnabled() == True):
            return True

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton1_3.isEnabled() == True):
            return True

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton1_3.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton1_3.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            return True

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton3_3.isEnabled() == True):
            return True

        elif ((self.Pbutton3_3.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton3_3.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton1_1.isEnabled() == True):
            return True

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton3_3.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            return True

        else:
            return False

    def isDualSame(self):

        if ((self.Pbutton1_1.text() == "X" and self.Pbutton1_2.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton1_2.text() == "O")) and (
                self.Pbutton1_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_3)

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton1_2.text() == "X") or (
                self.Pbutton1_3.text() == "O" and self.Pbutton1_2.text() == "O")) and (
                self.Pbutton1_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_1)

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton1_3.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton1_3.text() == "O")) and (
                self.Pbutton1_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_2)

        elif ((self.Pbutton2_1.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton2_1.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton2_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_3)

        elif ((self.Pbutton2_3.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton2_3.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton2_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_1)

        elif ((self.Pbutton2_1.text() == "X" and self.Pbutton2_3.text() == "X") or (
                self.Pbutton2_1.text() == "O" and self.Pbutton2_3.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_2)

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton3_2.text() == "X") or (
                self.Pbutton3_1.text() == "X" and self.Pbutton3_2.text() == "X")) and (
                self.Pbutton3_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_3)

        elif ((self.Pbutton3_3.text() == "X" and self.Pbutton3_2.text() == "X") or (
                self.Pbutton3_3.text() == "X" and self.Pbutton3_2.text() == "X")) and (
                self.Pbutton3_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_1)

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton3_3.text() == "O")) and (
                self.Pbutton3_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_2)

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton2_1.text() == "X") or (
                self.Pbutton1_1.text() == "X" and self.Pbutton2_1.text() == "X")) and (
                self.Pbutton3_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_1)

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton2_1.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton2_1.text() == "O")) and (
                self.Pbutton1_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_1)

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton3_1.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton3_1.text() == "O")) and (
                self.Pbutton2_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_1)

        elif ((self.Pbutton1_2.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton1_2.text() == "X" and self.Pbutton2_2.text() == "X")) and (
                self.Pbutton3_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_2)

        elif ((self.Pbutton3_2.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton3_2.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton1_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_2)

        elif ((self.Pbutton1_2.text() == "X" and self.Pbutton3_2.text() == "X") or (
                self.Pbutton1_2.text() == "O" and self.Pbutton3_2.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_2)

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton2_3.text() == "X") or (
                self.Pbutton1_3.text() == "O" and self.Pbutton2_3.text() == "O")) and (
                self.Pbutton3_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_3)

        elif ((self.Pbutton3_3.text() == "X" and self.Pbutton2_3.text() == "X") or (
                self.Pbutton3_3.text() == "O" and self.Pbutton2_3.text() == "O")) and (
                self.Pbutton1_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_3)

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton1_3.text() == "O" and self.Pbutton3_3.text() == "O")) and (
                self.Pbutton2_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_3)

        elif ((self.Pbutton1_3.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton1_3.text() == "X" and self.Pbutton2_2.text() == "X")) and (
                self.Pbutton3_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_1)

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton1_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_3)

        elif ((self.Pbutton3_1.text() == "X" and self.Pbutton1_3.text() == "X") or (
                self.Pbutton3_1.text() == "O" and self.Pbutton1_3.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_2)

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton3_3.isEnabled() == True):
            self.computerPushButton(self.Pbutton3_3)

        elif ((self.Pbutton3_3.text() == "X" and self.Pbutton2_2.text() == "X") or (
                self.Pbutton3_3.text() == "O" and self.Pbutton2_2.text() == "O")) and (
                self.Pbutton1_1.isEnabled() == True):
            self.computerPushButton(self.Pbutton1_1)

        elif ((self.Pbutton1_1.text() == "X" and self.Pbutton3_3.text() == "X") or (
                self.Pbutton1_1.text() == "O" and self.Pbutton3_3.text() == "O")) and (
                self.Pbutton2_2.isEnabled() == True):
            self.computerPushButton(self.Pbutton2_2)

    def computerPushButton(self, button):
        self.button = button
        self.button.setText("O")
        self.button.setEnabled(False)
        # if self.button.accessibleName() in self.nameOfAllEmptyButtons:
        self.nameOfAllEmptyButtons.remove(self.button.accessibleName())
        self.update()

    def clickPushButton1_1ForPlayer(self):

        self.Pbutton1_1.setText("X")
        self.Pbutton1_1.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton1_1.accessibleName())
        self.update()

    def clickPushButton1_2ForPlayer(self):
        self.Pbutton1_2.setText("X")
        self.Pbutton1_2.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton1_2.accessibleName())
        self.update()

    def clickPushButton1_3ForPlayer(self):
        self.Pbutton1_3.setText("X")
        self.Pbutton1_3.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton1_3.accessibleName())
        self.update()

    def clickPushButton2_1ForPlayer(self):
        self.Pbutton2_1.setText("X")
        self.Pbutton2_1.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton2_1.accessibleName())
        self.update()

    def clickPushButton2_2ForPlayer(self):
        self.Pbutton2_2.setText("X")
        self.Pbutton2_2.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton2_2.accessibleName())
        self.update()

    def clickPushButton2_3ForPlayer(self):
        self.Pbutton2_3.setText("X")
        self.Pbutton2_3.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton2_3.accessibleName())
        self.update()

    def clickPushButton3_1ForPlayer(self):
        self.Pbutton3_1.setText("X")
        self.Pbutton3_1.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton3_1.accessibleName())
        self.update()

    def clickPushButton3_2ForPlayer(self):
        self.Pbutton3_2.setText("X")
        self.Pbutton3_2.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton3_2.accessibleName())
        self.update()

    def clickPushButton3_3ForPlayer(self):
        self.Pbutton3_3.setText("X")
        self.Pbutton3_3.setEnabled(False)
        self.nameOfAllEmptyButtons.remove(self.Pbutton3_3.accessibleName())
        self.update()

    def computerTurn(self):
        if len(self.nameOfAllEmptyButtons) == 9:
            #########first move was computer
            ##step 1
            self.LIST = [self.allEmptyButtons[0], self.allEmptyButtons[2], self.allEmptyButtons[6],
                         self.allEmptyButtons[8]]
            self.computerPushButton(random.choice(self.LIST))

        elif len(self.nameOfAllEmptyButtons) == 8:
            #########first move was player
            ## step 1
            if self.Pbutton1_1.isEnabled() == False or self.Pbutton1_3.isEnabled() == False or self.Pbutton3_1.isEnabled() == False or self.Pbutton3_3.isEnabled() == False:
                self.computerPushButton(self.Pbutton2_2)
            elif self.Pbutton2_2.isEnabled() == False:
                self.LIST1 = [self.allEmptyButtons[0], self.allEmptyButtons[2], self.allEmptyButtons[6],
                              self.allEmptyButtons[8]]
                self.computerPushButton(random.choice(self.LIST1))
            elif self.Pbutton1_2.isEnabled() == False or self.Pbutton2_1.isEnabled() == False or self.Pbutton2_3.isEnabled() == False or self.Pbutton3_2.isEnabled() == False:
                self.computerPushButton(self.Pbutton2_2)
            else:
                self.LIST2 = []
                if self.Pbutton1_1.isEnabled() == True:
                    self.LIST2.append(self.Pbutton1_1)

                if self.Pbutton1_2.isEnabled() == True:
                    self.LIST2.append(self.Pbutton1_2)

                if self.Pbutton1_3.isEnabled() == True:
                    self.LIST2.append(self.Pbutton1_3)

                if self.Pbutton2_1.isEnabled() == True:
                    self.LIST2.append(self.Pbutton2_1)

                if self.Pbutton2_2.isEnabled() == True:
                    self.LIST2.append(self.Pbutton2_2)

                if self.Pbutton2_3.isEnabled() == True:
                    self.LIST2.append(self.Pbutton2_3)

                if self.Pbutton3_1.isEnabled() == True:
                    self.LIST2.append(self.Pbutton3_1)

                if self.Pbutton3_2.isEnabled() == True:
                    self.LIST2.append(self.Pbutton3_2)

                if self.Pbutton3_3.isEnabled() == True:
                    self.LIST2.append(self.Pbutton3_3)
                self.computerPushButton(random.choice(self.LIST2))
        elif len(self.nameOfAllEmptyButtons) == 7:
            #########first move was computer
            ##step 2
            if self.Pbutton2_2.isEnabled() == True:
                self.LIST3 = []
                if self.Pbutton1_1.isEnabled() == True:
                    self.LIST3.append(self.Pbutton1_1)
                if self.Pbutton1_3.isEnabled() == True:
                    self.LIST3.append(self.Pbutton1_3)
                if self.Pbutton3_1.isEnabled() == True:
                    self.LIST3.append(self.Pbutton3_1)
                if self.Pbutton3_3.isEnabled() == True:
                    self.LIST3.append(self.Pbutton3_3)

                if self.Pbutton1_1.text() == "O" and self.Pbutton3_3.isEnabled() == True:
                    self.LIST3.remove(self.Pbutton3_3)

                if self.Pbutton3_3.text() == "O" and self.Pbutton1_1.isEnabled() == True:
                    self.LIST3.remove(self.Pbutton1_1)

                if self.Pbutton1_3.text() == "O" and self.Pbutton3_1.isEnabled() == True:
                    self.LIST3.remove(self.Pbutton3_1)

                if self.Pbutton3_1.text() == "O" and self.Pbutton1_3.isEnabled() == True:
                    self.LIST3.remove(self.Pbutton1_3)

                self.computerPushButton(random.choice(self.LIST3))

            else:
                if self.Pbutton1_1.isEnabled() == False:
                    self.computerPushButton(self.Pbutton3_3)
                elif self.Pbutton3_1.isEnabled() == False:
                    self.computerPushButton(self.Pbutton1_3)
                elif self.Pbutton3_3.isEnabled() == False:
                    self.computerPushButton(self.Pbutton1_1)
                elif self.Pbutton1_3.isEnabled() == False:
                    self.computerPushButton(self.Pbutton3_1)
                else:
                    self.LIST4 = []
                    if self.Pbutton1_1.isEnabled() == True:
                        self.LIST4.append(self.Pbutton1_1)

                    if self.Pbutton1_2.isEnabled() == True:
                        self.LIST4.append(self.Pbutton1_2)

                    if self.Pbutton1_3.isEnabled() == True:
                        self.LIST4.append(self.Pbutton1_3)

                    if self.Pbutton2_1.isEnabled() == True:
                        self.LIST4.append(self.Pbutton2_1)

                    if self.Pbutton2_2.isEnabled() == True:
                        self.LIST4.append(self.Pbutton2_2)

                    if self.Pbutton2_3.isEnabled() == True:
                        self.LIST4.append(self.Pbutton2_3)

                    if self.Pbutton3_1.isEnabled() == True:
                        self.LIST4.append(self.Pbutton3_1)

                    if self.Pbutton3_2.isEnabled() == True:
                        self.LIST4.append(self.Pbutton3_2)

                    if self.Pbutton3_3.isEnabled() == True:
                        self.LIST4.append(self.Pbutton3_3)
                    self.computerPushButton(random.choice(self.LIST4))

        elif len(self.nameOfAllEmptyButtons) == 6:
            #########first move was player
            ## step 2
            if self.checkIfIsDualSame() == False:
                if self.Pbutton2_2.text() == "O" and self.Pbutton1_2.isEnabled() == True and self.Pbutton2_1.isEnabled() == True and self.Pbutton2_3.isEnabled() == True and self.Pbutton3_2.isEnabled() == True:
                    self.LIST5 = [self.Pbutton1_2, self.Pbutton2_1, self.Pbutton2_3, self.Pbutton3_2]
                    self.computerPushButton(random.choice(self.LIST5))
                elif self.Pbutton2_2.text() == "O":
                    if (self.Pbutton1_2.isEnabled() == False and self.Pbutton3_2.isEnabled() == False) or (
                            self.Pbutton2_1.isEnabled() == False and self.Pbutton2_3.isEnabled() == False):
                        self.LIST6 = [self.allEmptyButtons[0], self.allEmptyButtons[2], self.allEmptyButtons[6],
                                      self.allEmptyButtons[8]]
                        self.computerPushButton(random.choice(self.LIST6))
                    else:
                        self.rlist = []
                        if self.Pbutton1_2.isEnabled() == False:
                            if self.Pbutton1_1.isEnabled() == True:
                                self.rlist.append(self.Pbutton1_1)
                            if self.Pbutton1_3.isEnabled() == True:
                                self.rlist.append(self.Pbutton1_3)
                        elif self.Pbutton2_1.isEnabled() == False:
                            if self.Pbutton1_1.isEnabled() == True:
                                self.rlist.append(self.Pbutton1_1)
                            if self.Pbutton3_1.isEnabled() == True:
                                self.rlist.append(self.Pbutton3_1)
                        elif self.Pbutton2_3.isEnabled() == False:
                            if self.Pbutton1_3.isEnabled() == True:
                                self.rlist.append(self.Pbutton1_3)
                            if self.Pbutton3_3.isEnabled() == True:
                                self.rlist.append(self.Pbutton3_3)
                        elif self.Pbutton3_2.isEnabled() == False:
                            if self.Pbutton3_1.isEnabled() == True:
                                self.rlist.append(self.Pbutton3_1)
                            if self.Pbutton3_3.isEnabled() == True:
                                self.rlist.append(self.Pbutton3_3)
                        self.computerPushButton(random.choice(self.rlist))

                elif self.Pbutton2_2.text() == "X":
                    self.isDualSame()
                    self.anyOneIsWinner()
                else:
                    self.LIST7 = []
                    if self.Pbutton1_1.isEnabled() == True:
                        self.LIST7.append(self.Pbutton1_1)

                    if self.Pbutton1_2.isEnabled() == True:
                        self.LIST7.append(self.Pbutton1_2)

                    if self.Pbutton1_3.isEnabled() == True:
                        self.LIST7.append(self.Pbutton1_3)

                    if self.Pbutton2_1.isEnabled() == True:
                        self.LIST7.append(self.Pbutton2_1)

                    if self.Pbutton2_2.isEnabled() == True:
                        self.LIST7.append(self.Pbutton2_2)

                    if self.Pbutton2_3.isEnabled() == True:
                        self.LIST7.append(self.Pbutton2_3)

                    if self.Pbutton3_1.isEnabled() == True:
                        self.LIST7.append(self.Pbutton3_1)

                    if self.Pbutton3_2.isEnabled() == True:
                        self.LIST7.append(self.Pbutton3_2)

                    if self.Pbutton3_3.isEnabled() == True:
                        self.LIST7.append(self.Pbutton3_3)
                    self.computerPushButton(random.choice(self.LIST7))
            else:
                self.anyOneIsWinner()
                self.isDualSame()
                self.anyOneIsWinner()

        elif len(self.nameOfAllEmptyButtons) == 5:
            #########first move was computer
            ##step 3
            if self.checkIfIsDualSame() == False:
                self.LIST8 = []
                if self.Pbutton1_1.isEnabled() == True:
                    self.LIST8.append(self.Pbutton1_1)
                if self.Pbutton1_3.isEnabled() == True:
                    self.LIST8.append(self.Pbutton1_3)
                if self.Pbutton3_1.isEnabled() == True:
                    self.LIST8.append(self.Pbutton3_1)
                if self.Pbutton3_3.isEnabled() == True:
                    self.LIST8.append(self.Pbutton3_3)
                if len(self.LIST8) == 1 and self.Pbutton2_2.text() == "X":
                    self.computerPushButton(self.LIST8[0])

                elif self.Pbutton2_2.text() == "X":
                    if self.checkIfIsDualSame() == True:
                        self.anyOneIsWinner()
                        self.isDualSame()
                        self.anyOneIsWinner()
                    else:
                        self.LIST9 = []
                        if self.Pbutton1_1.isEnabled() == True:
                            self.LIST9.append(self.Pbutton1_1)

                        if self.Pbutton1_2.isEnabled() == True:
                            self.LIST9.append(self.Pbutton1_2)

                        if self.Pbutton1_3.isEnabled() == True:
                            self.LIST9.append(self.Pbutton1_3)

                        if self.Pbutton2_1.isEnabled() == True:
                            self.LIST9.append(self.Pbutton2_1)

                        if self.Pbutton2_2.isEnabled() == True:
                            self.LIST9.append(self.Pbutton2_2)

                        if self.Pbutton2_3.isEnabled() == True:
                            self.LIST9.append(self.Pbutton2_3)

                        if self.Pbutton3_1.isEnabled() == True:
                            self.LIST9.append(self.Pbutton3_1)

                        if self.Pbutton3_2.isEnabled() == True:
                            self.LIST9.append(self.Pbutton3_2)

                        if self.Pbutton3_3.isEnabled() == True:
                            self.LIST9.append(self.Pbutton3_3)
                        self.computerPushButton(random.choice(self.LIST9))

                else:
                    if self.checkIfIsDualSame() == False:
                        self.LIST10 = []
                        if self.Pbutton1_1.isEnabled() == True:
                            self.LIST10.append(self.Pbutton1_1)
                        if self.Pbutton1_3.isEnabled() == True:
                            self.LIST10.append(self.Pbutton1_3)
                        if self.Pbutton3_1.isEnabled() == True:
                            self.LIST10.append(self.Pbutton3_1)
                        if self.Pbutton3_3.isEnabled() == True:
                            self.LIST10.append(self.Pbutton3_3)
                        self.computerPushButton(random.choice(self.LIST10))
            else:
                self.anyOneIsWinner()
                self.isDualSame()
                self.anyOneIsWinner()

        elif len(self.nameOfAllEmptyButtons) == 4:
            #########first move was player
            ## step 3
            if self.Pbutton2_2.text() == "O" and (
                    self.Pbutton1_2.text() == "O" or self.Pbutton2_1.text() == "O" or self.Pbutton2_3.text() == "O" or self.Pbutton3_2.text() == "O"):
                if self.checkIfIsDualSame() == True:
                    self.anyOneIsWinner()
                    self.isDualSame()
                    self.anyOneIsWinner()
                else:
                    self.LIST11 = []
                    if self.Pbutton1_1.isEnabled() == True:
                        self.LIST11.append(self.Pbutton1_1)

                    if self.Pbutton1_2.isEnabled() == True:
                        self.LIST11.append(self.Pbutton1_2)

                    if self.Pbutton1_3.isEnabled() == True:
                        self.LIST11.append(self.Pbutton1_3)

                    if self.Pbutton2_1.isEnabled() == True:
                        self.LIST11.append(self.Pbutton2_1)

                    if self.Pbutton2_2.isEnabled() == True:
                        self.LIST11.append(self.Pbutton2_2)

                    if self.Pbutton2_3.isEnabled() == True:
                        self.LIST11.append(self.Pbutton2_3)

                    if self.Pbutton3_1.isEnabled() == True:
                        self.LIST11.append(self.Pbutton3_1)

                    if self.Pbutton3_2.isEnabled() == True:
                        self.LIST11.append(self.Pbutton3_2)

                    if self.Pbutton3_3.isEnabled() == True:
                        self.LIST11.append(self.Pbutton3_3)
                    self.computerPushButton(random.choice(self.LIST11))

            else:
                if self.checkIfIsDualSame() == False:
                    self.LIST12 = []
                    if self.Pbutton1_1.isEnabled() == True:
                        self.LIST12.append(self.Pbutton1_1)

                    if self.Pbutton1_2.isEnabled() == True:
                        self.LIST12.append(self.Pbutton1_2)

                    if self.Pbutton1_3.isEnabled() == True:
                        self.LIST12.append(self.Pbutton1_3)

                    if self.Pbutton2_1.isEnabled() == True:
                        self.LIST12.append(self.Pbutton2_1)

                    if self.Pbutton2_2.isEnabled() == True:
                        self.LIST12.append(self.Pbutton2_2)

                    if self.Pbutton2_3.isEnabled() == True:
                        self.LIST12.append(self.Pbutton2_3)

                    if self.Pbutton3_1.isEnabled() == True:
                        self.LIST12.append(self.Pbutton3_1)

                    if self.Pbutton3_2.isEnabled() == True:
                        self.LIST12.append(self.Pbutton3_2)

                    if self.Pbutton3_3.isEnabled() == True:
                        self.LIST12.append(self.Pbutton3_3)
                    self.computerPushButton(random.choice(self.LIST12))
                else:
                    self.anyOneIsWinner()
                    self.isDualSame()
                    self.anyOneIsWinner()

        elif len(self.nameOfAllEmptyButtons) == 3:
            #########first move was computer
            ##step 4
            if self.checkIfIsDualSame() == True:
                # self.anyOneIsWinner()
                self.isDualSame()
                self.anyOneIsWinner()
            else:
                self.LIST13 = []
                if self.Pbutton1_1.isEnabled() == True:
                    self.LIST13.append(self.Pbutton1_1)

                if self.Pbutton1_2.isEnabled() == True:
                    self.LIST13.append(self.Pbutton1_2)

                if self.Pbutton1_3.isEnabled() == True:
                    self.LIST13.append(self.Pbutton1_3)

                if self.Pbutton2_1.isEnabled() == True:
                    self.LIST13.append(self.Pbutton2_1)

                if self.Pbutton2_2.isEnabled() == True:
                    self.LIST13.append(self.Pbutton2_2)

                if self.Pbutton2_3.isEnabled() == True:
                    self.LIST13.append(self.Pbutton2_3)

                if self.Pbutton3_1.isEnabled() == True:
                    self.LIST13.append(self.Pbutton3_1)

                if self.Pbutton3_2.isEnabled() == True:
                    self.LIST13.append(self.Pbutton3_2)

                if self.Pbutton3_3.isEnabled() == True:
                    self.LIST13.append(self.Pbutton3_3)
                self.computerPushButton(random.choice(self.LIST13))

        elif len(self.nameOfAllEmptyButtons) == 2:
            #########first move was plqyer
            ## step 4
            if self.checkIfIsDualSame() == True:
                self.anyOneIsWinner()
                self.isDualSame()
                self.anyOneIsWinner()
            else:
                self.LIST14 = []
                if self.Pbutton1_1.isEnabled() == True:
                    self.LIST14.append(self.Pbutton1_1)

                if self.Pbutton1_2.isEnabled() == True:
                    self.LIST14.append(self.Pbutton1_2)

                if self.Pbutton1_3.isEnabled() == True:
                    self.LIST14.append(self.Pbutton1_3)

                if self.Pbutton2_1.isEnabled() == True:
                    self.LIST14.append(self.Pbutton2_1)

                if self.Pbutton2_2.isEnabled() == True:
                    self.LIST14.append(self.Pbutton2_2)

                if self.Pbutton2_3.isEnabled() == True:
                    self.LIST14.append(self.Pbutton2_3)

                if self.Pbutton3_1.isEnabled() == True:
                    self.LIST14.append(self.Pbutton3_1)

                if self.Pbutton3_2.isEnabled() == True:
                    self.LIST14.append(self.Pbutton3_2)

                if self.Pbutton3_3.isEnabled() == True:
                    self.LIST14.append(self.Pbutton3_3)
                self.computerPushButton(random.choice(self.LIST14))

        elif len(self.nameOfAllEmptyButtons) == 1:
            #########first move was computer
            ##step 5
            if self.checkIfIsDualSame() == True:
                self.anyOneIsWinner()
                self.isDualSame()
                self.anyOneIsWinner()
            else:
                self.LIST15 = []
                if self.Pbutton1_1.isEnabled() == True:
                    self.LIST15.append(self.Pbutton1_1)

                if self.Pbutton1_2.isEnabled() == True:
                    self.LIST15.append(self.Pbutton1_2)

                if self.Pbutton1_3.isEnabled() == True:
                    self.LIST15.append(self.Pbutton1_3)

                if self.Pbutton2_1.isEnabled() == True:
                    self.LIST15.append(self.Pbutton2_1)

                if self.Pbutton2_2.isEnabled() == True:
                    self.LIST15.append(self.Pbutton2_2)

                if self.Pbutton2_3.isEnabled() == True:
                    self.LIST15.append(self.Pbutton2_3)

                if self.Pbutton3_1.isEnabled() == True:
                    self.LIST15.append(self.Pbutton3_1)

                if self.Pbutton3_2.isEnabled() == True:
                    self.LIST15.append(self.Pbutton3_2)

                if self.Pbutton3_3.isEnabled() == True:
                    self.LIST15.append(self.Pbutton3_3)
                self.computerPushButton(random.choice(self.LIST15))


styleSheet = """
MyWindow {
        background-image: url("final.jpg");
        background-repeat: no-repeat; 
        background-position: center;
    }
    """


def window():
    app = QApplication(sys.argv)
    app.setStyleSheet(styleSheet)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
