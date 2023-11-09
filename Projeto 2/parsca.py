from enum import Enum

class TokenType(Enum):
    IDENT = "IDENT"
    INTCONST = "INTCONST"
    REALCONST = "REALCONST"
    OPERATOR = "OPERATOR"
    KEYWORD = "KEYWORD"

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

class Scanner:
    def __init__(self, entrada):
        self.entrada = entrada
        self.tokens = []

    def scan(self):
        palavra = ""
        for char in self.entrada:
            if char.isalnum():
                palavra += char
            elif palavra:
                self.add_token(palavra)
                palavra = ""
            if char in ["(", ")", ",", "=", ">", "<", ">=", "<=", "==", "!=", "+", "-", "*", "/", "AND", "OR", "IF", "THEN", "ELSE"]:
                self.add_token(char)
        if palavra:
            self.add_token(palavra)

    def add_token(self, valor):
        if valor.isalpha():
            tipo = TokenType.IDENT
        elif valor.isdigit():
            tipo = TokenType.INTCONST
        elif "." in valor:
            tipo = TokenType.REALCONST
        elif valor in ["AND", "OR", "IF", "THEN", "ELSE"]:
            tipo = TokenType.KEYWORD
        else:
            tipo = TokenType.OPERATOR
        self.tokens.append(Token(tipo, valor))

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        try:
            self.funcao()
            print("Análise sintática bem-sucedida")
        except Exception as e:
            print(f"Erro sintático: {e}")

    def erro(self, mensagem):
        raise Exception(mensagem)

    def match(self, tipo_esperado):
        if self.index < len(self.tokens) and self.tokens[self.index].tipo == tipo_esperado:
            self.index += 1
        else:
            self.erro(f"Esperava {tipo_esperado}, mas obteve {self.tokens[self.index].tipo}")

    def funcao(self):
        self.match(TokenType.IDENT)
        self.match("(")
        self.lista_variaveis()
        self.match(")")
        self.match("=")
        self.expressao_cond()

    def lista_variaveis(self):
        self.match(TokenType.IDENT)
        while self.tokens[self.index].valor == ",":
            self.match(",")
            self.match(TokenType.IDENT)

    def expressao_cond(self):
        if self.tokens[self.index].valor == "IF":
            self.match("IF")
            self.expressao_bool()
            self.match("THEN")
            self.expressao_bool()
            self.match("ELSE")
            self.expressao_bool()
        else:
            self.expressao_bool()

    def expressao_bool(self):
        self.expressao_and()
        while self.tokens[self.index].valor == "OR":
            self.match("OR")
            self.expressao_and()

    def expressao_and(self):
        self.expressao_composta()
        while self.tokens[self.index].valor == "AND":
            self.match("AND")
            self.expressao_composta()

    def expressao_composta(self):
        self.expressao()
        if self.tokens[self.index].valor in [">", "<", ">=", "<=", "==", "!="]:
            self.match(self.tokens[self.index].valor)
            self.expressao()

    def expressao(self):
        self.termo()
        while self.tokens[self.index].valor in ["+", "-"]:
            self.match(self.tokens[self.index].valor)
            self.termo()

    def termo(self):
        self.fator()
        while self.tokens[self.index].valor in ["*", "/"]:
            self.match(self.tokens[self.index].valor)
            self.fator()

    def fator(self):
        if self.tokens[self.index].tipo == TokenType.IDENT or self.tokens[self.index].tipo in [TokenType.INTCONST, TokenType.REALCONST]:
            self.match(self.tokens[self.index].tipo)
        elif self.tokens[self.index].valor == "(":
            self.match("(")
            self.expressao_cond()
            self.match(")")
        else:
            self.erro(f"Token inesperado: {self.tokens[self.index].valor}")


# Exemplo de uso:
entrada = "minha_funcao(ident1, ident2) = ident1 OR ident2 AND ident3 > ident4 ELSE ident5"
scanner = Scanner(entrada)
scanner.scan()
tokens = scanner.tokens
parser = Parser(tokens)
parser.parse()
