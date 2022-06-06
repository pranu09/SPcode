%{
	#include<stdio.h>
	#include<stdlib.h>
	#include "y.tab.h"
%}

verbs is|am|are|do|does|did|go|went|can|could|will|would|read|write|listen
adverbs very|simply|calmly
pronouns I|He|She|They|We
conjunctions if|then|and|or|but
adjectives my|your|their|his|her
prepositions on|above|below
nouns [A-Za-z]+

%%
{pronouns} {return PRONOUN;}
{verbs} {return VERB;}
{conjunctions} {return CONJ;}
{adverbs} {return ADVERB;}
{adjectives} {return ADJECTIVE;}
{prepositions} {return PREPOSITION;}
"\n" {return NL;}
{nouns} {return NOUN;}
%%
