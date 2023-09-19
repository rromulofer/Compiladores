import ply.yacc as yacc

# Lista de tokens
tokens = (
    'IDENT',
    'INT_LITERAL',
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

# Definição das regras de precedência
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE'),
    # Outras precedências aqui
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

# Continuaremos adicionando mais regras de produção nas mensagens subsequentes.
# Continuação das regras de produção

def p_declaracao_func(p):
    '''declaracao_func : tipo IDENT LPAREN par_formais RPAREN decl_composto'''
    # Ação semântica para declaração de função
    symbol_table[p[2]] = {'type': p[1], 'params': p[4]}

def p_par_formais(p):
    '''par_formais : lista_par_formais
                |'''
    if len(p) == 1:
        p[0] = []  # Nenhum parâmetro
    else:
        p[0] = p[1]

def p_lista_par_formais(p):
    '''lista_par_formais : parametro COMMA lista_par_formais
                    | parametro'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_parametro(p):
    '''parametro : tipo IDENT
                | tipo IDENT LBRACKET RBRACKET'''
    if len(p) == 3:
        p[0] = {'type': p[1], 'name': p[2], 'isArray': False}
    else:
        p[0] = {'type': p[1], 'name': p[2], 'isArray': True}

def p_decl_composto(p):
    '''decl_composto : LBRACE declaracoes_locais lista_comandos RBRACE'''
    # Ação semântica para declarações compostas

def p_declaracoes_locais(p):
    '''declaracoes_locais : declaracoes_locais declaracao_var
                        |'''
    # Ação semântica para declarações locais

def p_lista_comandos(p):
    '''lista_comandos : lista_comandos comando
                    |'''
    # Ação semântica para lista de comandos

def p_comando(p):
    '''comando : comando_expressao
            | comando_composto
            | comando_selecao
            | comando_iteracao
            | comando_retorno
            | SEMICOLON'''
    # Ação semântica para comandos

def p_comando_expressao(p):
    '''comando_expressao : expressao SEMICOLON
                    | SEMICOLON'''
    # Ação semântica para comando de expressão

# Continuaremos adicionando mais regras de produção nas mensagens seguintes.
# Continuação das regras de produção

def p_comando_composto(p):
    '''comando_composto : LBRACE declaracoes_locais lista_comandos RBRACE'''
    # Ação semântica para comando composto

def p_comando_selecao(p):
    '''comando_selecao : IF LPAREN expressao RPAREN comando
                    | IF LPAREN expressao RPAREN comando ELSE comando'''
    # Ação semântica para comando de seleção

def p_comando_iteracao(p):
    '''comando_iteracao : WHILE LPAREN expressao RPAREN comando'''
    # Ação semântica para comando de iteração

def p_comando_retorno(p):
    '''comando_retorno : RETURN SEMICOLON
                    | RETURN expressao SEMICOLON'''
    # Ação semântica para comando de retorno

def p_expressao(p):
    '''expressao : var ASSIGN expressao
                | expressao_simples'''
    # Ação semântica para expressão

def p_var(p):
    '''var : IDENT
            | IDENT LBRACKET expressao RBRACKET'''
    # Ação semântica para variável

def p_expressao_simples(p):
    '''expressao_simples : expressao_simples op_relacional termo
                    | termo'''
    # Ação semântica para expressão simples

def p_op_relacional(p):
    '''op_relacional : GT
                     | LT
                     | LE
                     | GE
                     | EQ
                     | NE'''
    # Ação semântica para operador relacional

def p_termo(p):
    '''termo : termo op_aditivo fator
            | fator'''
    # Ação semântica para termo

def p_op_aditivo(p):
    '''op_aditivo : PLUS
                | MINUS'''
    # Ação semântica para operador aditivo

def p_fator(p):
    '''fator : LPAREN expressao RPAREN
            | var
            | INT_LITERAL'''
    # Ação semântica para fator

# Continuaremos adicionando mais regras de produção nas próximas mensagens.
# Continuação das regras de produção

def p_expressao_chamada_funcao(p):
    '''expressao : IDENT LPAREN args RPAREN'''
    # Ação semântica para expressão de chamada de função

def p_args(p):
    '''args : lista_args
            |'''
    # Ação semântica para argumentos

def p_lista_args(p):
    '''lista_args : lista_args COMMA expressao
                | expressao'''
    # Ação semântica para lista de argumentos

# Continuaremos adicionando mais regras de produção nas próximas mensagens.
# Continuação das regras de produção

def p_op_mult(p):
    '''op_mult : TIMES
              | DIVIDE'''
    # Ação semântica para operador de multiplicação/divisão

def p_termo(p):
    '''termo : termo op_mult fator
            | fator'''
    # Ação semântica para termo

def p_fator(p):
    '''fator : LPAREN expressao RPAREN
            | var
            | INT_LITERAL'''
    # Ação semântica para fator

def p_expressao_simples(p):
    '''expressao_simples : expressao_simples op_relacional termo
                        | termo'''
    # Ação semântica para expressão simples

# Continuaremos adicionando mais regras de produção nas próximas mensagens.
# Continuação das regras de produção

def p_comando_expressao(p):
    '''comando_expressao : expressao SEMICOLON
                        | var ASSIGN expressao SEMICOLON'''
    # Ação semântica para comando de atribuição

def p_comando_composto(p):
    '''comando_composto : LBRACE declaracoes_locais lista_comandos RBRACE'''
    # Ação semântica para comando composto

def p_declaracoes_locais(p):
    '''declaracoes_locais : declaracoes_locais declaracao_var
                        |'''
    # Ação semântica para declarações locais

def p_lista_comandos(p):
    '''lista_comandos : lista_comandos comando
                    |'''
    # Ação semântica para lista de comandos

# Continuaremos adicionando mais regras de produção nas próximas mensagens.
# Continuação das regras de produção

def p_comando_selecao(p):
    '''comando_selecao : IF LPAREN expressao RPAREN comando
                    | IF LPAREN expressao RPAREN comando ELSE comando'''
    # Ação semântica para comando de seleção

def p_comando_iteracao(p):
    '''comando_iteracao : WHILE LPAREN expressao RPAREN comando'''
    # Ação semântica para comando de iteração

# Continuaremos adicionando mais regras de produção nas próximas mensagens.
# Continuação das regras de produção

def p_comando_retorno(p):
    '''comando_retorno : RETURN SEMICOLON
                    | RETURN expressao SEMICOLON'''
    # Ação semântica para comando de retorno

def p_programa(p):
    '''programa : declaracoes_lista'''
    # Ação semântica para o programa