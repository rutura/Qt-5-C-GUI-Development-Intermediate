/*
 *      . Classes across multiple files
 *
 * */

#include <iostream>
#include "rectangle.h"
#include "box.h"
#include "square.h"


int main()
{
    Rectangle r;
    Rectangle r1(20,20);
    Box b ( 30,30,30);
    Square s(40);
    std::cout << "The area of the rectangle is : " << r1.getArea() << std::endl;
    std::cout << "The volume of our shape is : " << b.getVolume() <<std::endl;
    std::cout << "The area of your square is : " << s.getArea() << std::endl;
    return 0;
}
