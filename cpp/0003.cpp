#include <cstdlib>
#include <iostream>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    int n,a,b,c;
    bool f;
    std::cin >> n;
    while (std::cin >> a >> b >> c) {
        f = false;
        if (c*c == a*a+b*b) {
            f = true;
        } else if (a*a == b*b+c*c) {
            f = true;
        } else if (b*b == c*c+a*a) {
            f = true;
        } else {
            std::cout << "NO" << std::endl;
        }
        if (f) {
            std::cout << "YES" << std::endl;
        }
    }
    return EXIT_SUCCESS;
}