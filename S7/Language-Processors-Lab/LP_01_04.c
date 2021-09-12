#include <stdio.h>
#include <stdbool.h>  
#include <string.h>

const int transition_table[][3] = {
    {1, 0, 0},      // state 0, initial state
    {1, 2, 0},      // state 1
    {1, 0, 3},      // state 2
    {3, 3, 3},      // state 3, final state
    {4, 4, 4}       // dead state
};
const int final_state[] = {3};
const int num_final_states = sizeof(final_state)/sizeof(final_state[0]);

void main() {
    char s[1000];
    bool valid = false;
    int state = 0;
    printf("input string : ");
    scanf("%s", s);
    for(int i=0; s[i] != '\0' ; i++){
        if(s[i] != 'a' && s[i] != 'b' && s[i] != 'c')
            state = 4;
        if(state == 4)
            break;
        state = transition_table[state][s[i] - 'a'];
    }
    for(int i=0; i<num_final_states; i++)
        if(state == final_state[i]){
            valid = true;
            break;
        }
    if(valid)
        printf("String is Valid!\n");
    else 
        printf("String is not Valid!\n");
    return;
}