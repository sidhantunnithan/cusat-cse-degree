%{
%}

%%
[0+1]*000[0+1]* {printf( "Valid String\n"); }
.* { printf("Invalid String\n");}

%%
int yywrap(){}
int main()
{
    yylex();
    return 0;
}
