#include <stdio.h>
int main(){
    while(1){
        int d,D;
        char e[50],E[50];
        scanf("%s%d%s%d",&e,&d,&E,&D);
        printf("%s\n",(d<D)?e:E);
    }
}