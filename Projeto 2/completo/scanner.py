from token import Token, TokenType

class Scanner:
    def __init__(self, entrada):
        self.entrada = entrada
        self.tokens = []

    def scan(self):
        palavra = ""
        for char in self.entrada:
            if char.isalnum() or char == "_":
                palavra += char
            elif palavra:
                self.add_token(palavra)
                palavra = ""
            if char in ["(", ")", ",", "=", ">", "<", ">=", "<=", "==", "!=", "+", "-", "*", "/"]:
                self.add_token(char)

        # Adiciona o último token, se houver
        if palavra:
            self.add_token(palavra)

        # Atualiza os tokens desconhecidos para TokenType.IDENT, se necessário
        for i in range(len(self.tokens)):
            if self.tokens[i].tipo == TokenType.UNKNOWN and self.tokens[i].valor.isalpha():
                self.tokens[i].tipo = TokenType.IDENT

        # Imprime os tokens gerados
        print("Tokens gerados:")
        for token in self.tokens:
            print(f"Tipo: {token.tipo}, Valor: {token.valor}")


    def add_token(self, valor):
        if valor.isalpha():
            tipo = TokenType.IDENT if valor != "funcao_simples" else TokenType.KEYWORD
        elif valor.isdigit():
            tipo = TokenType.INTCONST
        elif valor in ["(", ")", ",", "=", ">", "<", ">=", "<=", "==", "!=", "+", "-", "*", "/"]:
            tipo = TokenType.OPERATOR
        elif valor in ["AND", "OR", "IF", "THEN", "ELSE"]:
            tipo = TokenType.KEYWORD
        else:
            tipo = TokenType.IDENT  # Trata todas as outras palavras como identificadores
        self.tokens.append(Token(tipo, valor))







