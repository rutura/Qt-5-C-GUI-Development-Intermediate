#include "house.h"
#include <QDebug>

House::House(QObject *parent, const QString& descr)
    : QObject{parent} , m_descr(descr)
{
    qDebug() << "House object" << m_descr <<" constructed";
}

House::~House()
{
    qDebug() << "House object" << m_descr <<" destroyed";
}

void House::print_info()
{
    qDebug() << "House : " << m_descr;
}
