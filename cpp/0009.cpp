#include <cstdlib>
#include <iostream>
#include <math.h>



void Eratosthenes(int N){

}

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    int n,m;
    while (std::cin >> n) {
        // std::cout << n << "," << std::endl;
        m = 0;
        int arr[n];
        for(int i = 0; i <= n; i++){
            arr[i] = 1;
        }
        for(int i = 2; i <= sqrt(n); i++){
            if(arr[i]){
                for(int j = 0; i * (j + 2) <= n; j++){
                    arr[i *(j + 2)] = 0;
                }
            }
        }
        for(int i = 2; i <= n; i++){
            if(arr[i]){
                // std::cout << i << std::endl;
                m++;
            }
        }
        std::cout << m << std::endl;
    }
    return EXIT_SUCCESS;
}