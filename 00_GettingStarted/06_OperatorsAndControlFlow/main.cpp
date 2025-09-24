/*
 *      . Exploring some operators and control flow in C++
 *      . Visualize this in slides
 *
 * */


#include <iostream>

using namespace std;

int main()
{
    int a = 20;
    int b = 20;

    //Comment
    cout << "----------Math Operators------------"<<endl;
    cout << "a + b = " << a + b  << endl;
    cout << "a - b = " << a - b  << endl;
    cout << "a * b = " << a * b  << endl;
    cout << "a / b = " << (float) a / b  << endl;
    cout << "a % b = " << a % b  << endl;



  //  cout << "----------Logical Operators------------"<<endl;

    /* >,<,>=,<=,==
      */

    //Decisions
    if( a == b)
    {
        cout << "A is equal to b " <<endl;
    }else
    {
        cout << "A is not equal to b" <<endl;
    }

    //Loops
    /*
    cout << "Hello Daniel 1" <<endl;
    cout << "Hello Daniel 2" <<endl;
    cout << "Hello Daniel 3" <<endl;
    cout << "Hello Daniel 4" <<endl;
    cout << "Hello Daniel 5" <<endl;
    cout << "Hello Daniel 7" <<endl;
    cout << "Hello Daniel 8" <<endl;
    cout << "Hello Daniel 9" <<endl;
    cout << "Hello Daniel 10" <<endl;
    cout << "Hello Daniel 11" <<endl;
    cout << "Hello Daniel 12" <<endl;
    cout << "Hello Daniel 13" <<endl;
    cout << "Hello Daniel 14" <<endl;
    cout << "Hello Daniel 15" <<endl;
    cout << "Hello Daniel 16" <<endl;
    cout << "Hello Daniel 17" <<endl;
    cout << "Hello Daniel 18" <<endl;
    cout << "Hello Daniel 19" <<endl;
    cout << "Hello Daniel 20" <<endl;
    */

    //For loop
    /*
    for ( int i = 1 ; i <= 20 ; i=i+1)
    {
        cout << "Hello Daniel "<<i<<endl;
    }
    */

    //While loop
    /*
    int i =1;
    while ( i <= 20)
    {
      cout << "Hello Daniel "<<i<<endl;
      i=i+1;
    }
    */

    //Do while loop
    int i = 1;
    do{
        cout << "Hello Daniel "<<i<<endl;
        i=i+1;
    }while( i <=20);


    //While loop

    return 0;
}
