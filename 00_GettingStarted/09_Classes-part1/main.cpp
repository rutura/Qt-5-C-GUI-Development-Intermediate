/*
 *      . Introducing classes
 *      . Setting up member variables
 *      . Using default constructor
 *      . Constructors will be covered in next lecture
 *
 * */

#include <iostream>

class Rectangle {
public:
    void setWidth( int width);
    void setLength( int length);

    int getArea()const{
        return width * length;
    }
private:
    int width;
    int length;
};

void Rectangle::setWidth(int width)
{
    this->width = width;
}

void Rectangle::setLength(int length)
{
    this->length = length;
}

int main()
{

    Rectangle r;
    r.setWidth(10);
    r.setLength(20);
    std::cout << "Area : " << r.getArea() <<std::endl;

    return 0;
}
