#include "expense.h"

Expense::Expense(QObject *parent) : QObject(parent),
    m_date(QDate::currentDate()),
    m_item(""),
    m_amount(0.0),
    m_category("")
{
}

Expense::Expense(const QDate &date, const QString &item, double amount, const QString &category, QObject *parent)
    : QObject(parent),
    m_date(date),
    m_item(item),
    m_amount(amount),
    m_category(category)
{
}

QDate Expense::date() const
{
    return m_date;
}

QString Expense::item() const
{
    return m_item;
}

double Expense::amount() const
{
    return m_amount;
}

QString Expense::category() const
{
    return m_category;
}

void Expense::setDate(const QDate &date)
{
    if (m_date != date) {
        m_date = date;
        emit dateChanged(m_date);
    }
}

void Expense::setItem(const QString &item)
{
    if (m_item != item) {
        m_item = item;
        emit itemChanged(m_item);
    }
}

void Expense::setAmount(double amount)
{
    if (m_amount != amount) {
        m_amount = amount;
        emit amountChanged(m_amount);
    }
}

void Expense::setCategory(const QString &category)
{
    if (m_category != category) {
        m_category = category;
        emit categoryChanged(m_category);
    }
}