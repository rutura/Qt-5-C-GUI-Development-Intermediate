#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);

    // Connect water tank signals to indicator slots
    connect(ui->waterTank, &WaterTank::normal, ui->indicator, &Indicator::activateNormal);
    connect(ui->waterTank, &WaterTank::warning, ui->indicator, &Indicator::activateWarning);
    connect(ui->waterTank, &WaterTank::danger, ui->indicator, &Indicator::activateDanger);

    // Setup controls
    setupControls();

    // Connect control signals
    connect(ui->resetButton, &QPushButton::clicked, this, &Widget::onResetClicked);
    connect(ui->startStopButton, &QPushButton::clicked, this, &Widget::onStartStopClicked);
    connect(ui->waterTank, &WaterTank::waterLevelChanged, this, &Widget::onWaterLevelChanged);
    connect(ui->waterLevelSlider, &QSlider::valueChanged, ui->waterTank, &WaterTank::setWaterLevel);
    connect(ui->warningThreshold, QOverload<int>::of(&QSpinBox::valueChanged),
            ui->waterTank, &WaterTank::setWarningThreshold);
    connect(ui->dangerThreshold, QOverload<int>::of(&QSpinBox::valueChanged),
            ui->waterTank, &WaterTank::setDangerThreshold);

}

Widget::~Widget()
{
    delete ui;
}

void Widget::onWaterLevelChanged(int level)
{
    ui->waterLevelSlider->blockSignals(true);
    ui->waterLevelSlider->setValue(level);
    ui->waterLevelSlider->blockSignals(false);
    ui->waterLevelDisplay->display(level);

}

void Widget::onResetClicked()
{
    ui->waterTank->resetWaterLevel();
}

void Widget::onStartStopClicked()
{
    m_isSimulationRunning = !m_isSimulationRunning;
    if (m_isSimulationRunning) {
        ui->waterTank->startSimulation();
        ui->startStopButton->setText("Stop");
    } else {
        ui->waterTank->stopSimulation();
        ui->startStopButton->setText("Start");
    }

}

void Widget::setupControls()
{
    // Setup water level slider
    ui->waterLevelSlider->setMinimum(ui->waterTank->MIN_WATER_HEIGHT);
    ui->waterLevelSlider->setMaximum(ui->waterTank->MAX_WATER_HEIGHT);
    ui->waterLevelSlider->setValue(ui->waterTank->waterLevel());

    // Setup threshold spinboxes
    ui->warningThreshold->setRange(ui->waterTank->MIN_WATER_HEIGHT, ui->waterTank->MAX_WATER_HEIGHT);
    ui->dangerThreshold->setRange(ui->waterTank->MIN_WATER_HEIGHT, ui->waterTank->MAX_WATER_HEIGHT);
    ui->warningThreshold->setValue(ui->waterTank->warningThreshold());
    ui->dangerThreshold->setValue(ui->waterTank->dangerThreshold());

    // Initial display value
    ui->waterLevelDisplay->display(ui->waterTank->waterLevel());
}
















