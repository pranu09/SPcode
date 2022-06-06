%{
	#include<stdio.h>
	#include<stdlib.h>
	int yylex();
	int yyerror();
%}

%token PRONOUN VERB CONJ ADVERB ADJECTIVE PREPOSITION NL NOUN
 
%%
start : simple_statement NL {printf("Simple Sentence"); exit(0);}
	| compound_statement NL {printf("Compund Sentence"); exit(0);}
	;
simple_statement : subject verb object
	| subject verb object prep_noun
	;
compound_statement : simple_statement CONJ simple_statement
	| compound_statement CONJ simple_statement
	;
subject : NOUN
	| PRONOUN
	| ADJECTIVE subject
	;
verb : VERB
	| ADVERB VERB
	| verb VERB
	;
object : NOUN
	| ADJECTIVE object
	;
prep_noun : PREPOSITION NOUN
	;
%%
int main(){
	yyparse();
}
int yyerror(){
	printf("INVALID");
}
int yywrap(){
	return 1;
}
