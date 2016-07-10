#include <stdio.h>  
#include <string.h>  
#include <math.h>  
#include <stdlib.h>  
int main()  
{  
      unsigned long long int i;  
      int t,count,n1,n2;  
      scanf("%d",&t);  
      while(t--)  
      {  
           scanf("%d %d",&n1,&n2);  
           count = floor(sqrt(n2))-ceil(sqrt(n1))+1;
            printf("%d\n",count);  
      }  
      return 0;  
}  