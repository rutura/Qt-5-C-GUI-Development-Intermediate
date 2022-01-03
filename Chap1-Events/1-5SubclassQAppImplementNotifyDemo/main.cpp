#include "widget.h"
#include "application.h"

int main(int argc, char *argv[])
{
    Application a(argc, argv);
    Widget w;
    w.show();

    return a.exec();
}
