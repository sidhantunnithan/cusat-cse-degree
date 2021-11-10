%{
#include<stdio.h>
int valid=0;
%}

%token IF ELSE ID NUM LE GE EQ NE OR AND

%%

start:  statement {valid = 1;};
statement: IF '(' condition ')' '{' ST1';' '}' ELSE '{' ST1';' '}'
        | IF '(' condition ')' '{' ST1';' '}'
        ;
ST1:    statement
        | E
        ;
E:      ID'='E
        | E'+'E
        | E'-'E
        | E'*'E
        | E'/'E
        | E'<'E
        | E'>'E
        | E LE E
        | E GE E
        | E EQ E
        | E NE E
        | E OR E
        | E AND E
        | ID
        | NUM
        ;
condition: E'<'E
        | E'>'E
        | E LE E
        | E GE E
        | E EQ E
        | E NE E
        | E OR E
        | E AND E
        | ID
        | NUM
        ;

%%

//driver code
void main()
{
    printf("\nEnter Any if-else statement \n");
    yyparse();
    if(valid)
    printf("\nEntered if-else statement is Valid\n\n");
}

int yyerror()
{
    valid=0;
    printf("\nEntered if-else statement is Invalid\n\n");
    return 0;
}
