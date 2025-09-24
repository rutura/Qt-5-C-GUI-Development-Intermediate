#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QFormLayout>
#include <QPushButton>
#include <QGroupBox>
#include <QMessageBox>
#include <QTableWidgetItem>
#include <QHeaderView>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

      // Store UI elements in member variables for easier access
    nameEdit = ui->nameEdit;
    subjectEdit = ui->subjectEdit;
    scoreEdit = ui->scoreEdit;
    tableWidget = ui->tableWidget;
    averageScoreLabel = ui->averageScoreLabel;

      // Connect signals and slots
    connect(ui->addStudentButton, &QPushButton::clicked, this, &MainWindow::addStudent);
    connect(ui->clearAllButton, &QPushButton::clicked, this, &MainWindow::clearStudents);
    connect(tableWidget, &QTableWidget::itemChanged, this, &MainWindow::itemChanged);

      // Configure tableWidget properties
    tableWidget->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
    tableWidget->setSelectionBehavior(QAbstractItemView::SelectRows);
    tableWidget->setAlternatingRowColors(true);
    tableWidget->setEditTriggers(QAbstractItemView::DoubleClicked | QAbstractItemView::SelectedClicked);
    
    // Set font for average score label
    QFont font = averageScoreLabel->font();
    font.setBold(true);
    averageScoreLabel->setFont(font);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::addStudent()
{
    // Get input values
    QString name = nameEdit->text().trimmed();
    QString subject = subjectEdit->text().trimmed();
    QString scoreText = scoreEdit->text().trimmed();

    // Validate inputs
    if (name.isEmpty() || subject.isEmpty() || scoreText.isEmpty()) {
        QMessageBox::warning(this, "Validation Error", "All fields must be filled in.");
        return;
    }
    
    // Validate score
    double score;
    if (!validateScore(scoreText, score)) {
        QMessageBox::warning(this, "Validation Error", "Score must be a number between 0 and 100.");
        return;
    }
    
    // Add new row to table
    int row = tableWidget->rowCount();
    tableWidget->insertRow(row);
    
    // Create and set table items
    QTableWidgetItem *nameItem = new QTableWidgetItem(name);
    QTableWidgetItem *subjectItem = new QTableWidgetItem(subject);
    QTableWidgetItem *scoreItem = new QTableWidgetItem(scoreText);
    
    // Make first two columns non-editable
    nameItem->setFlags(nameItem->flags() & ~Qt::ItemIsEditable);
    subjectItem->setFlags(subjectItem->flags() & ~Qt::ItemIsEditable);
    
    // Set items in the table
    tableWidget->setItem(row, 0, nameItem);
    tableWidget->setItem(row, 1, subjectItem);
    tableWidget->setItem(row, 2, scoreItem);
      // Apply red background if score is below 40
    if (score < 40.0) {
        scoreItem->setBackground(QColor(255, 200, 200)); // Light red
    } else {
        scoreItem->setBackground(QColor(Qt::green)); // Normal background
    }
    
    // Clear input fields
    nameEdit->clear();
    subjectEdit->clear();
    scoreEdit->clear();
    nameEdit->setFocus();
    
    // Update average score
    updateAverageScore();
}

void MainWindow::clearStudents()
{
    // Ask for confirmation
    QMessageBox::StandardButton reply = QMessageBox::question(this, 
        "Confirmation", 
        "Are you sure you want to clear all student records?",
        QMessageBox::Yes | QMessageBox::No);
    
    if (reply == QMessageBox::Yes) {
        // Temporarily disconnect itemChanged signal to prevent multiple updates
        disconnect(tableWidget, &QTableWidget::itemChanged, this, &MainWindow::itemChanged);
        
        // Clear all rows
        tableWidget->setRowCount(0);
        
        // Reconnect signal
        connect(tableWidget, &QTableWidget::itemChanged, this, &MainWindow::itemChanged);

        // Reset average score
        averageScoreLabel->setText("Average Score: 0.0");
    }
}

void MainWindow::itemChanged(QTableWidgetItem *item)
{
    // Only process changes to the Score column (column 2)
    if (item && item->column() == 2) {
        double score;
        QString scoreText = item->text().trimmed();
        
        // Validate the edited score
        if (!validateScore(scoreText, score)) {
            QMessageBox::warning(this, "Invalid Score", 
                "Score must be a number between 0 and 100.\nChanges will be reverted.");
            
            // Restore previous valid value or set to 0
            item->setText("0");
            return;
        }
        
        // Update cell background based on score
        if (score < 40.0) {
            item->setBackground(QColor(255, 200, 200)); // Light red for failing scores
        } else {
            item->setBackground(QColor(Qt::green)); // Reset background
        }
        
        // Update average score
        updateAverageScore();
    }
}

void MainWindow::updateAverageScore()
{
    double totalScore = 0.0;
    int count = 0;
    
    // Calculate sum of all scores
    for (int row = 0; row < tableWidget->rowCount(); ++row) {
        QTableWidgetItem *scoreItem = tableWidget->item(row, 2);
        if (scoreItem) {
            bool ok;
            double score = scoreItem->text().toDouble(&ok);
            if (ok) {
                totalScore += score;
                count++;
            }
        }
    }
    
    // Calculate and display average
    double average = (count > 0) ? (totalScore / count) : 0.0;
    averageScoreLabel->setText(QString("Average Score: %1").arg(average, 0, 'f', 1));
}

bool MainWindow::validateScore(const QString &scoreText, double &score)
{
    bool ok;
    score = scoreText.toDouble(&ok);
    
    // Check if conversion succeeded and score is in valid range
    if (!ok || score < 0.0 || score > 100.0) {
        // Output debug information
        qDebug() << "Score validation failed: " << scoreText << ", ok=" << ok << ", score=" << score;
        return false;
    }
    
    // Valid score
    qDebug() << "Score validation passed: " << scoreText << ", score=" << score;
    return true;
}
