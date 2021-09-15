%{
%}

%%
aa[a+b]*bb {printf( "Valid String\n"); }
.* { printf("Invalid String\n");}

%%
int yywrap(){}
int main()
{
    yylex();
    return 0;
}
