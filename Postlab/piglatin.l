 // Definition section of lexical analyser
%{
#include<stdio.h>
#include<string.h>
FILE *out;
char* vowels = "aieouAEIOU";
%}
 // Regex to differentiate between words made of letters and other text
other [ ]|[\.,;\"\']|['\n']|([A-Za-z]*[0-9]+)*
words [A-za-z]+
 // Rules section for lexical analyser
%%
{other}	{fprintf(out,"%s",yytext);}
{words}	{
				if(strchr(vowels,yytext[0])!=NULL) fprintf(out,"%cay%s",yytext[0],yytext+1);
				else fprintf(out,"%s%cay",yytext+1,yytext[0]);
				}
%%
 // User code section
void main() {
	yyin=fopen("piglatin.txt","r");
	out=fopen("buffer.txt","w");
	yylex();
	remove("piglatin.txt");
	rename("buffer.txt","piglatin.txt");
}
int yywrap(){
	return 1;
}
