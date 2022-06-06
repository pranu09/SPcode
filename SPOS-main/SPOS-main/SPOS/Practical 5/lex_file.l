%{
%}

headerf "#".*

keyword int|void|if|else|do|while

letter [A-Za-z]
digit [0-9]+

identifier {letter}({letter}|{digit})*

punctuation [,|'|()|{}|"|;]

%%

{headerf} { printf("Header File is : %s \n", yytext); }
{keyword} { printf("Keyword Found : %s \n", yytext); }
{identifier} { printf("Identifier Found : %s \n", yytext); }
{punctuation} { printf("Punctuation Found : %s \n", yytext); }
%%
 
void main(){
	yylex();
}
int yywrap(){
	return 1;
}
