#ifndef DRAGDROPLABEL_H
#define DRAGDROPLABEL_H

#include <QLabel>
#include <QMimeData>

class DragDropLabel : public QLabel
{
    Q_OBJECT
public:
    explicit DragDropLabel(QWidget *parent = nullptr);

signals:
    void mimeChanged(const QMimeData *mimeData = nullptr);

public slots:

    // QWidget interface
protected:
    void dragEnterEvent(QDragEnterEvent *event) override;
    void dragMoveEvent(QDragMoveEvent *event) override;
    void dragLeaveEvent(QDragLeaveEvent *event) override;
    void dropEvent(QDropEvent *event) override;

private:
    void clear();
};

#endif // DRAGDROPLABEL_H
