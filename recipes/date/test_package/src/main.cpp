#include <cstdlib>
#include <iostream>

#include "date/date.h"
//#include "date/tz.h"

int main() {
    //auto& db = date::get_tzdb();
    std::cout << date::weekday{date::may/20/2023} << '\n';
    return EXIT_SUCCESS;
}
