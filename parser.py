import ply.yacc as yacc

# Lista de tokens
tokens = (
    'IDENT',
    'INT',
    'VOID',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'ASSIGN',
    'IF',
    'ELSE',
    'WHILE',
    'RETURN',
    'GT',
    'LT',
    'LE',
    'GE',
    'EQ',
    'NE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
)

# Variável global para armazenar a tabela de símbolos
symbol_table = {}

# Definição das regras de produção
def p_programa(p):
    '''programa : declaracoes_lista'''
    pass

def p_declaracoes_lista(p):
    '''declaracoes_lista : declaracoes_lista declaracoes
                        | declaracoes'''
    pass

def p_declaracoes(p):
    '''declaracoes : declaracao_var
                | declaracao_func'''
    pass

def p_declaracao_var(p):
    '''declaracao_var : tipo IDENT SEMICOLON
                    | tipo IDENT LBRACKET contint RBRACKET SEMICOLON'''
    if len(p) == 4:
        # Ação semântica para declaração de variável simples
        symbol_table[p[2]] = {'type': p[1], 'isArray': False}
    else:
        # Ação semântica para declaração de vetor
        symbol_table[p[2]] = {'type': p[1], 'isArray': True, 'size': p[4]}

def p_tipo(p):
    '''tipo : INT
            | VOID'''
    p[0] = p[1]

# Aqui você precisa adicionar mais regras de produção para as outras partes da gramática

# Error rule for syntax errors
def p_error(p):
    print(f"Erro de sintaxe: {p}")

# Construir o analisador
parser = yacc.yacc()

# Teste com uma entrada de exemplo
data = '''
int x;
void foo(int a, int b) {
    int y[10];
}
'''

result = parser.parse(data)

# Exemplo de como acessar a tabela de símbolos após a análise
print("Tabela de Símbolos:")
for symbol, info in symbol_table.items():
    print(f"Nome: {symbol}, Tipo: {info['type']}, Array: {info['isArray']}, Tamanho: {info.get('size', '')}")
