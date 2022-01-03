#ifndef SHAPELIST_H
#define SHAPELIST_H

#include <QListWidget>

class ShapeList : public QListWidget
{
    Q_OBJECT
public:
    explicit ShapeList(QWidget *parent = nullptr);

signals:

public slots:

    // QAbstractItemView interface
protected:
    void startDrag(Qt::DropActions supportedActions) override;
};

#endif // SHAPELIST_H
