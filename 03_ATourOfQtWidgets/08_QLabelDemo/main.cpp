/*
 *      The resource file should also be added as a source file
 *          . See the PROJECT_SOURCES CMake variable in your CMakeLists.txt file
 *
 * */

#include "widget.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Widget w;
    w.show();

    return a.exec();
}
