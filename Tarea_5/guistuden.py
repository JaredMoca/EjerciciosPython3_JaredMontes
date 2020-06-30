# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI-Stu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(377, 472)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nombre = QLineEdit(self.centralwidget)
        self.nombre.setObjectName(u"nombre")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nombre)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.Email = QLineEdit(self.centralwidget)
        self.Email.setObjectName(u"Email")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Email)

        self.Password = QLineEdit(self.centralwidget)
        self.Password.setObjectName(u"Password")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Password)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Registrar = QPushButton(self.centralwidget)
        self.Registrar.setObjectName(u"Registrar")

        self.horizontalLayout_2.addWidget(self.Registrar)

        self.Buscar = QPushButton(self.centralwidget)
        self.Buscar.setObjectName(u"Buscar")

        self.horizontalLayout_2.addWidget(self.Buscar)

        self.Actualizar = QPushButton(self.centralwidget)
        self.Actualizar.setObjectName(u"Actualizar")

        self.horizontalLayout_2.addWidget(self.Actualizar)

        self.Eliminar = QPushButton(self.centralwidget)
        self.Eliminar.setObjectName(u"Eliminar")

        self.horizontalLayout_2.addWidget(self.Eliminar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.cuadro = QTextEdit(self.centralwidget)
        self.cuadro.setObjectName(u"cuadro")

        self.verticalLayout.addWidget(self.cuadro)

        self.Limpiar = QPushButton(self.centralwidget)
        self.Limpiar.setObjectName(u"Limpiar")

        self.verticalLayout.addWidget(self.Limpiar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 377, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.Buscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.Actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.Eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.Limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar ventana", None))
    # retranslateUi

