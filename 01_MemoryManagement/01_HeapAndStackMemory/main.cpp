/*
 *      Exploring heap and stack memory
 *
 * */


#include <QCoreApplication>
#include <QDebug>
#include "house.h"

void do_stuff(){
    //Stack memory
    /*
    House h1(nullptr,"First");
    h1.print_info();
    */

    //Heap memory
    House* p_h1 = new House(nullptr,"First");
    p_h1->print_info();
    delete p_h1; 
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    qDebug() << "Starting...";
    do_stuff();
    qDebug() << "Ending...";

    return a.exec();
}
