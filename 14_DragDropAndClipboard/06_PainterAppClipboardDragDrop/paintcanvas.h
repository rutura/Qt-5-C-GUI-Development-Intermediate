#ifndef PAINTCANVAS_H
#define PAINTCANVAS_H

#include <QWidget>

class PaintCanvas : public QWidget
{
    Q_OBJECT
public:
    enum class ToolType {Pen, Rect, Ellipse, Eraser};
    explicit PaintCanvas(QWidget *parent = nullptr);

    ToolType getTool() const;
    void setTool(ToolType newTool);

    bool getFill() const;
    void setFill(bool newFill);

    int getPenWidth() const;
    void setPenWidth(int newPenWidth);

    QColor getPenColor() const;
    void setPenColor(const QColor &newPenColor);

    QColor getFillColor() const;
    void setFillColor(const QColor &newFillColor);


private:
    void drawLineTo(const QPoint& endPoint);
    void drawRectTo(const QPoint& endPoint, bool ellipse = false);
    void eraseUnder(const QPoint& topLeft);
    void resizeImage(QImage *image, const QSize &newSize);


signals:


private:
    bool isImage(const QString& fullpath) const;
    void copy();
    void paste();

private:
    ToolType tool{ToolType::Ellipse};
    bool fill{true};
    bool drawing{false};
    int penWidth{3};
    QColor fillColor{Qt::red};
    QColor penColor{Qt::green};
    QPoint lastPoint{};
    QRectF lastRect{};
    QRectF lastEraserRect{};
    QImage image{};


    // QWidget interface
protected:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void paintEvent(QPaintEvent *event) override;
    void resizeEvent(QResizeEvent *event) override;

    void dragEnterEvent(QDragEnterEvent *event) override;
    void dropEvent(QDropEvent *event) override;

    void keyPressEvent(QKeyEvent *event) override;
};

#endif // PAINTCANVAS_H
