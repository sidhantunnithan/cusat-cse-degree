%{
        #include<stdio.h>
        int valid=0;
%}

%token FOR TYPE ID NUM LE GE EQ NE OR AND

%%

start:  statement {valid = 1;};
statement: FOR '(' TYPE ID '=' NUM ';' condition ';' E ')' '{' ST1';' '}'
        | FOR '(' ';' ';' ')' '{' ST1';' '}'
        | FOR '(' ID '=' NUM ';' condition ';' E ')' '{' ST1';' '}'
        | FOR '(' TYPE ID '=' NUM ';' condition ';' E ')' ';'
        | FOR '(' ID '=' NUM ';' condition ';' E ')' ';'
        ;
ST1: statement
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
        printf("\nEnter Any for statement \n");
        yyparse();
        if(valid)
                printf("\nEntered for statement is Valid\n\n");
}

int yyerror()
{
        valid=0;
        printf("\nEntered for statement is Invalid\n\n");
        return 0;
}

