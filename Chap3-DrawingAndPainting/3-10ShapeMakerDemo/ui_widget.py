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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(722, 514)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.canvasLayout = QVBoxLayout()
        self.canvasLayout.setSpacing(6)
        self.canvasLayout.setObjectName(u"canvasLayout")

        self.verticalLayout_2.addLayout(self.canvasLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.shapeCombo = QComboBox(Widget)
        self.shapeCombo.setObjectName(u"shapeCombo")

        self.horizontalLayout.addWidget(self.shapeCombo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.penWidthSpinbox = QSpinBox(Widget)
        self.penWidthSpinbox.setObjectName(u"penWidthSpinbox")

        self.horizontalLayout_2.addWidget(self.penWidthSpinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.penStyleCombobox = QComboBox(Widget)
        self.penStyleCombobox.setObjectName(u"penStyleCombobox")

        self.horizontalLayout_3.addWidget(self.penStyleCombobox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.penCapCombobox = QComboBox(Widget)
        self.penCapCombobox.setObjectName(u"penCapCombobox")

        self.horizontalLayout_4.addWidget(self.penCapCombobox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.penJoinComboBox = QComboBox(Widget)
        self.penJoinComboBox.setObjectName(u"penJoinComboBox")

        self.horizontalLayout_5.addWidget(self.penJoinComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.brushStyleCombobox = QComboBox(Widget)
        self.brushStyleCombobox.setObjectName(u"brushStyleCombobox")

        self.horizontalLayout_6.addWidget(self.brushStyleCombobox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.antiAlisingCheckbox = QCheckBox(Widget)
        self.antiAlisingCheckbox.setObjectName(u"antiAlisingCheckbox")

        self.horizontalLayout_7.addWidget(self.antiAlisingCheckbox)

        self.transformsCheckbox = QCheckBox(Widget)
        self.transformsCheckbox.setObjectName(u"transformsCheckbox")

        self.horizontalLayout_7.addWidget(self.transformsCheckbox)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Shape", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Pen Width", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Pen Style", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Pen Cap", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Pen Join", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Brush Style", None))
        self.antiAlisingCheckbox.setText(QCoreApplication.translate("Widget", u"Antialising", None))
        self.transformsCheckbox.setText(QCoreApplication.translate("Widget", u"Transforms", None))
    # retranslateUi

