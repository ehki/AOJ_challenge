#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;


int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    string a;
    int b,p,o;
    while(n--, n>=0){
        b = p = o = 0;
        while( cin >> a){
            if (a=="HIT"){
                b += 1;
                if (b >= 4){
                    b = 3;
                    p += 1;
                }
            } else if (a=="OUT"){
                o += 1;
                if (o >= 3) {
                    printf("%d\n",p);
                    break;
                }
            } else if (a=="HOMERUN"){
                p += b+1;
                b = 0;
            }
        }
    }
    return 0;
}