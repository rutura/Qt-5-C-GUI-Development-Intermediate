#ifndef SCENE_H
#define SCENE_H

#include <QGraphicsScene>

class Scene : public QGraphicsScene
{
    Q_OBJECT
public:
    enum ToolType {
           Cursor,
           Pen,
           Rect,
           Ellipse,
           Star,
           QtQuick,
           Eraser
       };
    explicit Scene(QObject *parent = nullptr);

    ToolType getTool() const;
    void setTool(const ToolType &value);

    void addImageItem(const QString & path);

    QColor getPenColor() const;
    void setPenColor(const QColor &value);

    int getPenWidth() const;
    void setPenWidth(int value);

    Qt::PenStyle getPenStyle() const;
    void setPenStyle(const Qt::PenStyle &value);

    QColor getFillColor() const;
    void setFillColor(const QColor &value);

    Qt::BrushStyle getBrushStyle() const;
    void setBrushStyle(const Qt::BrushStyle &value);

signals:

public slots:

    // QGraphicsScene interface
protected:
    void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override;
    void dropEvent(QGraphicsSceneDragDropEvent *event) override;

    // QGraphicsScene interface
protected:
    void mousePressEvent(QGraphicsSceneMouseEvent *event) override;
    void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override;
    void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override;
    void keyPressEvent(QKeyEvent *event) override;

private:

    void drawLineTo(const QPointF &endPoint);
    void drawEraserAt(const QPointF & endPoint);
    void eraseStrokesUnder(QGraphicsEllipseItem * item);
    void drawShapeTo(const QPointF & endPoint);

    ToolType tool;
    bool drawing;
    QGraphicsItemGroup * lineGroup;
    QPointF startingPoint;
    QPointF lastPenPoint;
    QGraphicsEllipseItem * lastEraserCircle;
    QGraphicsItem * lastItem;

    QGraphicsLineItem * horGuideLine;
    QGraphicsLineItem * verGuideLine;

    QColor penColor;
    int penWidth;
    Qt::PenStyle penStyle;
    QColor fillColor;
    Qt::BrushStyle brushStyle;

};

#endif // SCENE_H
