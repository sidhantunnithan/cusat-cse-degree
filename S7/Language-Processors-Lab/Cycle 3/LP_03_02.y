%{
    #include<stdio.h>
    int valid=0;
%}

%token ID NUM LE GE EE NE OR AND

%%
start: statement {valid = 1;}
statement: ID'=' e ';'
e: e '+' e
    | e '*' e
    | e '-' e
    | e '/' e
    | e '>' e
    | e '<' e
    | e LE e
    | e GE e
    | e EE e
    | e NE e
    | e OR e
    | e AND e
    | '(' e ')'
    | ID
    | NUM
    ;
%%

void main() {
    printf("Enter any expression: ");
    yyparse();
    if(valid){
        printf("Entered expression is valid!\n");
    }
}

int yyerror(){
    valid = 0;
    printf("Entered expression is invalid!\n");
    return 0;
}