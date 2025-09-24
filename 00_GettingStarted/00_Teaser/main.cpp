#include "widget.h"
/*
 *      . A teaser app just to spice the appetite for the students
 *      . This should be in the intro section of the course after we
 *          have Qt installed
 * */

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Widget w;
    w.show();
    return a.exec();
}
