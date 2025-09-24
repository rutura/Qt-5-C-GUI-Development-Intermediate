#include <QCoreApplication>

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QSet<QString> set;
    set.insert("one");
    set.insert("three");
    set.insert("seven");

    qDebug() << set ;
    //Elements are stored in the order decided by QSet
    //More : read the docs


    return a.exec();
}
