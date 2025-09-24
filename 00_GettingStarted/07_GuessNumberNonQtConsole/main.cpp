/*
 *      . Work hard to explain the logic of seeds
 *
 *      . It'll be fun to take this app and turn it into GUI
 *
 * */


#include <iostream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;

int main()
{
    int guessNumber, secretNumber;
    //Initialize
    //srand(time(NULL));
    srand (static_cast<unsigned int>((time(nullptr))));

    //Generate (1-10)
    secretNumber = rand() % 10 + 1;

    //Ask the user to guess
    cout << "Guess my number ( 1-10 ) :";
    do
    {
        cin >> guessNumber;
       if( secretNumber < guessNumber)
       {
            cout << "The number is lower than that" <<endl;
       }

       if( secretNumber > guessNumber)
       {
            cout << "The number is higher than that" <<endl;
       }
    }while( guessNumber != secretNumber);

    cout<< "Congratulations, the  number is :"<<guessNumber <<endl;


    return 0;
}
