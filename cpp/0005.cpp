#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <stdio.h>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    long a,b,c,d;
    while (std::cin >> a >> b) {
        if (a > b){
            c = a;
            d = b;
        }else{
            c = b;
            d = a;
        }
        long temp;
        while (c % d != 0){
            temp = d;
            d = c % d;
            c = temp;
        }
        std::cout << d << " " << a*b/d << std::endl;
    }
    return EXIT_SUCCESS;
}