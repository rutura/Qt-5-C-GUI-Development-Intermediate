#ifndef VIEW_H
#define VIEW_H

#include <QGraphicsView>
#include <QGraphicsRectItem>

class View : public QGraphicsView
{
    Q_OBJECT
public:
    explicit View(QWidget *parent = nullptr);

    bool getDrawGridLines() const;
    void setDrawGridLines(bool value);

signals:

public slots:

    // QWidget interface
protected:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;

    void drawBackground(QPainter *painter, const QRectF &rect) override;
    void drawForeground(QPainter *painter, const QRectF &rect) override;

private:
    QPoint selectTopLeft;
    bool drawingSelection;
    QGraphicsRectItem * lastRect;
    bool drawGridLines;


};

#endif // VIEW_H
