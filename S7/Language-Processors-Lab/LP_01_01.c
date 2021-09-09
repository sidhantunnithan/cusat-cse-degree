#include <stdio.h>
#include <stdbool.h>  
#include <string.h>

void main() {
    char s[1000];
    bool valid = 1;
    int state = 0;
    printf("input string : ");
    scanf("%s", s);

    for(int i = 0; s[i] != '\0'; ++i) {
        if(state == 0){
            if(s[i] == 'b')
                continue;
            else if(s[i] == 'a')
                state = 1;
            else{
                valid = 0;
                break;
            }
        }

        else if(state == 1){
            if(s[i] == 'a')
                continue;
            else if(s[i] == 'b')
                state = 2;
            else{
                valid = 0;
                break;
            }
        }
        
        else if(state == 2){
            if(s[i] == 'a')
                state = 1;
            else if(s[i] == 'b')
                state = 3;
            else{
                valid = 0;
                break;
            }
        }

        else if(state == 3){
            if(s[i] == 'a')
                state = 1;
            else if(s[i] == 'b')
                state = 0;
            else{
                valid = 0;
                break;
            }
        }
    }

    if(valid && state == 3){
        printf("valid\n");
    } else {
        printf("not valid\n");
    }

    return;
}