#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Alexander Bigulov 19.06.2020. Github: https://github.com/bialger/Holocorn

def errmsg(num, name):
    hexnum1 = hex(num)
    zero = ''
    for i in range(11-len(hexnum1[2:])):
        zero += '0'
    hexnum = hexnum1[:1]+zero+hexnum1[2:]
    print('Error! \nError number: '+hexnum+'. \nError name: '+name+'.')
#We import some necessary libraries, packages and classes ...
try:
    import hashlib
    import random
    import datetime
    import os
    import sys
    from PyQt5 import (QtWidgets, QtGui)
    from PyQt5.QtWidgets import (QWidget, QLineEdit, QTextEdit, QGridLayout,  QDesktopWidget, QMainWindow, QLabel, QToolTip, QComboBox, QPushButton, QMessageBox, QApplication, QFileDialog)
    from pathlib import Path
    from os.path import basename
    from PyQt5.QtCore import QCoreApplication
    from PyQt5.QtGui import (QFont, QIcon)
except ImportError:
    errmsg(38265, 'Error importing some packages. Try typing "pip install pyqt" at the command prompt')
    exit()
class Holocorn(QWidget): #Declare the main class. May the Force be with you! :)
    def color(self, cur_object, color="green"): #We declare a method that changes the font color. It will come in handy many more times.
        self.palette = cur_object.palette()
        self.palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color))
        cur_object.setPalette(self.palette)
    def __init__(self): #The usual technical method. Nothing interesting here.
        super().__init__()
        self.initUI()
    def initUI(self): #Declare the main method
        self.de = 'en' #We declare the variables that will be used to get the values entered by users.
        self.password = ''
        self.infile = ''
        self.infile2 = ''
        self.outfile = ''
        self.file2 = ''
        self.df = 'no'
        self.lan = 'rus'
        if sys.platform != 'win32':
            QWidget.setFont(self, QFont('Verdana', 11)) #Customize fonts ...
            QFileDialog.setFont(self, QFont('Verdana', 11))
            QtWidgets.QErrorMessage.setFont(self, QFont('Verdana', 11))
            QLabel.setFont(self, QFont('Verdana', 11))
            QLineEdit.setFont(self, QFont('Verdana', 11))
            QPushButton.setFont(self, QFont('Verdana', 11))
            QComboBox.setFont(self, QFont('Verdana', 11))
            QMessageBox.setFont(self, QFont('Verdana', 11))
        QToolTip.setFont(QFont('Times New Roman', 11))
        self.setToolTip('Holocorn 1.0 by bialger') #Set up a tooltip for the entire window, later configure for individual parts
        self.grid = QGridLayout() #Declare the layout type - grid
        self.grid.setSpacing(3) 
        self.setLayout(self.grid)
        self.lnel = QComboBox(self) #Create a drop-down list for choosing a language
        self.lnel.addItems(["Русский", "English"])
        self.lne4 = QComboBox(self) #Create a drop-down list to choose whether to delete the source file
        self.lne4.addItems(["Нет ", "Да  "])
        self.lne = QComboBox(self) #Create a drop-down list to select whether to encrypt or decrypt the source file
        self.lne.addItems(["Зашифровать", "Расшифровать"])
        self.lne23 = QLineEdit('', self) #Create text input fields
        self.lne1 = QLineEdit('', self)
        self.lne2 = QLineEdit('', self)
        self.lne3 = QLineEdit('', self)
        self.lbl1 = QLabel('Выберите опцию', self) #Create QLabels with information about input fields
        self.llbl = QLabel("Выберите язык", self)
        self.lbl11 = QLabel('Введите пароль', self)
        self.lbl12 = QLabel('Введите полный путь до исходного файла', self)
        self.lbl213 = QLabel('Введите путь до файла-ключа. Оставьте пустым для использования Crypt0     ', self)
        self.lbl13 = QLabel('Введите полный путь до файла назначения', self)
        self.lbl14 = QLabel('Удалить исходный файл?(да/нет)', self)
        self.lne23.setToolTip('Полный путь до файла-ключа') #Customize tips for added items
        self.lne.setToolTip('Опция шифрования (зашифровать или расшифровать)')
        self.lne1.setToolTip('Выберите сложный пароль, из минимум 8 символов, используя прописные и строчные латинские буквы, цифры и спецсимволы')
        self.lne2.setToolTip('Полный путь до исходного файла')
        self.lne3.setToolTip('Полный путь до файла назначения')
        self.lnel.setToolTip('Язык')
        self.lne4.setToolTip('Удалить исхоный файл')
        self.lbl233 = QLabel('Вы ничего не выбрали', self) #We declare QLabels to show what the user has selected.
        self.lrlbl = QLabel('Текущий язык: Русский')
        self.lbl3 = QLabel('Применена опция по умолчанию(зашифровать)', self)
        self.lbl31 = QLabel('Вы ничего не выбрали', self)
        self.lbl32 = QLabel('Вы ничего не выбрали', self)
        self.lbl33 = QLabel('Вы ничего не выбрали', self)
        self.lbl34 = QLabel('Применена опция по умолчанию(нет)', self)
        self.fslbl = QLabel('', self) #Empty QLabels ... It Should Be Just That, Honestly
        self.lbl223 = QLabel('', self)
        lbl2 = QLabel('', self)
        lbl21 = QLabel('', self)
        lbl22 = QLabel('', self)
        lbl23 = QLabel('', self)
        lbl24 = QLabel('', self)
        self.defin1 = QLabel('Если возникли вопросы, пишите на email artur.bigulov@yandex.ru', self) #
        self.btn = QPushButton("Шифровать!", self) #Create buttons ...
        self.btn1 = QPushButton("Случайный пароль", self)
        self.btn2 = QPushButton("По умолчанию", self)
        self.btn3 = QPushButton("По умoлчанию", self)
        self.chb2 = QPushButton("Выберите файл", self)
        self.btn.setToolTip('Применить алгоритм шифрования') #Customize tooltips for these buttons
        self.btn1.setToolTip('Надежный двенадцатисимвольный пароль из аглийских букв, символов и цифр')
        self.btn2.setToolTip('Выходной файл по умолчанию, вида [имя_исходного_файла].holocorn')
        self.btn3.setToolTip('Файл-ключ по умолчанию, вида [имя_исходного_файла].key')
        self.chb2.setToolTip('Открывает окно выбора исходного файла')
        self.btn.clicked.connect(self.crypt) #We connect with processing methods all objects with which the user interacts
        self.btn1.clicked.connect(self.rand_pass)
        self.btn2.clicked.connect(self.def_outfile)
        self.btn3.clicked.connect(self.def_file2)
        self.chb2.clicked.connect(self.chooseInfile)
        self.lne1.textChanged[str].connect(self.ch_passw)
        self.lne3.textChanged[str].connect(self.ch_outfile)
        self.lne23.textChanged[str].connect(self.ch_file2)
        self.lne.activated[str].connect(self.ch_type)
        self.lne4.activated[str].connect(self.ch_desfile)
        self.lnel.activated[str].connect(self.ch_lan)
        self.color(self.lbl3) #Repainting QLabels with user selection information
        self.color(self.lrlbl)
        self.color(self.lbl31, "red")
        self.color(self.lbl32, "red")
        self.color(self.lbl33, "red")
        self.color(self.lbl233, "red")
        self.color(self.lbl34)
        self.grid.addWidget(self.lbl1, 2, 1) #Customize the objects in the grid ...
        self.grid.addWidget(lbl2, 1, 1)
        self.grid.addWidget(self.lne, 3, 1)
        self.grid.addWidget(self.lbl3, 4, 1)
        self.grid.addWidget(self.lbl11, 6, 1)
        self.grid.addWidget(lbl21, 5, 1)
        self.grid.addWidget(self.lne1, 7, 1)
        self.grid.addWidget(self.lbl31, 9, 1)
        self.grid.addWidget(self.lbl12, 11, 1)
        self.grid.addWidget(lbl22, 10, 1)
        self.grid.addWidget(self.lne2, 12, 1)
        self.grid.addWidget(self.chb2, 12, 1)
        self.grid.addWidget(self.lbl32, 13, 1)
        self.grid.addWidget(self.lbl13, 15, 1)
        self.grid.addWidget(lbl23, 14, 1)
        self.grid.addWidget(self.lne3, 16, 1)
        self.grid.addWidget(self.lbl33, 18, 1)
        self.grid.addWidget(self.lbl14, 20, 1)
        self.grid.addWidget(lbl24, 19, 1)
        self.grid.addWidget(self.lne4, 21, 1)
        self.grid.addWidget(self.lbl34, 22, 1)
        self.grid.addWidget(self.defin1, 23, 1)
        self.grid.addWidget(self.btn, 24, 1)
        self.grid.addWidget(self.btn1, 8, 1)
        self.grid.addWidget(self.btn2, 17, 1)
        self.grid.addWidget(self.fslbl, 1, 2)
        self.grid.addWidget(self.llbl, 2, 2)
        self.grid.addWidget(self.lnel, 3, 2)
        self.grid.addWidget(self.lrlbl, 4, 2)
        self.grid.addWidget(self.fslbl, 5, 2)
        self.grid.addWidget(self.fslbl, 6, 2)
        self.grid.addWidget(self.fslbl, 7, 2)
        self.grid.addWidget(self.fslbl, 8, 2)
        self.grid.addWidget(self.fslbl, 9, 2)
        self.grid.addWidget(self.fslbl, 10, 2)
        self.grid.addWidget(self.fslbl, 11, 2)
        self.grid.addWidget(self.fslbl, 12, 2)
        self.grid.addWidget(self.fslbl, 13, 2)
        self.grid.addWidget(self.lbl213, 15, 2)
        self.grid.addWidget(self.lbl223, 14, 2)
        self.grid.addWidget(self.lne23, 16, 2)
        self.grid.addWidget(self.btn3, 17, 2)
        self.grid.addWidget(self.lbl233, 18, 2)
        self.grid.addWidget(self.fslbl, 19, 2)
        self.grid.addWidget(self.fslbl, 20, 2)
        self.grid.addWidget(self.fslbl, 21, 2)
        self.grid.addWidget(self.fslbl, 22, 2)
        self.grid.addWidget(self.fslbl, 23, 2)
        self.grid.addWidget(self.fslbl, 24, 2)
        self.center() #We use a special method to position objects in the center
        self.setWindowTitle('Holocorn 1.0 Personal Jesus') #Customize the window title
        self.setWindowIcon(QIcon('zamok.png')) #Set the program icon
        self.show() #Show all
        self.en = ['q','w','e','r','t','y','u','i','o','p', #Special array. I need him honestly
          'a','s','d','f','g','h','j','k','l',
          'z','x','c','v','b','n','m',',','.',  
          '1','2','3','4','5','6','7','8','9','0',
          ';','(',')','+',
          'Q','W','E','R','T','Y','U','I','O','P',
          'A','S','D','F','G','H','J','K','L',
          'Z','X','C','V','B','N','M',]
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def chooseInfile2(self):
        file_dialog = QFileDialog.getOpenFileName(self, "Open file")
        if file_dialog[0] != "":
            self.file2 = file_dialog[0]
            self.color(self.lbl33)
            self.color(self.lbl233)
            msg = 'Файл-ключ: '
            if self.lan == 'en':
                msg = 'Key file: '
            self.lbl233.setText(msg+basename(file_dialog[0]))
            self.lne3.setText(file_dialog[0][:-4])
            self.outfile = file_dialog[0][:-4]
            msg = 'Итоговый файл: '
            if self.lan == 'en':
                msg = 'End file: '
            self.lbl33.setText(msg+basename(file_dialog[0][:-4]))
    def chooseInfile(self):
        file_dialog = QFileDialog.getOpenFileName(self, "Open file")
        if file_dialog[0] != "":
            self.infile = file_dialog[0]
            self.color(self.lbl32)
            self.color(self.lbl33)
            self.color(self.lbl233)
            msg = 'Первый начальный файл: '
            if self.lan == 'en':
                msg = 'First start file: '
            self.lbl32.setText(msg+basename(file_dialog[0]))
            if self.de == "en":
                self.lne3.setText(file_dialog[0]+".holocorn")
                self.lne23.setText(file_dialog[0]+".key")
                self.outfile = file_dialog[0]+".holocorn"
                self.file2 = file_dialog[0]+".key"
                msg = 'Итоговый файл: '
                if self.lan == 'en':
                    msg = 'End file: '
                self.lbl33.setText(msg+basename(file_dialog[0]+".holocorn"))
                msg = 'Файл-ключ: '
                if self.lan == 'en':
                    msg = 'Key file: '
                self.lbl233.setText(msg+basename(file_dialog[0]+".key"))
            else:
                self.lne3.setText(file_dialog[0][:-9])
                self.outfile = file_dialog[0][:-9]
                msg = 'Итоговый файл: '
                if self.lan == 'en':
                    msg = 'End file: '
                self.lbl33.setText(msg+basename(file_dialog[0][:-9]))
    def errmsg(self, num, name):
        hexnum1 = hex(num)
        zero = ''
        for i in range(11-len(hexnum1[2:])):
            zero += '0'
        hexnum = hexnum1[:1]+zero+hexnum1[2:]
        error_dialog = QtWidgets.QErrorMessage(self)
        error_dialog.showMessage("Error! \nError number: "+hexnum+". \nError name: "+name+".")
    def ch_passw(self, text):
        self.password = text
        if self.password != '':
            self.color(self.lbl31)
            msg = 'Ваш пароль: '
            if self.lan == 'en':
                msg = 'Your password: '
            self.lbl31.setText(msg+text)
        else:
            self.color(self.lbl31, "red")
            msg = 'Вы ничего не выбрали'
            if self.lan == 'en':
                msg = 'You didn`t selected anything'
            self.lbl31.setText(msg)
    def ch_outfile(self, text):
        self.outfile = text
        if self.outfile != '':
            self.color(self.lbl33)
            msg = 'Итоговый файл: '
            if self.lan == 'en':
                msg = 'End file: '
            self.lbl33.setText(msg+text)
        else:
            self.color(self.lbl33, "red")
            msg = 'Вы ничего не выбрали'
            if self.lan == 'en':
                msg = 'You didn`t choose anything'
            self.lbl33.setText(msg)
    def ch_file2(self, text):
        self.file2 = text
        if self.file2 != '':
            self.color(self.lbl233)
            msg = 'Файл-ключ: '
            if self.lan == 'en':
                 msg = 'Key file: '
            self.lbl233.setText(msg+text)
        else:
            self.color(self.lbl233, "red")
            msg = 'Вы ничего не выбрали'
            if self.lan == 'en':
                msg = 'You didn`t choose anything'
            self.lbl233.setText(msg)
    def ch_type(self, text):
        self.color(self.lbl3)
        msg = 'Вы выбрали: '
        if self.lan == 'en':
            msg = 'You selected: '
        self.lbl3.setText(msg+text)
        if (text == 'Зашифровать') or (text == 'Encrypt'):
            if self.de == 'decr':
                self.lne23 = QLineEdit('', self)
                self.lne23.setToolTip('Полный путь до файла-ключа')
                if self.lan == "en":
                    self.lne23.setToolTip('Full path to the key file')
                self.btn3 = QPushButton("По умoлчанию", self)
                if self.lan == "en":
                    self.btn3.setText("Default")
                self.btn3.setToolTip('Файл-ключ по умолчанию, вида [имя_исходного_файла].key')
                if self.lan == "en":
                    self.btn3.setToolTip ('Default key file of the form [source_name].key')
                self.btn3.clicked.connect(self.def_file2)
                self.lne23.setText(self.file2)
                self.lne23.textChanged[str].connect(self.ch_file2)
                self.chb3.deleteLater()
            self.grid.addWidget(self.lbl213, 15, 2)
            self.grid.addWidget(self.lbl223, 14, 2)
            self.grid.addWidget(self.lne23, 16, 2)
            self.grid.addWidget(self.btn3, 17, 2)
            self.grid.addWidget(self.lbl233, 18, 2)
            self.grid.addWidget(self.fslbl, 11, 2)
            self.grid.addWidget(self.fslbl, 12, 2)
            self.grid.addWidget(self.fslbl, 13, 2)
            self.de = 'en'
        else:
            if self.de == 'en':
                self.chb3 = QPushButton("Выберите файл", self)
                if self.lan == "en":
                    self.chb3.setText("Choose file")
                self.chb3.setToolTip('Открывает окно выбора файла-ключа')
                if self.lan == "en":
                    self.chb3.setToolTip ('Opens the key file selection window')
                self.chb3.clicked.connect(self.chooseInfile2)
                self.lne23.deleteLater()
                self.btn3.deleteLater()
            self.grid.addWidget(self.lbl213, 11, 2)
            self.grid.addWidget(self.chb3, 12, 2)
            self.grid.addWidget(self.lbl233, 13, 2)
            self.grid.addWidget(self.fslbl, 14, 2)
            self.grid.addWidget(self.fslbl, 15, 2)
            self.grid.addWidget(self.fslbl, 16, 2)
            self.grid.addWidget(self.fslbl, 17, 2)
            self.grid.addWidget(self.fslbl, 18, 2)
            self.de = 'decr'
    def ch_desfile(self, text):
        self.color(self.lbl34)
        msg = 'Вы выбрали: '
        if self.lan == 'en':
            msg = 'You selected: '
        self.lbl34.setText(msg+text)
        if (text == 'Да  ') or (text == 'Yes '):
            self.df = 'Yes'
        else:
            self.df = 'no'
    def ch_lan(self, text):
        self.color(self.lrlbl)
        if text == 'Русский':
            self.lan = 'rus'
            self.btn.setText("Шифровать!")
            self.btn1.setText("Случайный пароль")
            self.btn2.setText("По умолчанию")
            if self.de == 'en':
                self.btn3.setText("По умoлчанию")
            else:
                self.chb3.setText("Выберите файл")
            self.chb2.setText("Выберите файл")
            self.lne.removeItem(0)
            self.lne.removeItem(0)
            arr = ['Зашифровать', 'Расшифровать']
            if self.de == 'decr':
                arr = ['Расшифровать', 'Зашифровать']
            self.lne.addItems(arr)
            self.lne4.removeItem(0)
            self.lne4.removeItem(0)
            arr = ['Нет ', 'Да  ']
            if self.df == 'Yes':
                arr = ['Да  ', 'Нет ']
            self.lne4.addItems(arr)
            self.lne.setToolTip('Опция шифрования (зашифровать или расшифровать)')
            self.lne1.setToolTip('Выберите сложный пароль, из минимум 8 символов, используя прописные и строчные латинские буквы, цифры и спецсимволы')
            self.lne2.setToolTip('Полный путь до исходного файла')
            self.lne3.setToolTip('Полный путь до файла назначения')
            self.lnel.setToolTip('Язык')
            self.lne4.setToolTip('Удалить исходный файл')
            if self.de == 'en':
                self.lne23.setToolTip('Полный путь до файла-ключа')
            self.btn.setToolTip('Применить алгоритм шифрования')
            self.btn1.setToolTip('Надежный двенадцатисимвольный пароль из аглийских букв, символов и цифр')
            self.btn2.setToolTip('Выходной файл по умолчанию, вида [имя_исходного_файла].holocorn')
            if self.de == 'en':
                self.btn3.setToolTip('Файл-ключ по умолчанию, вида [имя_исходного_файла].key')
            else:
                self.chb3.setToolTip('Открывает окно выбора файла-ключа')
            self.chb2.setToolTip('Открывает окно выбора исходного файла')
            self.defin1.setText('Если возникли вопросы, пишите на email artur.bigulov@yandex.ru')
            self.lbl1.setText('Выберите опцию')
            self.llbl.setText("Выберите язык")
            self.lbl11.setText('Введите пароль')
            self.lbl12.setText('Введите полный путь до исходного файла')
            self.lbl213.setText('Введите путь до файла-ключа. Оставьте пустым для использования Crypt0     ')
            self.lbl13.setText('Введите полный путь до файла назначения')
            self.lbl14.setText('Удалить исходный файл?(да/нет)')
            if self.file2 == '':
                self.lbl233.setText('Вы ничего не выбрали')
            elif self.file2 == 'def':
                self.lbl233.setText('Файл-ключ: по умолчанию')
            else:
                self.lbl233.setText('Файл-ключ: '+self.file2)
            if self.de == 'en':
                self.lbl3.setText('Применена опция по умолчанию(зашифровать)')
            else:
                self.lbl3.setText('Вы выбрали: Расшифровать')
            self.lrlbl.setText('Текущий язык: '+text)
            if self.password == '':
                self.lbl31.setText('Вы ничего не выбрали')
            elif len(self.password) == 12:
                self.lbl31.setText('Ваш пароль(не забудьте скопировать!): '+self.password)
            else:
                self.lbl31.setText('Ваш пароль: '+self.password)
            if self.infile == '':
                self.lbl32.setText('Вы ничего не выбрали')
            elif self.infile == 'def':
                self.lbl32.setText('Начальный файл: по умолчанию')
            else:
                self.lbl32.setText('Начальный файл: '+basename(self.infile))
            if self.outfile == '':
                self.lbl33.setText('Вы ничего не выбрали')
            elif self.outfile == 'def':
                self.lbl33.setText('Конечный файл: по умолчанию')
            else:
                self.lbl33.setText('Конечный файл: '+self.outfile)
            if self.df == 'no':
                self.lbl34.setText('Применена опция по умолчанию(нет)')
            else:
                self.lbl34.setText('Вы выбрали: Да')
            self.grid.addWidget(self.btn, 24, 1)
            self.grid.addWidget(self.btn1, 8, 1)
            self.grid.addWidget(self.btn2, 17, 1)
            if self.de == "en":
                self.grid.addWidget(self.btn3, 17, 2)
            else:
                self.grid.addWidget(self.chb3, 12, 2)
            self.grid.addWidget(self.chb2, 12, 1)
        else:
            self.lan = 'en'
            self.lrlbl.setText('Current language: '+text)
            self.btn.setText("Crypt!")
            self.btn1.setText("Random password")
            self.btn2.setText("Default")
            if self.de == 'en':
                self.btn3.setText("Defаult")
            else:
                self.chb3.setText("Choose file")
            self.chb2.setText("Choose file")
            self.lne.removeItem (0)
            self.lne.removeItem (0)
            arr = ['Encrypt', 'Decrypt']
            if self.de == 'decr':
                arr = ['Decrypt', 'Encrypt']
            self.lne.addItems (arr)
            self.lne4.removeItem (0)
            self.lne4.removeItem (0)
            arr = ['No  ', 'Yes ']
            if self.df == 'Yes':
                arr = ['Yes ', 'No  ']
            self.lne4.addItems (arr)
            self.lne.setToolTip ('Encryption option (encrypt or decrypt)')
            self.lne1.setToolTip ('Choose a strong password, at least 8 characters, using uppercase and lowercase Latin letters, numbers and special characters')
            self.lne2.setToolTip ('Full path to source file')
            self.lne3.setToolTip ('Full path to destination file')
            self.lnel.setToolTip ('Language')
            self.lne4.setToolTip ('Delete source file')
            self.defin1.setText('If you have questions, write to email artur.bigulov@yandex.ru')
            self.lbl1.setText ('Select an option')
            if self.de == 'en':
                self.lne23.setToolTip ('Full path to the key file')
            self.btn.setToolTip ('Apply encryption algorithm')
            self.btn1.setToolTip ('Strong twelve-character password from English letters, characters and numbers')
            self.btn2.setToolTip ('The default output file, of the form [source_name].holocorn')
            if self.de == 'en':
                self.btn3.setToolTip ('Default key file of the form [source_name].key')
            else:
                self.chb3.setToolTip ('Opens the key file selection window')
            self.chb2.setToolTip ('Opens the source file selection window')
            self.llbl.setText ("Choose your language")
            self.lbl11.setText ('Enter password')
            self.lbl12.setText ('Enter the full path to the source file')
            self.lbl213.setText ('Enter the full path to the key file. Leave blank to use Crypt0                         ')
            self.lbl13.setText ('Enter the full path to the destination file')
            self.lbl14.setText ('Delete the source file? (yes / no)')
            if self.file2 == '':
                self.lbl233.setText ('You didn`t selected anything')
            elif self.file2 == 'def':
                self.lbl233.setText ('Key file: default')
            else:
                self.lbl233.setText ('Key file: ' + self.file2)
            if self.de == 'en':
                self.lbl3.setText ('Default option applied (encrypt)')
            else:
                self.lbl3.setText ('You choosed: Decrypt')
            self.lrlbl.setText ('Current language:' + text)
            if self.password == '':
                self.lbl31.setText ('You didn`t selected anything')
            elif len (self.password) == 12:
                self.lbl31.setText ('Your password(do not forget to copy!):' + self.password)
            else:
                self.lbl31.setText ('Your password:' + self.password)
            if self.infile == '':
                self.lbl32.setText ('You didn`t selected anything')
            elif self.infile == 'def':
                self.lbl32.setText ('Start file: default')
            else:
                self.lbl32.setText ('Start file: ' + basename (self.infile))
            if self.outfile == '':
                self.lbl33.setText ('You didn`t selected anything')
            elif self.outfile == 'def':
                self.lbl33.setText ('End file: default')
            else:
                self.lbl33.setText ('End file: ' + self.outfile)
            if self.df == 'no':
                self.lbl34.setText ('Default option applied (no)')
            else:
                self.lbl34.setText ('You selected: Yes')
            self.grid.addWidget(self.btn, 24, 1)
            self.grid.addWidget(self.btn1, 8, 1)
            self.grid.addWidget(self.btn2, 17, 1)
            if self.de == "en":
                self.grid.addWidget(self.btn3, 17, 2)
            else:
                self.grid.addWidget(self.chb3, 12, 2)
            self.grid.addWidget(self.chb2, 12, 1)
    def crypt(self):
        def sha512(password):
            return int(hashlib.sha512(password.encode('utf-8')).hexdigest(), 16)
        def encfile (self, password, infile, outfile, file2):
            start = datetime.datetime.now()
            crypt0 = False
            if file2 != '':
                if file2 == 'def':
                    file2 = infile+'.key'
            else:
                crypt0 = True
            errhap = 1
            bet = 2
            try:
                with open(infile, "rb") as handle:
                    data = handle.readlines()
                    bet = len(b''.join(data))
            except FileNotFoundError:
                self.errmsg(16387823, 'There is no file like '+infile)
                errhap = 0
            except IsADirectoryError:
                self.errmsg(636776, infile+' is a directory')
                errhap = 0
            except Exception:
                self.errmsg(2983756, 'Unknown error')
                errhap = 0
            if errhap != 0:
                if bet > 10000000:
                    msg = "Размер вашего файла превышает 10 МБайт. Вы точно хотите продолжить?"
                    if self.lan == 'en':
                        msg = "Your file is larger than 10 MB. Are you sure you want to continue?"
                    reply = QMessageBox.question(self, 'Warning', msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        shaint = sha512(password)
                        key = 1
                        if crypt0 == False:
                            key = random.randint(10**99999, 10**100000)
                        beta = b''.join(data)
                        aleph = int.from_bytes(beta, byteorder='big')
                        l = aleph*shaint*key
                        gamma = l.to_bytes((len(bin(l))// 8) + 1, byteorder='big')
                        ac = b''
                        for i in data[0]:
                            if 0 == i:
                                ac += b'\x00'
                            else:
                                break
                        ab = len(ac)
                        c = ab.to_bytes(len(bin(ab))//8 +1, byteorder='big')    
                        c += b'\n'
                        c += gamma
                        if crypt0 == False:
                            with open(file2, "wb") as handle1:
                                handle1.write(key.to_bytes((len(bin(key))// 8) + 1, byteorder='big'))
                        with open(outfile, "wb") as handle1:
                            handle1.write(c)
                        end = datetime.datetime.now()
                        time = end - start
                        title = 'Зашифровано!'
                        msg1 = 'Программа работала '
                        msg2 = ' времени.'
                        if self.lan == 'en':
                            title = 'Encrypted!'
                            msg1 = 'Programm worked for '
                            msg2 = '.'
                        reply = QMessageBox.question(self, title, msg1+str(time)+msg2, QMessageBox.Yes)
                        if reply == QMessageBox.Yes:
                            pass
                        else:
                            pass
                    else:
                        pass
                else:
                    key = 1
                    if crypt0 == False:
                        key = random.randint(10**99999, 10**100000)
                    shaint = sha512(password)
                    beta = b''.join(data)
                    aleph = int.from_bytes(beta, byteorder='big')
                    l = aleph*shaint*key
                    gamma = l.to_bytes((len(bin(l))// 8) + 1, byteorder='big')
                    ac = b''
                    for i in data[0]:
                        if 0 == i:
                            ac += b'\x00'
                        else:
                            break
                    ab = len(ac)
                    c = ab.to_bytes(len(bin(ab))//8 +1, byteorder='big')    
                    c += b'\n'
                    c += gamma
                    if crypt0 == False:
                        with open(file2, "wb") as handle1:
                            handle1.write(key.to_bytes((len(bin(key))// 8) + 1, byteorder='big'))
                    with open(outfile, "wb") as handle1:
                        handle1.write(c)
                    end = datetime.datetime.now()
                    time = end - start
                    title = 'Зашифровано!'
                    msg1 = 'Программа работала '
                    msg2 = ' времени.'
                    if self.lan == 'en':
                        title = 'Encrypted!'
                        msg1 = 'Programm worked for '
                        msg2 = '.'
                    reply = QMessageBox.question(self, title, msg1+str(time)+msg2, QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        pass
                    else:
                        pass
        def decfile (self, password, infile, outfile, file2):
            start = datetime.datetime.now()
            crypt0 = False
            if file2 != '':
                if file2 == 'def':
                    file2 = infile[:-9]+'.key'
            else:
                crypt0 = True
            errhap = 1
            first = infile
            key = 1
            try:
                with open(infile, "rb") as handle:
                    data = handle.readlines()
                    bet = len(b''.join(data))
                if crypt0 == False:
                    first = file2
                    with open(file2, "rb") as handle:
                        key = int.from_bytes(b''.join(handle.readlines()), byteorder='big')
            except FileNotFoundError:
                self.errmsg(2084375, 'There is no file like '+first)
                errhap = 0
            except IsADirectoryError:
                self.errmsg(86576, first+' is a directory')
                errhap = 0
            except Exception:
                self.errmsg(92436, 'Unknown error')
                errhap = 0
            if errhap != 0:
                shaint = sha512(password)
                a = list(data[0]).copy()
                a.pop()
                ac = b''
                for i in range(a[0]):
                    ac += b'\x00'
                neid = b''.join(data[1:])
                aleph = int.from_bytes(neid, byteorder='big')
                l = aleph // shaint
                l = l // key
                gamma = l.to_bytes((len(bin(l)) // 8) + 1, byteorder='big')[1:]
                ac += gamma
                with open(outfile, "wb") as handle1:
                    handle1.write(ac)
                end = datetime.datetime.now()
                time = end - start
                title = 'Расшифровано!'
                msg1 = 'Программа работала '
                msg2 = ' времени.'
                if self.lan == 'en':
                    title = 'Decrypted!'
                    msg1 = 'Programm worked for '
                    msg2 = '.'
                reply = QMessageBox.question(self, title, msg1+str(time)+msg2, QMessageBox.Yes)
                if reply == QMessageBox.Yes:
                    pass
                else:
                    pass
        def desfile(self, file):
            errhap = 1
            try:
                with open(file, 'rb') as f0:
                    data = f0.readlines()
                    b = 0
                    for i in data:
                        b += len(list(i))
            except FileNotFoundError:
                self.errmsg(42976, 'There is no file like '+file)
                errhap = 0
            except IsADirectoryError:
                self.errmsg(57042534, file+' is a directory')
                errhap = 0
            if errhap != 0:
                for i in range(10):
                    with open(file, 'wb') as f1:
                        f1.write(os.urandom(b))
                os.remove(file)
        if self.infile != '' and self.outfile != '' and self.password != '':
            msg = "Вы уверены, что ввели все правильно?"
            if self.lan == 'en':
                msg = "Are you sure you entered everything correctly?"
            reply = QMessageBox.question(self, 'Encryption', msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                if 'en' in self.de:
                    if self.outfile == 'def':
                        c = self.df
                        mod = '.holocorn'
                        if self.file2 == '':
                            mod = '.crypt0'
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            encfile(self, self.password, self.infile, self.infile+mod, self.file2)
                            desfile(self, self.infile)
                        else:
                            encfile(self, self.password, self.infile, self.infile+mod, self.file2)
                    else:
                        c = self.df
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            encfile(self, self.password, self.infile, self.outfile, self.file2)
                            desfile(self, self.infile)
                        else:
                            encfile(self, self.password, self.infile, self.outfile, self.file2)
                else:
                    if self.outfile == 'def':
                        c = self.df
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            if self.infile[:-9] != '':
                                self.outfile = self.infile[:-9]
                                if self.file2 == '':
                                    self.outfile = self.infile[:-7]
                                decfile(self, self.password, self.infile, self.outfilefile, self.file2)
                                desfile(self, self.infile)
                                if self.file2 == 'def':
                                    self.file2 = self.infile[:-9]+'.key'
                                desfile(self, self.file2)
                            else:
                                self.errmsg(92475, 'The name of the original file is too small for a default option')
                        else:
                            if self.infile[:-9] != '':
                                self.outfile = self.infile[:-9]
                                if self.file2 == '':
                                    self.outfile = self.infile[:-7]
                                decfile(self, self.password, self.infile, self.outfilefile, self.file2)
                            else:
                                self.errmsg(834574, 'The name of the original file is too small for a default option')
                    else:
                        c = self.df
                        if 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c:
                            if self.infile[:-4] != '':
                                decfile(self, self.password, self.infile, self.outfile, self.file2)
                                desfile(self, self.infile)
                                if self.file2 == 'def':
                                    self.file2 = self.infile[:-9]+'.key'
                                desfile(self, self.file2)
                            else:
                                self.errmsg(4562865, 'The name of the original file is too small for a default option')
                        else:                        
                            decfile(self, self.password, self.infile, self.outfile, self.file2)
        else:
            msg = 'Вы ввели недостаточно данных'
            if self.lan == 'en':
                msg = 'You have entered insufficient data'
            self.errmsg(236239, msg)
    def rand_pass(self):
        self.password = ''.join(random.sample(self.en, 12))
        self.lne1.setText(self.password)
        msg = 'Ваш пароль(не забудьте скопировать!): '
        if self.lan == 'en':
            msg = 'Your password(do not forget to copy!): '
        self.lbl31.setText(msg+self.password)
    def def_outfile(self):
        self.outfile = 'def'
        self.color(self.lbl33)
        msg = 'Итоговый файл: по умолчанию'
        if self.lan == 'en':
            msg = 'End file: default'
        self.lbl33.setText(msg)
    def def_file2(self):
        if self.de == 'en':  
            self.outfile2 = 'def'
            self.color(self.lbl233)
            msg = 'Файл-ключ: по умолчанию'
            if self.lan == 'en':
                msg = 'Key file: default'
            self.lbl233.setText(msg)
    def closeEvent(self, event):
        msg = "Вы точно хотите выйти?"
        if self.lan == 'en':
            msg = "Do you really want to quit?"
        reply = QMessageBox.question(self, 'Exit', msg, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
def help():
    print('Использование:')
    print('  holocorn <опции1> <опции2>')
    print('Опции1:')
    print('  Зашифровка:')
    print('    "-e" или "-en" или "--encr" или "--encrypt"')
    print('  Расшифровка:')
    print('    "-d" или "-de" или "--decr" или "--decrypt"')
    print('  Справка:')
    print('    "--help"')
    print('Опции2:')
    print('  "-rp" - случайный пароль(только при зашифровке)')
    print('  "-p" - следующий аргумент - пароль')
    print('  "-if" - следующий аргумент - путь к исходному файлу')
    print('  "-of" - следующий аргумент - путь к конечному файлу')
    print('  "-kf" - следующий аргумент - путь к файлу-ключу. Не используйте для активации стандартного алгорита Crypt0')
    print('  "-df" - путь к конечному файлу по умолчанию')
    print('  "-dk" - путь к файлу-ключу по умолчанию')
    print('  "-dd" - уничтожить исходный файл')
en = ['q','w','e','r','t','y','u','i','o','p',
      'a','s','d','f','g','h','j','k','l',
      'z','x','c','v','b','n','m',',','.',  
      '1','2','3','4','5','6','7','8','9','0',
      '(',')','+',
      'Q','W','E','R','T','Y','U','I','O','P',
      'A','S','D','F','G','H','J','K','L',
      'Z','X','C','V','B','N','M',]
def sha512(password):
    return int(hashlib.sha512(password.encode('utf-8')).hexdigest(), 16)
def encfile (infile, outfile, password, file2):
    print('Начинается шифрование...')
    start = datetime.datetime.now()
    crypt0 = False
    if file2 != '':
        if file2 == 'def':
            file2 = infile+'.key'
    else:
        crypt0 = True
    print('Время начала шифрования', str(start))
    errhap = 1
    try:
        with open(infile, "rb") as handle:
            data = handle.readlines()
            bet = len(b''.join(data))
    except FileNotFoundError:
        print('Ошибка! Файла '+infile+' не существует!')
        errhap = 0
    except IsADirectoryError:
        print('Ошибка! '+infile+' - это папка')
        errhap = 0
    if errhap != 0:
        print('Файл имеет размер', bet/1000, 'KiB')
        key = 1
        if bet > 10000000:
            print('!!!ВНИМАНИЕ!!!')
            print('Размер вашего файла превышет 10 MiB.')
            c = input('Вы точно хотите продолжить?(yes/no): ')
            cb = 'Y' in c or 'y' in c or 'YES' in c or 'yes' in c or 'Д' in c or 'д' in c or 'ДА' in c or 'да' in c
            if cb == False: 
                exit()
        if crypt0 == False:
            key = random.randint(10**99999, 10**100000)
        shaint = sha512(password)
        beta = b''.join(data)
        aleph = int.from_bytes(beta, byteorder='big')
        l = aleph*shaint*key
        gamma = l.to_bytes((len(bin(l))// 8) + 1, byteorder='big')
        ac = b''
        for i in data[0]:
            if 0 == i:
                ac += b'\x00'
            else:
                break
        ab = len(ac)
        c = ab.to_bytes(len(bin(ab))//8 +1, byteorder='big')    
        c += b'\n'
        c += gamma
        if crypt0 == False:
            with open(file2, "wb") as handle1:
                handle1.write(key.to_bytes((len(bin(key))// 8) + 1, byteorder='big'))
        with open(outfile, "wb") as handle2:
            handle2.write(c)
        print('Шифрование окончено! Ваши данные в безопасности!')
        end = datetime.datetime.now()
        time = end - start
        print('Программа закончила выполнение в', str(end))
        print('Программа работала', str(time), 'времени')
        input ("Нажмите для выхода ... ")
def decfile (infile, outfile, password, file2):
    print('Начинаем расшифровку...')
    start = datetime.datetime.now()
    crypt0 = False
    if file2 != '':
        if file2 == 'def':
            file2 = infile[:-9]+'.key'
    else:
        crypt0 = True
    print('Время начала шифрования', str(start))
    errhap = 1
    key = 1
    first = infile
    try:
        with open(infile, "rb") as handle:
            data = handle.readlines()
            bet = len(b''.join(data))
        if crypt0 == False:
            first = file2
            with open(file2, "rb") as handle:
                key = int.from_bytes(b''.join(handle.readlines()), byteorder='big')
    except FileNotFoundError:
        print('Ошибка! Файла '+first+' не существует!')
        errhap = 0
    except IsADirectoryError:
        print('Ошибка! '+first+' - это папка')
        errhap = 0
    if errhap != 0:
        print('Файл имеет размер', bet/1000, 'KiB')
        shaint = sha512(password)
        a = list(data[0]).copy()
        a.pop()
        ac = b''
        for i in range(a[0]):
            ac += b'\x00'
        neid = b''.join(data[1:])
        aleph = int.from_bytes(neid, byteorder='big')
        l = aleph // shaint
        l = l // key
        gamma = l.to_bytes((len(bin(l)) // 8) + 1, byteorder='big')[1:]
        ac += gamma
        with open(outfile, "wb") as handle1:
            handle1.write(ac)
        print('Файл расшифрован.')
        end = datetime.datetime.now()
        time = end - start
        print('Программа закончила выполнение в', str(end))
        print('Программа работала', str(time), 'времени')
        input ("Нажмите для выхода ... ")
def desfile(file):
    errhap = 1
    try:
        with open(file, 'rb') as f0:
                data = f0.readlines()
                b = 0
                for i in data:
                    b += len(list(i))
    except FileNotFoundError:
        print('Ошибка! Файла '+file+'не существует!')
        errhap = 0
    except IsADirectoryError:
        print('Ошибка! '+file+' - это папка')
        errhap = 0
    if errhap != 0:
        for i in range(10):
            with open(file, 'wb') as f1:
                f1.write(os.urandom(b))
        os.remove(file)
def encr(args):
    password = ' '
    infile = ' '
    outfile = ' '
    file2 = ''
    dd = False
    default = False
    default1 = False
    for i in range(len(args)):
        a = args[i]
        if i != (len(args) - 1):
            b = args[i+1]
            if a == '-rp':
                password = ''.join(random.sample(en, 12))
                print('Ваш пароль:', password)
            elif a == '-p':
                password = b
            elif a == '-if':
                infile = b
            elif a == '-of':
                outfile = b
            elif a == '-df':
                outfile = infile + '.holocorn'
                default1 = True
            elif a == '-dd':
                dd = True
            elif a == '-kf':
                file2 = b
                default = True
            elif a == '-dk':
                file2 = infile+'.key'
                default = True
        else:
            if a == '-dd':
                dd = True
            elif a == '-rp':
                password = ''.join(random.sample(en, 12))
                print('Ваш пароль:', password)
            elif a == '-df':
                outfile = infile + '.holocorn'
                default1 = True
            elif a == '-dk':
                file2 = infile+'.key'
                default = True
            elif a == '-rp':
                password = ''.join(random.sample(en, 12))
                print('Ваш пароль:', password)
    if (default == False) and (default1 == True):
        outfile = infile+'.crypt0'
    if outfile != ' ' and infile != ' ' and password != ' ':
        try:
            encfile(infile, outfile, password, file2)
            if dd == True:
                desfile(infile)
        except Exception:
            print('Unknown error')
    else:
        print('Ошибка! Нет значений некоторых параметров!!')
        print("Запускаем GUI...")
        help()
        app = QApplication(sys.argv)
        ex = Holocorn()
        sys.exit(app.exec_())
def decr(args):
    password = ' '
    infile = ' '
    outfile = ' '
    file2 = ''
    dd = False
    default = False
    default1 = False
    for i in range(len(args)):
        a = args[i]
        if i != (len(args) - 1):
            b = args[i+1]
            if a == '-p':
                password = b
            elif a == '-if':
                infile = b
            elif a == '-of':
                outfile = b
            elif a == '-df':
                outfile = infile[:-9]
                default1 = True
            elif a == '-dd':
                dd = True
            elif a == '-kf':
                default = True
                file2 = b
            elif a == '-dk':
                file2 = infile[:-9]+'.key'
                default = True
        else:
            if a == '-dd':
                dd = True
            elif a == '-df':
                outfile = infile[:-9]
                default1 = True
            elif a == '-dk':
                file2 = infile[:-9]+'.key'
                default = True
    if (default == False) and (default1 == True):
        outfile = infile[:-7]
    if outfile != ' ' and infile != ' ' and password != ' ':
        try:
            decfile(infile, outfile, password, file2)
            if dd == True:
                desfile(infile)
                if file2 != '':
                    desfile(file2)
        except Exception:
            print('Unknown error')
    else:
        print('Ошибка! Нет значений некоторых параметров!!')
        print("Запускаем GUI...")
        help()
        app = QApplication(sys.argv)
        ex = Holocorn()
        sys.exit(app.exec_())
if __name__ == '__main__':
    def cui():  #Console User Interface
        arg = sys.argv[1:].copy()
        if arg[0] == '-e' or arg[0] == '-en' or arg[0] == '--encr' or arg[0] == '--encrypt':
            encr(arg[1:])
        elif arg[0] == '-d' or arg[0] == '-de' or arg[0] == '--decr' or arg[0] == '--decrypt':
            decr(arg[1:])
        elif arg[0] == '--help' or arg[0] == '-h':
            print('Справка.')
            help()
        else:
            print('Неправильный первый аргумент!')
            help()
    def errmsg(num, name):
        hexnum1 = hex(num)
        zero = ''
        for i in range(11-len(hexnum1[2:])):
            zero += '0'
        hexnum = hexnum1[:1]+zero+hexnum1[2:]
        print('Error! \nError number: '+hexnum+'. \nError name: '+name+'.')
    try:
        if len(sys.argv) != 1:
            cui()
        else:
            app = QApplication(sys.argv)
            ex = Holocorn()
            sys.exit(app.exec_())
    except StopIteration:
        errmsg(2347009, 'StopIteration error')
    except StopAsyncIteration:
        errmsg(3120597, 'StopAsyncIteration error')
    except ArithmeticError:
        errmsg(709235, 'ArithmeticError error')
    except AssertionError:
        errmsg(102375, 'AssertionError error')
    except AttributeError:
        errmsg(632508, 'AttributeError error')
    except BufferError:
        errmsg(365980, 'BufferError error')
    except EOFError:
        errmsg(921346, 'EOFError error')
    except ImportError:
        errmsg(103856, 'ImportError error')
    except LookupError:
        errmsg(213856, 'LookupError error')
    except MemoryError:
        errmsg(19856, 'MemoryError error')
    except NameError:
        errmsg(2938651, 'NameError error')
    except OSError:
        errmsg(193756, 'OSError error')
    except ReferenceError:
        errmsg(183560, 'ReferenceError error')
    except RuntimeError:
        errmsg(1032856, 'RuntimeError error')
    except SyntaxError:
        errmsg(9238561, 'SyntaxError error')
    except SystemError:
        errmsg(24865, 'SystemError error')
    except TypeError:
        errmsg(357225, 'TypeError error')
    except ValueError:
        errmsg(287345, 'ValueError error')
    except Exception:
        errmsg(11111111, 'Unknown error')
