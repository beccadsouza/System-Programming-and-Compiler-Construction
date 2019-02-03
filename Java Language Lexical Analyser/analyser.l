 // Definition section of lexical analyser
%{
#include<stdio.h>
#include<string.h>
char arr[100][100];
int indx = 0, size = 0, val = 0;
 // Function to record and track identifiers encountered
int ispresent(char* s){
	for(int i = 0;i<size;i++) if(strcmp(s,arr[i])==0)return i;
	return -1;
}
%}
 // Regex for keywords,single and multiline comments, operators, literals, constants, identifiers, separators and delimiters
keyword abstract|continue|for|new|switch|assert|default|goto|package|synchronized|boolean|do|if|private|this|break|double|implements|protected|throw|byte|else|import|public|throws|case|enum|instanceof|return|transient|catch|extends|int|short|try|char|final|interface|static|void|class|finally|long|strictfp|volatile|const|float|native|super|while
comment	\/\*(.*\n)*.*\*\/|\/\/(.*)
operator [+/*\-=<>!~&\|][=]*|"<<"|">>"|"<>"|"++"|"--"|"&&"|"||"|">>>"|"<<="|">>="|">>>="
literal \"(\\.|[^"\\])*\"|true|false|null
constant [0-9]+
identifier ([A-Za-z])([A-Za-z]|[0-9])*
separator [;,.]
delimiter "("|"){"|"{"|"["|"]"|"}"

  // System|out|print([ ]?|[f]|[l][n])

%%
 // Rules section for lexical analyser
{comment}
{keyword}			{printf("[Keyword]",yytext);}
{operator}		{printf("[Operator]",yytext);}
{separator}		{printf("[Separator]",yytext);}
{delimiter}		{printf("[Delimiter]",yytext);}
{identifier}		{
				val = ispresent(yytext);
				if(val!=-1) printf("[ID%d]",val+1);
				else{
					strncpy(arr[indx],yytext,100);
		 			printf("[ID%d]",indx+1);							 			indx++;size++;						 				}
		 	}
{literal}		{printf("[String Literal]",yytext);}
{constant}		{printf("[Numeric Constant]",yytext);}
%%
 // User code section
void main() {
	yyin=fopen("main.java","r");
	yylex();
}
int yywrap(){
	return 1;
}

