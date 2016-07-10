#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        
       char Str[100001];
    int len,i,c=0;
    
    scanf("%s",Str);
    len=strlen(Str);
   
    for(i=0;i<len;i++)
        if(Str[i]==Str[i+1])
        c++;
        
        printf("%d\n",c);
    
}
    return 0;
}
