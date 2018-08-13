#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <stdio.h>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    double a,b,c,d,e,f;
    while (std::cin >> a >> b >> c >> d >> e >> f) {
        double x,y;
        y = (a*f-c*d)/(a*e-b*d);
        x = (c-b*y)/ a;
        printf("%.3f %.3f\n",x,y);
    }
    return EXIT_SUCCESS;
}