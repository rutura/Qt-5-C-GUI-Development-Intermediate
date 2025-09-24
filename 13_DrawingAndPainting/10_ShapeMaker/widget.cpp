#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
    , canvas( new ShapeCanvas(this))
{
    ui->setupUi(this);

    //Add data into the ui components

    // Shape
    ui->shapeCombo->addItem(tr("Polygon"), static_cast<int>(ShapeCanvas::Shape::Polygon));
    ui->shapeCombo->addItem(tr("Rectangle"), static_cast<int>(ShapeCanvas::Shape::Rect));
    ui->shapeCombo->addItem(tr("Rounded Rectangle"), static_cast<int>(ShapeCanvas::Shape::RoundedRect));
    ui->shapeCombo->addItem(tr("Ellipse"), static_cast<int>(ShapeCanvas::Shape::Ellipse));
    ui->shapeCombo->addItem(tr("Pie"), static_cast<int>(ShapeCanvas::Shape::Pie));
    ui->shapeCombo->addItem(tr("Chord"), static_cast<int>(ShapeCanvas::Shape::Chord));
    ui->shapeCombo->addItem(tr("Text"), static_cast<int>(ShapeCanvas::Shape::Text));
    ui->shapeCombo->addItem(tr("Pixmap"), static_cast<int>(ShapeCanvas::Shape::Pixmap));

    // Pen style
    ui->penStyleCombobox->addItem(tr("Solid"), static_cast<int>(Qt::SolidLine));
    ui->penStyleCombobox->addItem(tr("Dash"), static_cast<int>(Qt::DashLine));
    ui->penStyleCombobox->addItem(tr("Dot"), static_cast<int>(Qt::DotLine));
    ui->penStyleCombobox->addItem(tr("Dash Dot"), static_cast<int>(Qt::DashDotLine));
    ui->penStyleCombobox->addItem(tr("Dash Dot Dot"), static_cast<int>(Qt::DashDotDotLine));
    ui->penStyleCombobox->addItem(tr("None"), static_cast<int>(Qt::NoPen));

    // Pen cap
    ui->penCapCombobox->addItem(tr("Flat"), Qt::FlatCap);
    ui->penCapCombobox->addItem(tr("Square"), Qt::SquareCap);
    ui->penCapCombobox->addItem(tr("Round"), Qt::RoundCap);

    // Pen join
    ui->penJoinComboBox->addItem(tr("Miter"), Qt::MiterJoin);
    ui->penJoinComboBox->addItem(tr("Bevel"), Qt::BevelJoin);
    ui->penJoinComboBox->addItem(tr("Round"), Qt::RoundJoin);

    // Brush styles
    ui->brushStyleCombobox->addItem(tr("Linear Gradient"), static_cast<int>(Qt::LinearGradientPattern));
    ui->brushStyleCombobox->addItem(tr("Radial Gradient"), static_cast<int>(Qt::RadialGradientPattern));
    ui->brushStyleCombobox->addItem(tr("Conical Gradient"), static_cast<int>(Qt::ConicalGradientPattern));
    ui->brushStyleCombobox->addItem(tr("Texture"), static_cast<int>(Qt::TexturePattern));
    ui->brushStyleCombobox->addItem(tr("Solid"), static_cast<int>(Qt::SolidPattern));
    ui->brushStyleCombobox->addItem(tr("Horizontal"), static_cast<int>(Qt::HorPattern));
    ui->brushStyleCombobox->addItem(tr("Vertical"), static_cast<int>(Qt::VerPattern));
    ui->brushStyleCombobox->addItem(tr("Cross"), static_cast<int>(Qt::CrossPattern));
    ui->brushStyleCombobox->addItem(tr("Backward Diagonal"), static_cast<int>(Qt::BDiagPattern));
    ui->brushStyleCombobox->addItem(tr("Forward Diagonal"), static_cast<int>(Qt::FDiagPattern));
    ui->brushStyleCombobox->addItem(tr("Diagonal Cross"), static_cast<int>(Qt::DiagCrossPattern));
    ui->brushStyleCombobox->addItem(tr("Dense 1"), static_cast<int>(Qt::Dense1Pattern));
    ui->brushStyleCombobox->addItem(tr("Dense 2"), static_cast<int>(Qt::Dense2Pattern));
    ui->brushStyleCombobox->addItem(tr("Dense 3"), static_cast<int>(Qt::Dense3Pattern));
    ui->brushStyleCombobox->addItem(tr("Dense 4"), static_cast<int>(Qt::Dense4Pattern));
    ui->brushStyleCombobox->addItem(tr("Dense 5"), static_cast<int>(Qt::Dense5Pattern));
    ui->brushStyleCombobox->addItem(tr("Dense 6"), static_cast<int>(Qt::Dense6Pattern));
    ui->brushStyleCombobox->addItem(tr("Dense 7"), static_cast<int>(Qt::Dense7Pattern));
    ui->brushStyleCombobox->addItem(tr("None"), static_cast<int>(Qt::NoBrush));


    //Add the canvas to the layout
    ui->canvasLayout->addWidget(canvas);

    penChanged();
    brushChanged();
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_shapeCombo_activated(int index)
{
    canvas->setShape(static_cast<ShapeCanvas::Shape>(index));
}


void Widget::on_penWidthSpinbox_valueChanged(int arg1)
{
    penChanged();
}


void Widget::on_penStyleCombobox_activated(int index)
{
    penChanged();
}


void Widget::on_penCapCombobox_activated(int index)
{
    penChanged();
}


void Widget::on_penJoinComboBox_activated(int index)
{
    penChanged();
}


void Widget::on_brushStyleCombobox_activated(int index)
{
    brushChanged();
}


void Widget::on_antiAlisingCheckbox_toggled(bool checked)
{
    canvas->setAntialiased(checked);
}


void Widget::on_transformsCheckbox_toggled(bool checked)
{
    canvas->setTransformed(checked);
}

void Widget::penChanged()
{
    const int penWidth = ui->penWidthSpinbox->value();
    const Qt::PenStyle style = static_cast<Qt::PenStyle>(ui->penStyleCombobox->currentData().toInt());
    const Qt::PenCapStyle cap = static_cast<Qt::PenCapStyle>(ui->penCapCombobox->currentData().toInt());
    const Qt::PenJoinStyle join = static_cast<Qt::PenJoinStyle>(ui->penJoinComboBox->currentData().toInt());

    QPen pen;
    pen.setWidth(penWidth);
    pen.setStyle(style);
    pen.setJoinStyle(join);
    pen.setCapStyle(cap);

    canvas->setPen(pen);

}

void Widget::brushChanged()
{
    const Qt::BrushStyle style = static_cast<Qt::BrushStyle>(ui->brushStyleCombobox->currentData().toInt());

    if (style == Qt::LinearGradientPattern) {
        QLinearGradient linearGradient(0, 0, 100, 100);
        linearGradient.setColorAt(0.0, Qt::red);
        linearGradient.setColorAt(0.2, Qt::green);
        linearGradient.setColorAt(1.0, Qt::blue);
        canvas->setBrush(linearGradient);
    } else if (style == Qt::RadialGradientPattern) {
        QRadialGradient radialGradient(50, 50, 50, 70, 70);
        radialGradient.setColorAt(0.0, Qt::red);
        radialGradient.setColorAt(0.2, Qt::green);
        radialGradient.setColorAt(1.0, Qt::blue);
        canvas->setBrush(radialGradient);
    } else if (style == Qt::ConicalGradientPattern) {
        QConicalGradient conicalGradient(50, 50, 150);
        conicalGradient.setColorAt(0.0, Qt::red);
        conicalGradient.setColorAt(0.2, Qt::green);
        conicalGradient.setColorAt(1.0, Qt::blue);
        canvas->setBrush(conicalGradient);
    } else if (style == Qt::TexturePattern) {
        canvas->setBrush(QBrush(QPixmap(":/images/learnqt.png")));
    } else {
        canvas->setBrush(QBrush(Qt::blue, style));
    }

}
















