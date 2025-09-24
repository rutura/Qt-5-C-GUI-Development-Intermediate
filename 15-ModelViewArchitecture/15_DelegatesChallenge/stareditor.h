#ifndef STAREDITOR_H
#define STAREDITOR_H

#include <QObject>
#include <QWidget>

class StarEditor : public QWidget
{
    Q_OBJECT
public:
    explicit StarEditor(QWidget *parent = nullptr);

signals:

    // QWidget interface
public:
    QSize sizeHint() const override;

    int getStarRating() const;
    void setStarRating(int newStarRating);

signals:
    void editingFinished();


protected:
    void mouseReleaseEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void paintEvent(QPaintEvent *event) override;

private:
    int starRating{3};
    QPolygon poly;
};

#endif // STAREDITOR_H
