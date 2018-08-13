#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int main(){
    int h,w;
    while(1){
        int h,w;
        scanf("%d %d",&h,&w);
        cin.ignore();
        if (h==0 & w==0){
            return 0;
        }
        char ma[100][100];
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                scanf(" %c",&ma[i][j]);
            }
        }
        int px,py;
        px = py = 0;
        while(1){
            // printf("%d %d %c\n",py,px,ma[py][px]);
            switch(ma[py][px]){
                case '>':
                    ma[py][px] = 'x';
                    px += 1;
                    break;
                case '^':
                    ma[py][px] = 'x';
                    py -= 1;
                    break;
                case '<':
                    ma[py][px] = 'x';
                    px -= 1;
                    break;
                case 'v':
                    ma[py][px] = 'x';
                    py += 1;
                    break;
            }
            if(ma[py][px] == 'x'){
                printf("LOOP\n");
                break;
            }else if (ma[py][px] == '.'){
                printf("%d %d\n", px,py);
                break;
            }
        }
    }
    return 0;
}