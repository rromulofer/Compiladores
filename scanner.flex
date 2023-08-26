// Importar a classe de símbolos do JavaCUP para representar os tokens
import java_cup.runtime.Symbol;

%%

// Definição da classe Lexer
%class Lexer

%{
    // Código Java de inicialização, se necessário
    // Por exemplo, importar classes necessárias aqui
%}

// Definição dos tokens
%token <String> IDENT          // Token para identificadores
%token <String> INT_LITERAL    // Token para números inteiros
%token <String> SEMICOLON      // Token para ponto e vírgula

// Definição de expressões regulares
ID = [a-zA-Z_][a-zA-Z0-9_]*     // Expressão regular para identificadores
DIGIT = [0-9]                   // Dígitos
INT_LIT = {DIGIT}+              // Expressão regular para números inteiros
WS = [ \t\n\r]+                 // Espaços em branco

%%

// Regras para ignorar espaços em branco
{WS}               { /* Ignorar espaços em branco */ }

// Regra para identificadores
{ID}               { return new Symbol(sym.IDENT, yytext()); }

// Regra para números inteiros
{INT_LIT}          { return new Symbol(sym.INT_LITERAL, yytext()); }

// Regra para ponto e vírgula
";"                { return new Symbol(sym.SEMICOLON); }

// Regra para caracteres não reconhecidos (tratamento de erro)
.                  { /* Caractere não reconhecido */ }

%%
