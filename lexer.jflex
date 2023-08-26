import java_cup.runtime.Symbol;

%%

%class Lexer

%{
    // Código Java de inicialização, se necessário
%}

// Definição de tokens
%token <String> IDENT
%token <String> INT_LITERAL
%token <String> VOID
%token <String> WHILE
%token <String> IF
%token <String> ELSE
%token <String> RETURN
%token <String> OP_REL
%token <String> OP_ADIT
%token <String> OP_MULT
%token <String> CONTINT
%token <String> SEMICOLON
%token <String> LBRACE
%token <String> RBRACE
%token <String> LPAR
%token <String> RPAR
%token <String> COMMA

// Regras léxicas
ID = [a-zA-Z_][a-zA-Z0-9_]*
DIGIT = [0-9]
INT_LIT = {DIGIT}+
WS = [ \t\n\r]+

%%

{WS}               { /* Ignorar espaços em branco */ }

{ID}               { return new Symbol(sym.IDENT, yytext()); }

{INT_LIT}          { return new Symbol(sym.INT_LITERAL, yytext()); }

"int"              { return new Symbol(sym.INT); }
"void"             { return new Symbol(sym.VOID); }
"while"            { return new Symbol(sym.WHILE); }
"if"               { return new Symbol(sym.IF); }
"else"             { return new Symbol(sym.ELSE); }
"return"           { return new Symbol(sym.RETURN); }
">"                { return new Symbol(sym.OP_REL, yytext()); }
"<"                { return new Symbol(sym.OP_REL, yytext()); }
"<="               { return new Symbol(sym.OP_REL, yytext()); }
">="               { return new Symbol(sym.OP_REL, yytext()); }
"=="               { return new Symbol(sym.OP_REL, yytext()); }
"!="               { return new Symbol(sym.OP_REL, yytext()); }
"+"                { return new Symbol(sym.OP_ADIT, yytext()); }
"-"                { return new Symbol(sym.OP_ADIT, yytext()); }
"*"                { return new Symbol(sym.OP_MULT, yytext()); }
"/"                { return new Symbol(sym.OP_MULT, yytext()); }
"contint"          { return new Symbol(sym.CONTINT); }
";"                { return new Symbol(sym.SEMICOLON); }
"{"                { return new Symbol(sym.LBRACE); }
"}"                { return new Symbol(sym.RBRACE); }
"("                { return new Symbol(sym.LPAR); }
")"                { return new Symbol(sym.RPAR); }
","                { return new Symbol(sym.COMMA); }

.                  { /* Caractere não reconhecido */ }

%%

// Método principal para teste
public static void main(String[] args) {
    Lexer lexer = new Lexer(System.in);
    Symbol token;
    do {
        token = lexer.next_token();
        System.out.println(token);
    } while (token.sym != sym.EOF);
}