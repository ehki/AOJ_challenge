#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    int a,b;
    int num;
    while (std::cin >> a >> b) {
        num = a+b;
        unsigned digit=0;
        while(num!=0){
            num /= 10;
            digit++;
        }
        std::cout << digit << std::endl;
    }
    
    return EXIT_SUCCESS;
}