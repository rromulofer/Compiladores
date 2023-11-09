class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def analisar(self):
        try:
            self.funcao()
            print("Análise sintática bem-sucedida")
        except Exception as e:
            print(f"Erro sintático: {e}")

    def erro(self, mensagem):
        raise Exception(mensagem)

    def match(self, token_esperado):
        if self.index < len(self.tokens) and self.tokens[self.index] == token_esperado:
            self.index += 1
        else:
            self.erro(f"Esperava {token_esperado}, mas obteve {self.tokens[self.index]}")

    def funcao(self):
        self.match("IDENT")
        self.match("(")
        self.lista_variaveis()
        self.match(")")
        self.match("=")
        self.expressao_cond()

    def lista_variaveis(self):
        self.match("IDENT")
        while self.tokens[self.index] == ",":
            self.match(",")
            self.match("IDENT")

    def expressao_cond(self):
        if self.tokens[self.index] == "IF":
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
        while self.tokens[self.index] == "OR":
            self.match("OR")
            self.expressao_and()

    def expressao_and(self):
        self.expressao_composta()
        while self.tokens[self.index] == "AND":
            self.match("AND")
            self.expressao_composta()

    def expressao_composta(self):
        self.expressao()
        if self.tokens[self.index] in [">", "<", ">=", "<=", "==", "!="]:
            self.match(self.tokens[self.index])
            self.expressao()

    def expressao(self):
        self.termo()
        while self.tokens[self.index] in ["+", "-"]:
            self.match(self.tokens[self.index])
            self.termo()

    def termo(self):
        self.fator()
        while self.tokens[self.index] in ["*", "/"]:
            self.match(self.tokens[self.index])
            self.fator()

    def fator(self):
        if self.tokens[self.index] == "IDENT" or self.tokens[self.index] in ["INTCONST", "REALCONST"]:
            self.match(self.tokens[self.index])
        elif self.tokens[self.index] == "(":
            self.match("(")
            self.expressao_cond()
            self.match(")")
        else:
            self.erro(f"Token inesperado: {self.tokens[self.index]}")


# Exemplo de uso:
tokens = ["IDENT", "(", "IDENT", ",", "IDENT", ")", "=", "IDENT", "OR", "IDENT", "AND", "IDENT", ">", "IDENT", "ELSE", "IDENT"]
analisador = AnalisadorSintatico(tokens)
analisador.analisar()
