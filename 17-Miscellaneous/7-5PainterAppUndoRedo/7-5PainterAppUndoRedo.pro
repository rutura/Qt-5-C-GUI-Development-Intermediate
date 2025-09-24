#-------------------------------------------------
#
# Project created by QtCreator 2019-07-15T13:47:44
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = 7-5PainterAppUndoRedo
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

CONFIG += c++11

SOURCES += \
        colorlistwidget.cpp \
        colorpicker.cpp \
        commands.cpp \
        doubleclickbutton.cpp \
        dragbutton.cpp \
        handleitem.cpp \
        main.cpp \
        mainwindow.cpp \
        resizableellipseitem.cpp \
        resizablehandlerect.cpp \
        resizablepixmapitem.cpp \
        resizablerectitem.cpp \
        resizablestaritem.cpp \
        scene.cpp \
        shapelist.cpp \
        strokeitem.cpp \
        view.cpp

HEADERS += \
        colorlistwidget.h \
        colorpicker.h \
        commands.h \
        doubleclickbutton.h \
        dragbutton.h \
        handleitem.h \
        mainwindow.h \
        painterapptypes.h \
        resizableellipseitem.h \
        resizablehandlerect.h \
        resizablepixmapitem.h \
        resizablerectitem.h \
        resizablestaritem.h \
        scene.h \
        shapelist.h \
        strokeitem.h \
        view.h

FORMS += \
        mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    resource.qrc
