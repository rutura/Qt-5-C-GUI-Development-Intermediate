#include "inventorydelegates.h"
#include <QApplication>
#include <QMouseEvent>
#include <QPainterPath>
#include <QImageReader>

// Image Delegate Implementation
ImageDelegate::ImageDelegate(QObject *parent)
    : QStyledItemDelegate(parent)
{
}

void ImageDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option,
                        const QModelIndex &index) const
{
    QStyledItemDelegate::paint(painter, option, index);
    
    QPixmap pixmap = index.data(Qt::DecorationRole).value<QPixmap>();
    if (!pixmap.isNull()) {
        painter->save();
        
        // Draw selection background if item is selected
        if (option.state & QStyle::State_Selected) {
            painter->fillRect(option.rect, option.palette.highlight());
        }

        // Scale pixmap to fit in the cell while maintaining aspect ratio
        QSize size = option.rect.size();
        size.setHeight(size.height() - 4); // Padding
        size.setWidth(size.width() - 4);
        QPixmap scaled = pixmap.scaled(size, Qt::KeepAspectRatio, Qt::SmoothTransformation);
        
        // Center the pixmap in the cell
        QPoint point(option.rect.x() + (option.rect.width() - scaled.width()) / 2,
                    option.rect.y() + (option.rect.height() - scaled.height()) / 2);
        
        painter->drawPixmap(point, scaled);
        painter->restore();
    }
}

bool ImageDelegate::editorEvent(QEvent *event, QAbstractItemModel *model,
                              const QStyleOptionViewItem &option, const QModelIndex &index)
{
    if (event->type() == QEvent::MouseButtonDblClick) {
        QString fileName = QFileDialog::getOpenFileName(nullptr, 
                                                     tr("Select Image"),
                                                     QString(),
                                                     tr("Images (*.png *.jpg *.jpeg)"));
        if (!fileName.isEmpty()) {
            QPixmap pixmap(fileName);
            if (!pixmap.isNull()) {
                model->setData(index, fileName, Qt::EditRole);
                return true;
            }
        }
    }
    return QStyledItemDelegate::editorEvent(event, model, option, index);
}

QSize ImageDelegate::sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(option);
    Q_UNUSED(index);
    return QSize(100, 100); // Fixed size for image cells
}

// Rating Delegate Implementation
RatingDelegate::RatingDelegate(QObject *parent)
    : QStyledItemDelegate(parent)
{
}

void RatingDelegate::paint(QPainter *painter, const QStyleOptionViewItem &option,
                         const QModelIndex &index) const
{
    QStyledItemDelegate::paint(painter, option, index);

    painter->save();

    // Draw selection background if item is selected
    if (option.state & QStyle::State_Selected) {
        painter->fillRect(option.rect, option.palette.highlight());
    }

    // Get the rating value (1-5)
    int rating = index.data(Qt::DisplayRole).toInt();
    
    // Calculate the total width needed for all stars
    int totalWidth = MaxStars * StarSize;
    int startX = option.rect.x() + (option.rect.width() - totalWidth) / 2;
    int centerY = option.rect.y() + (option.rect.height() - StarSize) / 2;

    // Draw stars
    for (int i = 0; i < MaxStars; ++i) {
        QRect starRect(startX + i * StarSize, centerY, StarSize, StarSize);
        drawStar(painter, starRect, i < rating);
    }

    painter->restore();
}

void RatingDelegate::drawStar(QPainter *painter, const QRect &rect, bool filled) const
{
    // Create star path
    QPainterPath starPath;
    QPolygonF star;
    const qreal radius = rect.width() / 2.0;
    const QPointF center(rect.center());
    
    // Calculate points for a 5-pointed star
    for (int i = 0; i < 5; ++i) {
        qreal angle = -M_PI / 2 + i * 2 * M_PI / 5;
        star << center + QPointF(radius * cos(angle), radius * sin(angle));
        angle += M_PI / 5;
        star << center + QPointF(radius * 0.4 * cos(angle), radius * 0.4 * sin(angle));
    }
    
    starPath.addPolygon(star);
    starPath.closeSubpath();

    // Set up the painter
    painter->setRenderHint(QPainter::Antialiasing);
    QPen pen(Qt::black);
    pen.setWidth(1);
    painter->setPen(pen);

    if (filled) {
        painter->setBrush(QColor(255, 215, 0)); // Gold color for filled stars
    } else {
        painter->setBrush(Qt::white);
    }

    // Draw the star
    painter->drawPath(starPath);
}

bool RatingDelegate::editorEvent(QEvent *event, QAbstractItemModel *model,
                              const QStyleOptionViewItem &option, const QModelIndex &index)
{
    if (event->type() == QEvent::MouseButtonPress) {
        QMouseEvent *mouseEvent = static_cast<QMouseEvent*>(event);
        int star = starAtPosition(mouseEvent->pos(), option);
        if (star != -1) {
            model->setData(index, star, Qt::EditRole);
            return true;
        }
    }
    return QStyledItemDelegate::editorEvent(event, model, option, index);
}

int RatingDelegate::starAtPosition(const QPoint &pos, const QStyleOptionViewItem &option) const
{
    // Calculate the total width of all stars
    int totalWidth = MaxStars * StarSize;
    int startX = option.rect.x() + (option.rect.width() - totalWidth) / 2;
    
    // If click is outside the stars area, return -1
    if (pos.x() < startX || pos.x() > startX + totalWidth) {
        return -1;
    }
    
    // Calculate which star was clicked (1-5)
    int star = ((pos.x() - startX) / StarSize) + 1;
    return qBound(1, star, MaxStars);
}

QSize RatingDelegate::sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_UNUSED(option);
    Q_UNUSED(index);
    return QSize(MaxStars * StarSize + 10, StarSize + 6); // Add some padding
}

// Supplier Delegate Implementation
SupplierDelegate::SupplierDelegate(const QStringList &suppliers, QObject *parent)
    : QStyledItemDelegate(parent), supplierList(suppliers)
{
}

QWidget *SupplierDelegate::createEditor(QWidget *parent,
                                      const QStyleOptionViewItem &option,
                                      const QModelIndex &index) const
{
    Q_UNUSED(option);
    Q_UNUSED(index);
    
    QComboBox *editor = new QComboBox(parent);
    editor->addItems(supplierList);
    editor->setFrame(false);
    return editor;
}

void SupplierDelegate::setEditorData(QWidget *editor, const QModelIndex &index) const
{
    QString currentSupplier = index.data(Qt::EditRole).toString();
    QComboBox *comboBox = static_cast<QComboBox*>(editor);
    
    int idx = comboBox->findText(currentSupplier);
    if (idx >= 0) {
        comboBox->setCurrentIndex(idx);
    }
}

void SupplierDelegate::setModelData(QWidget *editor, QAbstractItemModel *model,
                                  const QModelIndex &index) const
{
    QComboBox *comboBox = static_cast<QComboBox*>(editor);
    model->setData(index, comboBox->currentText(), Qt::EditRole);
}

void SupplierDelegate::updateEditorGeometry(QWidget *editor,
                                          const QStyleOptionViewItem &option,
                                          const QModelIndex &index) const
{
    Q_UNUSED(index);
    editor->setGeometry(option.rect);
}

void SupplierDelegate::setSuppliers(const QStringList &suppliers)
{
    supplierList = suppliers;
}
