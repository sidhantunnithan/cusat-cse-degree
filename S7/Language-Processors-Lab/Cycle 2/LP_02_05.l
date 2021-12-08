%{
    #include<stdio.h>
    char beg[] = "begin";
    char end[] = "end";
    FILE *outp;
%}

%%
[{] {fwrite(&beg[0],sizeof(char),5,outp);}
[}] {fwrite(&end[0],sizeof(char),3,outp);}
. {fwrite(yytext,sizeof(char),1,outp);}
["\n"] {fwrite(yytext,sizeof(char),1,outp);}
%%

int yywrap(){
    return(1);
}

int main(int argc, char* argv[]){
    if (argc != 2){
        printf("Filename not specified");
        exit(0);
    }
    yyin = fopen(argv[1],"r");
    outp = fopen("outdoc.txt","w");
    yylex();
}
