#ifndef COLORLISTWIDGET_H
#define COLORLISTWIDGET_H

#include <QListWidget>

class ColorListWidget : public QListWidget
{
    Q_OBJECT
public:
    explicit ColorListWidget(QWidget *parent = nullptr);

signals:

public slots:

    // QAbstractItemView interface
protected:
    void startDrag(Qt::DropActions supportedActions) override;
};

#endif // COLORLISTWIDGET_H
