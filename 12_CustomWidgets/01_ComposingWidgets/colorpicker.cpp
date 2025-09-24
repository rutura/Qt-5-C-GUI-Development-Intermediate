#include "colorpicker.h"
#include <QPushButton>

ColorPicker::ColorPicker(QWidget *parent)
    : QWidget{parent},
    m_layout{new QGridLayout{this}},
    m_previewLabel{ new QLabel{this}}
{
    populateColors();
    setupUi();

}

QColor ColorPicker::color() const
{
    return m_color;
}

void ColorPicker::setColor(const QColor &newColor)
{
    if (m_color != newColor) {
        m_color = newColor;

        // Change the preview label to show the selected color
        const QString css = QString("background-color: %1").arg(m_color.name());
        m_previewLabel->setStyleSheet(css);
        emit colorChanged(m_color);
    }
}

void ColorPicker::handleColorButtonClicked()
{
    auto* button = qobject_cast<QPushButton*>(sender());
    if(button){
        const int index = button->property("colorIndex").toInt();\
        if (index >= 0 && index < m_colorList.size()) {
            setColor(m_colorList[index]);
        }
    }
}

void ColorPicker::populateColors()
{

    m_colorList = {
        QColor("#FF0000"),  // Red
        QColor("#00FF00"),  // Green
        QColor("#0000FF"),  // Blue
        QColor("#FFFF00"),  // Yellow
        QColor("#FF00FF"),  // Magenta
        QColor("#00FFFF"),  // Cyan
        QColor("#FFA500"),  // Orange
        QColor("#800080"),  // Purple
        QColor("#008000")   // Dark Green
    };
}

void ColorPicker::setupUi()
{
    setLayout(m_layout);

    // Setup preview label
    m_previewLabel->setMinimumSize(200, 50);
    m_previewLabel->setFrameStyle(QFrame::Panel | QFrame::Sunken);
    m_previewLabel->setAlignment(Qt::AlignCenter);
    m_layout->addWidget(m_previewLabel, 0, 0, 1, 3);


    //Create the color buttons
    for ( int i = 0; i < m_colorList.size(); i++){
        auto* button = new QPushButton(this);
        button->setFixedSize(60,60);
        button->setProperty("colorIndex", i);

        const QString css = QString(R"(
            QPushButton {
                background-color: %1;
                border: 2px solid transparent;
                border-radius: 5px;
            }
            QPushButton:hover {
                border: 2px solid white;
                border-radius: 5px;
            }
            QPushButton:pressed {
                border: 3px solid white;
            }
        )").arg(m_colorList[i].name());
        button->setStyleSheet(css);

        connect(button, &QPushButton::clicked, this, &ColorPicker::handleColorButtonClicked);

        m_layout->addWidget(button, (i/3) + 1,i % 3);

    }
}






















