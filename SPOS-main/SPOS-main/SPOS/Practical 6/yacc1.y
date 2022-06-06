%{
	#include<stdio.h>
	#include<stdlib.h>
	int yylex();
	int yyerror();
%}
%token TYPE ID COMMA SC NL
%%
Start : TYPE varlist SC NL 
{printf("Valid Syntax"); 
exit(0);
}
	;
varlist : varlist COMMA ID
	| ID
	;
%%
int main(){
	yyparse();
}
int yyerror(){
	printf("Invalid Syntax");
}
int yywrap(){
	return 1;
}
