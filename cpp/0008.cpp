#include <cstdlib>
#include <iostream>

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    int n,m;
    while (std::cin >> n) {
        m = 0;
        for(int i=0;i<=9;i++){
            for(int j=0;j<=9;j++){
                for(int k=0;k<=9;k++){
                    for(int l=0;l<=9;l++){
                        if (i+j+k+l == n){
                            m += 1;
                        }
                    }
                }
            }
        }
        std::cout << m << std::endl;
    }
    return EXIT_SUCCESS;
}