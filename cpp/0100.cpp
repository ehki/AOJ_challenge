#include <cstdlib>
#include <iostream>
#include <math.h>



void Eratosthenes(int N){

}

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);

    int n;
    while (std::cin >> n) {
        if (n==0){
            return EXIT_SUCCESS;
        }
        int Nw = 4000;
        int ar[Nw];
        for( int i=0; i < Nw; i++){
            ar[i] = -1;
        }
        int br[Nw];
        for( int i=0; i < Nw; i++){
            br[i] = 0;
        }
        int e,p,q;
        for(int i = 0; i < n; i++){
            std::cin >> e >> p >> q;
            int b = -1;
            for(int k=0; k<Nw; k++){
                if (ar[k] == e) {
                    br[k] += p*q;
                    b = 1;
                    break;
                }
            }
            if (b==-1){
                for(int k=0; k<Nw; k++){
                    if (ar[k] == -1) {
                        ar[k] = e;
                        br[k] = p*q;
                        break;
                    }
                }
            }
        }
        int f = 0;
        for(int i =0; i < Nw; i++){
            if (br[i] >= 1000000){
                std::cout << ar[i] << std::endl;
                f = 1;
            }
        }
        if ( f == 0 ){
            std::cout << "NA" << std::endl;
        }
        // for(int i = 0; i< 5; i++){
        //     fprintf(stderr,"i=%2d, ar[i]=%5d, br[i]=%9d\n",i,ar[i],br[i]);
        // }
        // return EXIT_SUCCESS;
    }
    return EXIT_SUCCESS;
}