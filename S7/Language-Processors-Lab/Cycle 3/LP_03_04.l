%{
    #include "y.tab.h";
    extern int yylval;
%}


%%
[ \t]
for return FOR;
int|float|char return TYPE;
[a-zA-Z_][a-zA-Z_0-9]* return ID;
[0-9]+(\.[0-9]*)? return NUM;
"<=" return LE;
">=" return GE;
"==" return EQ;
"!=" return NE;
"||" return OR;
"&&" return AND;
. return yytext[0];
\n return 0;

%%
int yywrap(){
    return 1;
}

