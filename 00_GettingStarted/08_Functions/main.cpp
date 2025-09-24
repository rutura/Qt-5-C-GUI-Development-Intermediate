#include <iostream>

//[Return Type] [Function name] [Function Parameters]
void sayHi(){
   std::cout << "Hello Daniel!" << std::endl;
}

int add( int a, int b){
    std::cout << "int version of add called..." << std::endl;
    return a + b;
}

float add(float a , float b){
    std::cout << "float version of add called..." << std::endl;
    return a + b;
}

double add(double a, double b){
    std::cout << "double version of add called..."<< std::endl;
    return a + b;
}

int main()
{
    sayHi();

    auto result_int = add(3,7);
    std::cout << "result_int :"<< result_int  <<std::endl;

    auto result_float = add(3.3f,7.4f);
    std::cout << "result_float :"<< result_float  <<std::endl;

    auto result_double = add(4.3,8.4);
    std::cout << "result_double :"<< result_double  <<std::endl;

    return 0;
}
