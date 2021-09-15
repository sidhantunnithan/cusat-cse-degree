%{
int num_lines=0,num_words=0,num_chars=0;
%}

%%
\n { num_chars++; num_lines++; }
[^ \n]+ { num_words++, num_chars=num_chars+yyleng;}
. {num_chars++;}
%%
int yywrap(void)  
{
 return 1;
}


int main(int argc, char*argv[]) 
{
	yyin=fopen(argv[1],"r");
    yylex();
    printf("Chars = %d\nWords = %d\nLines = %d\n",num_chars,num_words,(num_lines+1));

    return 0;
} 