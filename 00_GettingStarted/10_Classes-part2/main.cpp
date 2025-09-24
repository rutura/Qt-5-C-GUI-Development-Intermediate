/*
     *   . Setting up a bunch of constructors and methods
     *   . We also set up a Paralellepipede class. May be I should just use
     *      box here as it's easier to pronounce.
     *
 **/

#include <iostream>

using namespace std;

class Rectangle {

public:
    Rectangle();
    Rectangle(int w,int l);

    //...

    void setWidth( int width);


    void setLength( int length);

    int getArea()
    {
        return width * length;
    }

private:
    int width;
    int length;
};

Rectangle::Rectangle()
{
    clog << "Default Constructor called" <<endl;
    this->length = 5;
    this->width = 5;
}
/*
Rectangle::Rectangle(int w, int l)
{
    clog << "Custom Constructor called" <<endl;
    this->width = w;
    this->length = l;
}
*/
Rectangle::Rectangle(int w, int l):width(w),length(l)
{
    clog << "Custom Constructor called" <<endl;
}


void Rectangle::setWidth(int width)
{
    this->width = width;
}

void Rectangle::setLength(int length)
{
    this->length = length;
}


//Box class

class Box
{
public:
    Box(int w, int l, int h):r(w,l),height(h)
    {
        cout << "Para Constructor Called";
    }

    int getVolume()
    {
        return r.getArea() * height;
    }

private:
    Rectangle r;
    int height;
};



int main()
{

    Rectangle r;
    Rectangle r1(20,20);
    Box b ( 30,30,30);
    std::cout << std::endl;
    std::cout << "Area : " << r1.getArea() << std::endl;
    std::cout << "Volume : " << b.getVolume() <<std::endl;

    return 0;
}
