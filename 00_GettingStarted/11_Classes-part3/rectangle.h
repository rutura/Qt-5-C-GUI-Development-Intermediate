#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {

public:
    Rectangle();
    Rectangle(int w,int l);


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

#endif // RECTANGLE_H
