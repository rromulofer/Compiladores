from tokentype import TokenType
from token import Token

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
            print(f"Erro em match: Esperava {tipo_esperado}, mas obteve {self.tokens[self.index].tipo}")
            print(f"Token atual: {self.tokens[self.index].tipo}, Valor: {self.tokens[self.index].valor}")
            raise Exception(f"Erro sintático: Esperava {tipo_esperado}, mas obteve {self.tokens[self.index].tipo}")


    def funcao(self):
        if self.tokens[self.index].tipo == TokenType.IDENT and self.tokens[self.index].valor == "(":
            print(f"Token atual ao iniciar a função: {self.tokens[self.index].tipo}, Valor: {self.tokens[self.index].valor}")
            self.match(TokenType.IDENT)  # Mova esta linha para depois da verificação do parêntese aberto
            self.match("(")
            self.lista_variaveis()
            self.match(")")
            self.match("=")
            self.expressao_cond()
        else:
            self.erro(f"Esperava (, mas obteve {self.tokens[self.index].tipo}")


    def lista_variaveis(self):
        while self.tokens[self.index].tipo == TokenType.IDENT:
            self.match(TokenType.IDENT)
            if self.tokens[self.index].valor == ",":
                self.match(",")
            else:
                break

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
