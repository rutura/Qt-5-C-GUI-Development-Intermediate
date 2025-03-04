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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QToolBar, QVBoxLayout, QWidget)

from dragbutton import DragButton
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(966, 704)
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
        icon4.addFile(u":/images/circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionEllipse.setIcon(icon4)
        self.actionRectangle = QAction(MainWindow)
        self.actionRectangle.setObjectName(u"actionRectangle")
        icon5 = QIcon()
        icon5.addFile(u":/images/rectangle1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon9 = QIcon()
        icon9.addFile(u":/images/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSave.setIcon(icon9)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        self.actionLoad.setIcon(icon)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon10 = QIcon()
        icon10.addFile(u":/images/copyIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCopy.setIcon(icon10)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon11 = QIcon()
        icon11.addFile(u":/images/cutIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCut.setIcon(icon11)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon12 = QIcon()
        icon12.addFile(u":/images/pasteIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPaste.setIcon(icon12)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon13 = QIcon()
        icon13.addFile(u":/images/undoIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionUndo.setIcon(icon13)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon14 = QIcon()
        icon14.addFile(u":/images/redoIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRedo.setIcon(icon14)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.listLayout = QVBoxLayout()
        self.listLayout.setSpacing(6)
        self.listLayout.setObjectName(u"listLayout")
        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.penColorButton = QPushButton(self.groupBox)
        self.penColorButton.setObjectName(u"penColorButton")

        self.horizontalLayout_3.addWidget(self.penColorButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.colorPickerLayout = QVBoxLayout()
        self.colorPickerLayout.setSpacing(6)
        self.colorPickerLayout.setObjectName(u"colorPickerLayout")

        self.verticalLayout.addLayout(self.colorPickerLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.penWidthSpinbox = QSpinBox(self.groupBox)
        self.penWidthSpinbox.setObjectName(u"penWidthSpinbox")
        self.penWidthSpinbox.setMinimum(2)
        self.penWidthSpinbox.setMaximum(12)

        self.horizontalLayout_2.addWidget(self.penWidthSpinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.penStyleCombobox = QComboBox(self.groupBox)
        self.penStyleCombobox.setObjectName(u"penStyleCombobox")

        self.horizontalLayout.addWidget(self.penStyleCombobox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.listLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.brushColorButton = DragButton(self.groupBox_2)
        self.brushColorButton.setObjectName(u"brushColorButton")

        self.horizontalLayout_4.addWidget(self.brushColorButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.brushStyleComboBox = QComboBox(self.groupBox_2)
        self.brushStyleComboBox.setObjectName(u"brushStyleComboBox")

        self.horizontalLayout_5.addWidget(self.brushStyleComboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.showgridCheckbox = QCheckBox(self.groupBox_3)
        self.showgridCheckbox.setObjectName(u"showgridCheckbox")

        self.verticalLayout_3.addWidget(self.showgridCheckbox)

        self.centerSceneButton = QPushButton(self.groupBox_3)
        self.centerSceneButton.setObjectName(u"centerSceneButton")

        self.verticalLayout_3.addWidget(self.centerSceneButton)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.sceneBackgroundButton = QPushButton(self.groupBox_3)
        self.sceneBackgroundButton.setObjectName(u"sceneBackgroundButton")

        self.horizontalLayout_6.addWidget(self.sceneBackgroundButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.listLayout.addWidget(self.groupBox_2)


        self.horizontalLayout_7.addLayout(self.listLayout)

        self.viewLayout = QVBoxLayout()
        self.viewLayout.setSpacing(6)
        self.viewLayout.setObjectName(u"viewLayout")

        self.horizontalLayout_7.addLayout(self.viewLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 966, 26))
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
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuTools.addAction(self.actionCursor)
        self.menuTools.addAction(self.actionPen)
        self.menuTools.addAction(self.actionEraser)
        self.menuTools.addAction(self.actionEllipse)
        self.menuTools.addAction(self.actionRectangle)
        self.menuTools.addAction(self.actionStar)
        self.menuHelp.addAction(self.actionAbout)
        self.mainToolBar.addAction(self.actionSave)
        self.mainToolBar.addAction(self.actionLoad)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionCopy)
        self.mainToolBar.addAction(self.actionPaste)
        self.mainToolBar.addAction(self.actionCut)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionCursor)
        self.mainToolBar.addAction(self.actionPen)
        self.mainToolBar.addAction(self.actionEraser)
        self.mainToolBar.addAction(self.actionEllipse)
        self.mainToolBar.addAction(self.actionStar)
        self.mainToolBar.addAction(self.actionRectangle)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionUndo)
        self.mainToolBar.addAction(self.actionRedo)

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
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Pen Properties", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pen Color", None))
        self.penColorButton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pen Width : ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pen Style : ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Brush Properties", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Brush Color : ", None))
        self.brushColorButton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Brush Style : ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Canvas Properties", None))
        self.showgridCheckbox.setText(QCoreApplication.translate("MainWindow", u"Show Grid", None))
        self.centerSceneButton.setText(QCoreApplication.translate("MainWindow", u"Center Scene", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Scene Background : ", None))
        self.sceneBackgroundButton.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

