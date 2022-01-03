#include "application.h"
#include <QDebug>
#include "widget.h"

Application::Application(int &argc, char **argv) : QApplication(argc,argv)
{

}

bool Application::notify(QObject * dest, QEvent * event)
{
    if ( event->type() == QEvent::MouseButtonPress
         || event->type() == QEvent::MouseButtonDblClick){
        qDebug() << " Application : mouse press or double click detected";

        qDebug() << "Class Name : " << dest->metaObject()->className();

        Widget * button  = dynamic_cast<Widget* >(dest);
        if( button){
            qDebug() << "Cast successful";
        }else {
            qDebug() << "Cast failed";
        }

        return false;
    }
    return QApplication::notify(dest,event);
}
