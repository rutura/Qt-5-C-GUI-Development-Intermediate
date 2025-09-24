#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QNetworkAccessManager>
namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT
public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();
public slots:
    void dataReadyToRead();
    void dataReadFinished();
private:
    Ui::Widget *ui;
    QNetworkAccessManager * netManager;
    QNetworkReply * netReply;
    QByteArray * mDataBuffer;
};

#endif // WIDGET_H
