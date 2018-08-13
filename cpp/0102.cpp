#include <cstdlib>
#include <iostream>
#include<stdio.h>
using namespace std;


int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n;
    while(cin>>n,n){
        int Na = n+1;
        int a[12*12] = {};
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cin >> a[i*Na+j];
                a[n*Na+j] += a[i*Na+j];
                a[i*Na+n] += a[i*Na+j];
            }
            a[n*Na+n] += a[i*Na+n];
        }
        for(int i=0;i<Na;i++){
            for(int j=0;j<Na;j++){
                printf("%5d",a[i*Na+j]);
            }
            printf("\n");
        }
    }
    return 0;
}