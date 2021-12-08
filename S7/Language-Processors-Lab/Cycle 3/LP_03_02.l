digit [0-9]
letter [A-Za-z]

%{
    #include "y.tab.h";
%}

%%
[ \t] ;
{letter}({letter}|{digit}|_)* return ID;
{digit}* return NUM;
"<=" return LE;
">=" return GE;
"==" return EE;
"!=" return NE;
"||" return OR;
"&&" return AND;
. return yytext[0];
\n return 0;
%%

int yywrap() {
    return 0;
}