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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(811, 561)
        self.horizontalLayout_8 = QHBoxLayout(Widget)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.viewLayout = QVBoxLayout()
        self.viewLayout.setSpacing(6)
        self.viewLayout.setObjectName(u"viewLayout")

        self.horizontalLayout_8.addLayout(self.viewLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.xTranslateSpinbox = QSpinBox(self.groupBox)
        self.xTranslateSpinbox.setObjectName(u"xTranslateSpinbox")
        self.xTranslateSpinbox.setMinimum(-99)

        self.horizontalLayout.addWidget(self.xTranslateSpinbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.yTranslateSpinbox = QSpinBox(self.groupBox)
        self.yTranslateSpinbox.setObjectName(u"yTranslateSpinbox")
        self.yTranslateSpinbox.setMinimum(-99)

        self.horizontalLayout_2.addWidget(self.yTranslateSpinbox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.xScaleSpinbox = QSpinBox(self.groupBox_2)
        self.xScaleSpinbox.setObjectName(u"xScaleSpinbox")
        self.xScaleSpinbox.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.xScaleSpinbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.yScaleSpinbox = QSpinBox(self.groupBox_2)
        self.yScaleSpinbox.setObjectName(u"yScaleSpinbox")
        self.yScaleSpinbox.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.yScaleSpinbox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.xShearSpinbox = QSpinBox(self.groupBox_3)
        self.xShearSpinbox.setObjectName(u"xShearSpinbox")

        self.horizontalLayout_5.addWidget(self.xShearSpinbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.yShearSpinbox = QSpinBox(self.groupBox_3)
        self.yShearSpinbox.setObjectName(u"yShearSpinbox")

        self.horizontalLayout_6.addWidget(self.yShearSpinbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.rotationSpinbox = QSpinBox(self.groupBox_4)
        self.rotationSpinbox.setObjectName(u"rotationSpinbox")

        self.horizontalLayout_7.addWidget(self.rotationSpinbox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Transltate", None))
        self.label.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Y:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Scale", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Y:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Shear", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"X:", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Y:", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"Rotation", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Angle", None))
    # retranslateUi

