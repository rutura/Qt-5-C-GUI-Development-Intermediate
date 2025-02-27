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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(807, 609)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.viewLayout = QVBoxLayout()
        self.viewLayout.setSpacing(6)
        self.viewLayout.setObjectName(u"viewLayout")

        self.horizontalLayout.addLayout(self.viewLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centerInViewButton = QPushButton(Widget)
        self.centerInViewButton.setObjectName(u"centerInViewButton")

        self.verticalLayout.addWidget(self.centerInViewButton)

        self.showGridCheckbox = QCheckBox(Widget)
        self.showGridCheckbox.setObjectName(u"showGridCheckbox")

        self.verticalLayout.addWidget(self.showGridCheckbox)

        self.ensureVisibleButton = QPushButton(Widget)
        self.ensureVisibleButton.setObjectName(u"ensureVisibleButton")

        self.verticalLayout.addWidget(self.ensureVisibleButton)

        self.fitInViewButton = QPushButton(Widget)
        self.fitInViewButton.setObjectName(u"fitInViewButton")

        self.verticalLayout.addWidget(self.fitInViewButton)

        self.zoomInButton = QPushButton(Widget)
        self.zoomInButton.setObjectName(u"zoomInButton")

        self.verticalLayout.addWidget(self.zoomInButton)

        self.zoomOutButton = QPushButton(Widget)
        self.zoomOutButton.setObjectName(u"zoomOutButton")

        self.verticalLayout.addWidget(self.zoomOutButton)

        self.resetButton = QPushButton(Widget)
        self.resetButton.setObjectName(u"resetButton")

        self.verticalLayout.addWidget(self.resetButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.centerInViewButton.setText(QCoreApplication.translate("Widget", u"Center View", None))
        self.showGridCheckbox.setText(QCoreApplication.translate("Widget", u"Show Grid", None))
        self.ensureVisibleButton.setText(QCoreApplication.translate("Widget", u"Ensure Visible", None))
        self.fitInViewButton.setText(QCoreApplication.translate("Widget", u"Fit in View", None))
        self.zoomInButton.setText(QCoreApplication.translate("Widget", u"Zoom in (+)", None))
        self.zoomOutButton.setText(QCoreApplication.translate("Widget", u"Zoom out(-)", None))
        self.resetButton.setText(QCoreApplication.translate("Widget", u"Reset", None))
    # retranslateUi

