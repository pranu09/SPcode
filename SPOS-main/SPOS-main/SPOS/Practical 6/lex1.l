%{
	#include<stdio.h>
	#include "y.tab.h"
%}
datatypes int|float|char
letter [A-Za-z]
digit [0-9]
idt {letter}({letter}|{digit})*
%%
{datatypes} {return TYPE;}
{idt} {return ID;}
";" {return SC;}
"," {return COMMA;}
"\n" {return NL;}
%%
