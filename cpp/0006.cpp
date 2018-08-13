#include <cstdlib>
#include <iostream>
#include <algorithm>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    std::string a;
    while (std::getline(std::cin, a)) {
        reverse(a.begin(), a.end());
        std::cout << a << std::endl;
    }
    return EXIT_SUCCESS;
}