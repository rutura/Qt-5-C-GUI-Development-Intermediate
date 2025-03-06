# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(608, 456)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineButton = QPushButton(Widget)
        self.lineButton.setObjectName(u"lineButton")

        self.verticalLayout_2.addWidget(self.lineButton)

        self.ellipseButton = QPushButton(Widget)
        self.ellipseButton.setObjectName(u"ellipseButton")

        self.verticalLayout_2.addWidget(self.ellipseButton)

        self.pathButton = QPushButton(Widget)
        self.pathButton.setObjectName(u"pathButton")

        self.verticalLayout_2.addWidget(self.pathButton)

        self.pieButton = QPushButton(Widget)
        self.pieButton.setObjectName(u"pieButton")

        self.verticalLayout_2.addWidget(self.pieButton)

        self.imageButton = QPushButton(Widget)
        self.imageButton.setObjectName(u"imageButton")

        self.verticalLayout_2.addWidget(self.imageButton)

        self.starButton = QPushButton(Widget)
        self.starButton.setObjectName(u"starButton")

        self.verticalLayout_2.addWidget(self.starButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.lineButton.setText(QCoreApplication.translate("Widget", u"Line", None))
        self.ellipseButton.setText(QCoreApplication.translate("Widget", u"Ellipse", None))
        self.pathButton.setText(QCoreApplication.translate("Widget", u"Path", None))
        self.pieButton.setText(QCoreApplication.translate("Widget", u"Pie", None))
        self.imageButton.setText(QCoreApplication.translate("Widget", u"Image", None))
        self.starButton.setText(QCoreApplication.translate("Widget", u"Star", None))
    # retranslateUi

