/*
 *  Calories burnt calculator
 *      . Reference : http://www.shapesense.com/fitness-exercise/calculators/walking-calorie-burn-calculator.shtml
 *      . We will assume the user is walking on a level surface
 *          . Formula :  CB = [0.0215 x KPH^3 - 0.1765 x KPH^2 + 0.8710 x KPH + 1.4577] x WKG x T
 *          . where
                CB = Calorie burn (in calories)
                KPH = Walking speed (in kilometres per hour)
                WKG = Weight (in kilograms)
                T = Time (in hours)

             . When trying this out and comparing results to those from shapesense,
                    use their distance and time to compute the speed.


         . Goal : make this work using signals and slots

         . You'll do another one using property bindings
 * */

#include "widget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Widget w;
    w.show();
    return a.exec();
}
