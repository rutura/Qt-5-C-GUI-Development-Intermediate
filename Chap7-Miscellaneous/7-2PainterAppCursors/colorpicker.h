#ifndef COLORPICKER_H
#define COLORPICKER_H

#include <QWidget>
#include "doubleclickbutton.h"


class ColorPicker : public QWidget
{
    Q_OBJECT
public:
    explicit ColorPicker(QWidget *parent = nullptr);

signals:
    void colorChanged(QColor newColor);

public slots:
private:
    void populateColors();
    void setButtonColor(DoubleclickButton * button, QColor color);
    void makeConnections(DoubleclickButton * button, int index);



    QVector <QColor> colors;
};

#endif // COLORPICKER_H
