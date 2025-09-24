#include "widget.h"
#include "ui_widget.h"
#include <QNetworkRequest>
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>
#include <QVariantMap>
#include <QDebug>

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget),
    mNetManager(new QNetworkAccessManager(this)),
    mNetReply(nullptr),
    mDataBuffer(new QByteArray)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_fetchButton_clicked()
{
    //Initialize our API data
    const QUrl API_ENDPOINT("https://jsonplaceholder.typicode.com/posts");
    QNetworkRequest request;
    request.setUrl(API_ENDPOINT);

    mNetReply = mNetManager->get(request);
    connect(mNetReply,&QIODevice::readyRead,this,&Widget::dataReadyRead);
    connect(mNetReply,&QNetworkReply::finished,this,&Widget::dataReadFinished);
}

void Widget::dataReadyRead()
{
    mDataBuffer->append(mNetReply->readAll());
}

void Widget::dataReadFinished()
{
    if( mNetReply->error())
    {
        qDebug() << "Error : " << mNetReply->errorString();
    }else
    {
       qDebug() << "Data fetch finished : " << QString(*mDataBuffer);

       //Turn the data into a json document
       QJsonDocument doc = QJsonDocument::fromJson(*mDataBuffer);

       /*
       //What if you get an object from the server
       QJsonDocument objectDoc = QJsonDocument::fromJson(*mDataBuffer);
       QJsonObject obObject = objectDoc.toVariant().toJsonObject();
       */

       //Turn document into json array
       QJsonArray array = doc.array();

       for ( int i = 0; i < array.size(); i++)
       {
           QJsonObject object = array.at(i).toObject();
           QVariantMap map = object.toVariantMap();
           QString title = map["title"].toString();
           ui->listWidget->addItem("["+ QString::number(i+1) + "] " + title);

       }
    }
}
