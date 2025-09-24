#ifndef APPLICATION_H
#define APPLICATION_H

#include <QObject>
#include <QApplication>

class Application : public QApplication
{
    Q_OBJECT
public:
    explicit Application(int& argc, char** argv);

public:
    bool notify(QObject *, QEvent *) override;
signals:

};

#endif // APPLICATION_H
