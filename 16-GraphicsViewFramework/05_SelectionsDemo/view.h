#ifndef VIEW_H
#define VIEW_H

#include <QGraphicsView>

class View : public QGraphicsView
{
    Q_OBJECT
public:
    explicit View(QWidget *parent = nullptr);

    enum Tool {
        Cursor,
        Line,
        Ellipse,
        Path,
        Pie,
        Image,
        Star
    };

    Tool getCurrentTool() const;
    void setCurrentTool(const Tool &value);

signals:

public slots:

    // QWidget interface
protected:
    void mousePressEvent(QMouseEvent *event) override;

private:

    void addLine(QPointF pos);
       void addEllipse(QPointF pos);
       void addPath(QPointF pos);
       void addPie(QPointF pos);
       void addImage(QPointF pos);
       void addStar(QPointF pos);

    Tool currentTool;

};

#endif // VIEW_H
