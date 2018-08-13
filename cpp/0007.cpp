#include <cstdlib>
#include <iostream>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    int a;
    uint b = 100000;
    while (std::cin >> a) {
        for (int i=1; i <= a; i++){
            b = b*1.05;
            if (b%1000 != 0) {
                b -= b%1000;
                b += 1000;
            }
        }
        std::cout << b << std::endl;
    }
    return EXIT_SUCCESS;
}