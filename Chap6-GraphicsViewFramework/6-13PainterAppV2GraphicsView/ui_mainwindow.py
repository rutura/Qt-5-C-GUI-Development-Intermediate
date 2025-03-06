# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 600)
        self.actionAdd_Image = QAction(MainWindow)
        self.actionAdd_Image.setObjectName(u"actionAdd_Image")
        icon = QIcon()
        icon.addFile(u":/images/open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAdd_Image.setIcon(icon)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon1 = QIcon()
        icon1.addFile(u":/images/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionQuit.setIcon(icon1)
        self.actionPen = QAction(MainWindow)
        self.actionPen.setObjectName(u"actionPen")
        icon2 = QIcon()
        icon2.addFile(u":/images/pen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPen.setIcon(icon2)
        self.actionEraser = QAction(MainWindow)
        self.actionEraser.setObjectName(u"actionEraser")
        icon3 = QIcon()
        icon3.addFile(u":/images/eraser.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionEraser.setIcon(icon3)
        self.actionEllipse = QAction(MainWindow)
        self.actionEllipse.setObjectName(u"actionEllipse")
        icon4 = QIcon()
        icon4.addFile(u":/images/ellipse.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionEllipse.setIcon(icon4)
        self.actionRectangle = QAction(MainWindow)
        self.actionRectangle.setObjectName(u"actionRectangle")
        icon5 = QIcon()
        icon5.addFile(u":/images/rectangle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRectangle.setIcon(icon5)
        self.actionStar = QAction(MainWindow)
        self.actionStar.setObjectName(u"actionStar")
        icon6 = QIcon()
        icon6.addFile(u":/images/star.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionStar.setIcon(icon6)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon7 = QIcon()
        icon7.addFile(u":/images/about.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon7)
        self.actionCursor = QAction(MainWindow)
        self.actionCursor.setObjectName(u"actionCursor")
        icon8 = QIcon()
        icon8.addFile(u":/images/cursor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCursor.setIcon(icon8)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listLayout = QVBoxLayout()
        self.listLayout.setSpacing(6)
        self.listLayout.setObjectName(u"listLayout")

        self.horizontalLayout.addLayout(self.listLayout)

        self.viewLayout = QVBoxLayout()
        self.viewLayout.setSpacing(6)
        self.viewLayout.setObjectName(u"viewLayout")

        self.horizontalLayout.addLayout(self.viewLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 825, 26))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionAdd_Image)
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionCursor)
        self.menuTools.addAction(self.actionPen)
        self.menuTools.addAction(self.actionEraser)
        self.menuTools.addAction(self.actionEllipse)
        self.menuTools.addAction(self.actionRectangle)
        self.menuTools.addAction(self.actionStar)
        self.menuHelp.addAction(self.actionAbout)
        self.mainToolBar.addAction(self.actionCursor)
        self.mainToolBar.addAction(self.actionPen)
        self.mainToolBar.addAction(self.actionEraser)
        self.mainToolBar.addAction(self.actionEllipse)
        self.mainToolBar.addAction(self.actionStar)
        self.mainToolBar.addAction(self.actionRectangle)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAdd_Image.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionPen.setText(QCoreApplication.translate("MainWindow", u"Pen", None))
        self.actionEraser.setText(QCoreApplication.translate("MainWindow", u"Eraser", None))
        self.actionEllipse.setText(QCoreApplication.translate("MainWindow", u"Ellipse", None))
        self.actionRectangle.setText(QCoreApplication.translate("MainWindow", u"Rectangle", None))
        self.actionStar.setText(QCoreApplication.translate("MainWindow", u"Star", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionCursor.setText(QCoreApplication.translate("MainWindow", u"Cursor", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

