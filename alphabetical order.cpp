#include <stdio.h> 
#include <string.h>

void LetterCapitalize(char str[]) { 
  
  // code goes here- *Please feel free to conribute*
  int i,j,temp;
   for(i=0;i<strlen(str);i++){
	  if(str[i]>=97 && str[i]<=122)
   	    {		
		   for(j=0;j<str[j];j++){
		   	if(str[i]<str[j])
		   		{
		   			temp=str[i];
		   			str[i]=str[j];
		   			str[j]=temp;
				   }
		   }   
   	    	
		}
   	}
  printf("%s",str);

            
}

int main(void) { 
  
  // keep this function call here
  char str[100];
  {
  LetterCapitalize(gets(str));
  //getch();
  }
  return 0;
    
} 

