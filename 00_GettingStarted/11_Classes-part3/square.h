#ifndef SQUARE_H
#define SQUARE_H
#include "rectangle.h"
class Square : public Rectangle
{
public:
    Square( int side):Rectangle(side,side)
    {
    }

};
#endif // SQUARE_H
