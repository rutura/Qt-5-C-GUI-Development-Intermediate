/*
 *  . Showing how to create non Qt console apps with Qt creator
 *  . By default the output shows up in the application output pane
 *          of Qt Creator.
 *
 *  . To change this, you can to to Projects Mode, select the run configuration
 *      of the currently being used Kit and in Run settings, tick the checkbox
 *      saying Run in terminal
 *
 *  . We can also instruct Qt creator to set up projects in a way that
 *      output shows up in the terminal by default by Tools -> Options
 *          -> Build&Run
 *
 *   . To try this out, create a dummy project and show that it'll show up
 *          with the run in terminal thing checked by default. After this
 *          you can get rid of the dummy project.
 *
 *   . Turn back to not running in the terminal by default.
 *
 *
 * */

#include <iostream>
int main()
{
    std::cout << "Hello World!" << std::endl;
    std::cout << "How are you" << std::endl;
    return 0;
}
