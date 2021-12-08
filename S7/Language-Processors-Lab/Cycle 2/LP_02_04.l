%{
    int num_statements=0;
    int num_identifier=0;
    int num_assignment=0;
    int num_relational=0;
    int num_keyword=0;
    int num_int=0;
%}

%%
#include<.*> {}
".*" {}
; {num_statements++;} 
auto|double|if|static|break|else|int|struct|case|enum|long|switch|char|extern|near|typedef|const|float|continue|register|union|unsigned|void|while|default|do|goto|signed|while|signed|unsigned  {num_keyword++;}
[a-zA-Z][a-zA-Z0-9]* {num_identifier++;}
==|<=|>=|!=|<|> {num_relational++;}
= {num_assignment++;}
[0-9]+ {num_int++;}
. {}
\n {}
%%

int yywrap(void)
{
    return 1;
}

int main(int argc, char*argv[])
{
    yyin=fopen(argv[1],"r");
    yylex();
    printf("Number of statements: %d\nNumber of identifiers: %d\nNumber of assignment operators: %d\n", num_statements, num_identifier, num_assignment);
    printf("Number of relational operators: %d\nNumber of keywords: %d\nNumber of integers: %d\n", num_relational, num_keyword, num_int);
    return 0;
}