cmake_minimum_required(VERSION 3.5)

project(7-3PainterAppCopyPaste VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Widgets)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Widgets)

set(PROJECT_SOURCES
        colorlistwidget.cpp
        colorlistwidget.h
        colorpicker.cpp
        colorpicker.h
        doubleclickbutton.cpp
        doubleclickbutton.h
        dragbutton.cpp
        dragbutton.h
        handleitem.cpp
        handleitem.h
        main.cpp
        mainwindow.cpp
        mainwindow.h
        mainwindow.ui
        painterapptypes.h
        resizableellipseitem.cpp
        resizableellipseitem.h
        resizablehandlerect.cpp
        resizablehandlerect.h
        resizablepixmapitem.cpp
        resizablepixmapitem.h
        resizablerectitem.cpp
        resizablerectitem.h
        resizablestaritem.cpp
        resizablestaritem.h
        scene.cpp
        scene.h
        shapelist.cpp
        shapelist.h
        strokeitem.cpp
        strokeitem.h
        view.cpp
        view.h
)

set(PROJECT_RESOURCES
        images/about.png
        images/circle_active.png
        images/circle_cursor.png
        images/circle.png
        images/close.png
        images/copyIcon.png
        images/cursor_active.png
        images/cursor.png
        images/cutIcon.png
        images/ellipse.png
        images/eraser_active.png
        images/eraser_cursor.png
        images/eraser.png
        images/open.png
        images/pasteIcon.png
        images/pen_active.png
        images/pen_cursor.png
        images/pen_cursor1.png
        images/pen_style_dashed.png
        images/pen_style_dot_dashed.png
        images/pen_style_dotted.png
        images/pen_style_solid.png
        images/pen.png
        images/quick.png
        images/rectangle_cursor.png
        images/rectangle.png
        images/rectangle1_active.png
        images/rectangle1.png
        images/redoIcon.png
        images/save.png
        images/star_active.png
        images/star_cursor.png
        images/star.png
        images/undoIcon.png
)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(${PROJECT_NAME}
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}
    )
    qt_add_resources(${PROJECT_NAME} imageresources
        PREFIX /
        FILES ${PROJECT_RESOURCES}
    )
# Define target properties for Android with Qt 6 as:
#    set_property(TARGET ${PROJECT_NAME} APPEND PROPERTY QT_ANDROID_PACKAGE_SOURCE_DIR
#                 ${CMAKE_CURRENT_SOURCE_DIR}/android)
# For more information, see https://doc.qt.io/qt-6/qt-add-executable.html#target-creation
else()
    if(ANDROID)
        add_library(${PROJECT_NAME} SHARED
            ${PROJECT_SOURCES}
            resource.qrc
        )
# Define properties for Android with Qt 5 after find_package() calls as:
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
    else()
        add_executable(${PROJECT_NAME}
            ${PROJECT_SOURCES}
            resource.qrc
        )
    endif()
endif()

target_link_libraries(${PROJECT_NAME} PRIVATE Qt${QT_VERSION_MAJOR}::Widgets)

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
if(${QT_VERSION} VERSION_LESS 6.1.0)
  set(BUNDLE_ID_OPTION MACOSX_BUNDLE_GUI_IDENTIFIER com.learnQt.${PROJECT_NAME})
endif()
set_target_properties(${PROJECT_NAME} PROPERTIES
    ${BUNDLE_ID_OPTION}
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

include(GNUInstallDirs)
install(TARGETS ${PROJECT_NAME}
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

if(QT_VERSION_MAJOR EQUAL 6)
    qt_finalize_executable(${PROJECT_NAME})
endif()

