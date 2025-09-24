#ifndef COLORPICKER_H
#define COLORPICKER_H

#include <QObject>
#include <QColor>
#include <QLabel>
#include <QGridLayout>
#include <vector>
#include <QWidget>

class ColorPicker : public QWidget
{
    Q_OBJECT
public:
    explicit ColorPicker(QWidget *parent = nullptr);

    QColor color() const;
    void setColor(const QColor &newColor);

signals:
    void colorChanged(QColor newColor);

private slots:
    void handleColorButtonClicked();
private:
    void populateColors();
    void setupUi();

    QColor m_color;
    std::vector<QColor> m_colorList;
    QGridLayout* m_layout{nullptr};
    QLabel * m_previewLabel{nullptr};

};

#endif // COLORPICKER_H
