#include <stdio.h>
#include <stdbool.h>  
#include <string.h>

const int transition_table[][2] = {
    {1, 0},     // state 0, initial state & final state
    {2, 0},     // state 1
    {3, 0},     // state 2
    {3, 3}      // dead state 
};
const int final_state[] = {0};
const int num_final_states = sizeof(final_state)/sizeof(final_state[0]);

void main() {
    char s[1000];
    bool valid = false;
    int state = 0;
    printf("input string : ");
    scanf("%s", s);
    for(int i=0; s[i] != '\0' ; i++){
        if(s[i] != '0' && s[i] != '1')
            state = 3;
        if(state == 3)
            break;
        state = transition_table[state][s[i] - '0'];
    }
    for(int i=0; i<num_final_states; i++)
        if(state == final_state[i]){
            valid = true;
            break;
        }
    if(valid)
        printf("Valid string!\n");
    else 
        printf("Invalid string!\n");
    return;
}