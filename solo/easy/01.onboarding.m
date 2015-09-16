#include <Foundation/Foundation.h>
int main(int a, const char *A[]){
    while(1){
        char e[50],E[50];
        int d,D;
        scanf("%s%d%s%d",e,&d,E,&D);
        if(d<D) printf("%s\n", &e);
        else printf("%s\n", &E);
    }
}