from scanner import Scanner
from my_parser import Parser

entrada = "funcao_simples(ident1, ident2) = ident1 OR ident2 AND ident3"
scanner = Scanner(entrada)
scanner.scan()
tokens = scanner.tokens
parser = Parser(tokens)
parser.parse()
