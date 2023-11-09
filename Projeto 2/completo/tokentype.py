from enum import Enum

class TokenType(Enum):
    IDENT = "IDENT"
    INTCONST = "INTCONST"
    REALCONST = "REALCONST"
    OPERATOR = "OPERATOR"
    KEYWORD = "KEYWORD"
    UNKNOWN = "UNKNOWN"

