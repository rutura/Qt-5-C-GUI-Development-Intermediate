#ifndef ROCKWIDGET_H
#define ROCKWIDGET_H

#include <QObject>
#include <QWidget>

class RockWidget : public QWidget
{
    Q_OBJECT
public:
    explicit RockWidget(QWidget *parent = nullptr);
signals:

public slots:

private slots:
    void buttonClicked();
private:
    QSize sizeHint() const;
};

#endif // ROCKWIDGET_H
