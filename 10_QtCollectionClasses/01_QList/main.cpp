/*
 *  QList and QVector are the same in Qt 6
 *
 * */

#include <QCoreApplication>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QList<int> integerList;
    integerList << 1 << 2 << 3 << 4;
    qDebug() << "integers : " << integerList;


    QList<QString> stringList;
    stringList << "The" << " sky " << " is " << " blue.";
    qDebug() << "strings : " << stringList;
    QStringList otherList;
    otherList << " my " << " friend!";
    stringList.append(otherList);
    qDebug() << "strings : " << stringList;

    //Just show the doc for the rest
    //Be careful when removing stuff and know whether the memory was
    // released or not

    return a.exec();
}
