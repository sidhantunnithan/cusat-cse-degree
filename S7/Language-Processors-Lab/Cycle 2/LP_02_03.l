%{
FILE *outp;
%}

%%
[0-9]+ {}
[ ]+[0-9]*[ ]* {fputs(" ", outp);}
. {fputs(yytext, outp);}
%%

int main(int argc, char* argv[])
{
if (argc != 2)
{
    printf("Filename not specified\n");
    exit(0);
}
yyin = fopen(argv[1],"r");
outp = fopen("output.txt", "w");
yylex();
}
 
int yywrap()
{
return(1);
}