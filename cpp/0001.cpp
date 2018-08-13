#include <cstdlib>
#include <iostream>
#include <algorithm>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    int a[10];
    int i=0;
    while (std::cin >> a[i]) {
        i++;
    }
    std::sort(a, a+10);
    for (i=9; i>6; i--){
        std::cout << a[i] << std::endl;
    }
    return EXIT_SUCCESS;
}