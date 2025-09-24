/*
 *      . We can also create Qt Console applications
 *      . This allows them to take advantage of the features
 *              of Qt like
 *                  . Networking
 *                  . threading,.....
 *
 * */


#include <QCoreApplication>
//#include <iostream>
#include <QDebug>


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    //std::cout << "Hello world" << std::endl;
    qDebug() << "Hello world";

    return a.exec();
}
