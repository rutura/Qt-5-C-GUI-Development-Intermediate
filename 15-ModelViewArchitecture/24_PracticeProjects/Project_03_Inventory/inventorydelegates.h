#ifndef INVENTORYDELEGATES_H
#define INVENTORYDELEGATES_H

#include <QStyledItemDelegate>
#include <QPainter>
#include <QFileDialog>
#include <QEvent>
#include <QMouseEvent>
#include <QComboBox>

// Image Delegate
class ImageDelegate : public QStyledItemDelegate {
    Q_OBJECT
public:
    explicit ImageDelegate(QObject *parent = nullptr);

    void paint(QPainter *painter, const QStyleOptionViewItem &option,
               const QModelIndex &index) const override;
    bool editorEvent(QEvent *event, QAbstractItemModel *model,
                    const QStyleOptionViewItem &option, const QModelIndex &index) override;
    QSize sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const override;
};

// Rating Delegate - Improved star visualization
class RatingDelegate : public QStyledItemDelegate {
    Q_OBJECT
public:
    explicit RatingDelegate(QObject *parent = nullptr);

    void paint(QPainter *painter, const QStyleOptionViewItem &option,
               const QModelIndex &index) const override;
    bool editorEvent(QEvent *event, QAbstractItemModel *model,
                    const QStyleOptionViewItem &option, const QModelIndex &index) override;
    QSize sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const override;

private:
    void drawStar(QPainter *painter, const QRect &rect, bool filled) const;
    int starAtPosition(const QPoint &pos, const QStyleOptionViewItem &option) const;
    static constexpr int MaxStars = 5;
    static constexpr int StarSize = 20;
};

// Supplier Delegate for ComboBox selection
class SupplierDelegate : public QStyledItemDelegate {
    Q_OBJECT
public:
    explicit SupplierDelegate(const QStringList &suppliers, QObject *parent = nullptr);

    QWidget *createEditor(QWidget *parent, const QStyleOptionViewItem &option,
                         const QModelIndex &index) const override;
    void setEditorData(QWidget *editor, const QModelIndex &index) const override;
    void setModelData(QWidget *editor, QAbstractItemModel *model,
                     const QModelIndex &index) const override;
    void updateEditorGeometry(QWidget *editor, const QStyleOptionViewItem &option,
                            const QModelIndex &index) const override;

    void setSuppliers(const QStringList &suppliers);

private:
    QStringList supplierList;
};

#endif // INVENTORYDELEGATES_H
