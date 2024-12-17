#ifndef STARDELEGATE_H
#define STARDELEGATE_H

#include <QStyledItemDelegate>

class StarDelegate : public QStyledItemDelegate
{
    Q_OBJECT
public:
    explicit StarDelegate(QObject *parent = nullptr);

    // QAbstractItemDelegate interface
    void paint(QPainter *painter, const QStyleOptionViewItem &option,
               const QModelIndex &index) const override;
    QSize sizeHint(const QStyleOptionViewItem &option,
                   const QModelIndex &index) const override;
    QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option,
                          const QModelIndex &index) const override;
    void setEditorData(QWidget *editor, const QModelIndex &index) const override;
    void setModelData(QWidget *editor, QAbstractItemModel *model,
                      const QModelIndex &index) const override;


private slots:
    void commitAndCloseEditor();

private:
    QPolygon poly;
};

#endif // STARDELEGATE_H
