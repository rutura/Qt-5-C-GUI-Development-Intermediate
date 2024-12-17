#ifndef STAREDITOR_H
#define STAREDITOR_H

#include <QWidget>

class StarEditor : public QWidget
{
    Q_OBJECT
public:
    explicit StarEditor(QWidget *parent = nullptr);


    QSize sizeHint() const override;

    int getStarRating() const;
    void setStarRating(int value);

signals:
    void editingFinished();

public slots:

    // QWidget interface
protected:
    void mouseReleaseEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void paintEvent(QPaintEvent *event) override;

private:
    int starRating;
    QPolygon poly;

};

#endif // STAREDITOR_H
