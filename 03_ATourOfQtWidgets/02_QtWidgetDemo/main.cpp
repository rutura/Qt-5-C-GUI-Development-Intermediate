#include "rockwidget.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    RockWidget w;
    w.setWindowTitle("Rock Widget Here");
    w.show();

    return a.exec();
}
