/*
 *      . Show the user interface
 *          . modes (welcome, edit, design, debug, projects, help)
 *                  stress the importance of the built in doc
 *          . Modes :
 *              . debug , release, ...
 *          . Status bar stuff
 *
 *      . Come up with other ideas when making the slides
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
