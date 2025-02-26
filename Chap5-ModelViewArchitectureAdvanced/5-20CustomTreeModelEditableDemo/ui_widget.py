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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTreeView, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(639, 401)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeView = QTreeView(Widget)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout.addWidget(self.treeView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.addRowButton = QPushButton(Widget)
        self.addRowButton.setObjectName(u"addRowButton")

        self.horizontalLayout.addWidget(self.addRowButton)

        self.removeRowButton = QPushButton(Widget)
        self.removeRowButton.setObjectName(u"removeRowButton")

        self.horizontalLayout.addWidget(self.removeRowButton)

        self.addColumnButton = QPushButton(Widget)
        self.addColumnButton.setObjectName(u"addColumnButton")

        self.horizontalLayout.addWidget(self.addColumnButton)

        self.removeColumnButton = QPushButton(Widget)
        self.removeColumnButton.setObjectName(u"removeColumnButton")

        self.horizontalLayout.addWidget(self.removeColumnButton)

        self.addChildButton = QPushButton(Widget)
        self.addChildButton.setObjectName(u"addChildButton")

        self.horizontalLayout.addWidget(self.addChildButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.addRowButton.setText(QCoreApplication.translate("Widget", u"Add Row", None))
        self.removeRowButton.setText(QCoreApplication.translate("Widget", u"Remove Row", None))
        self.addColumnButton.setText(QCoreApplication.translate("Widget", u"Add Column", None))
        self.removeColumnButton.setText(QCoreApplication.translate("Widget", u"Remove Column", None))
        self.addChildButton.setText(QCoreApplication.translate("Widget", u"Add Child", None))
    # retranslateUi

