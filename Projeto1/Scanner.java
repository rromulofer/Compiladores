import java.io.IOException;
import java.io.InputStream;

public class Scanner {
    private InputStream in;
    private char currentChar;
    private boolean error;

    public Scanner(InputStream inputStream) {
        this.in = inputStream;
        this.error = false;
        this.currentChar = ' ';
    }

    private void nextChar() throws IOException {
        int next = in.read();
        if (next != -1) {
            currentChar = (char) next;
        } else {
            currentChar = '\0'; // Fim do arquivo
        }
    }

    public Token getNextToken() throws IOException {
        while (Character.isWhitespace(currentChar)) {
            nextChar();
        }

        if (currentChar == '\0') {
            return new Token(TokenType.EOF, "");
        }

        // Reconhecimento de tokens de acordo com a gramática

        if (currentChar == '{') {
            nextChar();
            return new Token(TokenType.LEFT_BRACE, "{");
        } else if (currentChar == '}') {
            nextChar();
            return new Token(TokenType.RIGHT_BRACE, "}");
        } else if (currentChar == '(') {
            nextChar();
            return new Token(TokenType.LEFT_PAREN, "(");
        } else if (currentChar == ')') {
            nextChar();
            return new Token(TokenType.RIGHT_PAREN, ")");
        } else if (currentChar == '[') {
            nextChar();
            return new Token(TokenType.LEFT_BRACKET, "[");
        } else if (currentChar == ']') {
            nextChar();
            return new Token(TokenType.RIGHT_BRACKET, "]");
        } else if (currentChar == ';') {
            nextChar();
            return new Token(TokenType.SEMICOLON, ";");
        } else if (currentChar == ',') {
            nextChar();
            return new Token(TokenType.COMMA, ",");
        } else if (currentChar == '=') {
            nextChar();
            if (currentChar == '=') {
                nextChar();
                return new Token(TokenType.EQUALS_EQUALS, "==");
            } else {
                return new Token(TokenType.EQUALS, "=");
            }
        } else if (currentChar == '+') {
            nextChar();
            return new Token(TokenType.PLUS, "+");
        } else if (currentChar == '-') {
            nextChar();
            return new Token(TokenType.MINUS, "-");
        } else if (currentChar == '*') {
            nextChar();
            return new Token(TokenType.MULTIPLY, "*");
        } else if (currentChar == '/') {
            nextChar();
            return new Token(TokenType.DIVIDE, "/");
        } else if (currentChar == '<') {
            nextChar();
            return new Token(TokenType.LESS_THAN, "<");
        } else if (currentChar == '>') {
            nextChar();
            return new Token(TokenType.GREATER_THAN, ">");
        } else if (currentChar == '!') {
            nextChar();
            if (currentChar == '=') {
                nextChar();
                return new Token(TokenType.NOT_EQUALS, "!=");
            } else {
                error = true;
                return new Token(TokenType.ERROR, "Erro de sintaxe: ! esperava =");
            }
        } else if (currentChar == '/') {
            nextChar();
            if (currentChar == '/') {
                // Comentário de linha, ignorar até o final da linha
                while (currentChar != '\n' && currentChar != '\0') {
                    nextChar();
                }
                return getNextToken(); // Chamada recursiva para obter o próximo token após o comentário
            } else {
               

                return new Token(TokenType.MULTIPLY, "*");
            }
        } else if (Character.isLetter(currentChar) || currentChar == '_') {
            StringBuilder identifier = new StringBuilder();
            while (Character.isLetterOrDigit(currentChar) || currentChar == '_') {
                identifier.append(currentChar);
                nextChar();
            }
            String identifierStr = identifier.toString();
            if (identifierStr.equals("int")) {
                return new Token(TokenType.INT, identifierStr);
            } else if (identifierStr.equals("void")) {
                return new Token(TokenType.VOID, identifierStr);
            } else if (identifierStr.equals("if")) {
                return new Token(TokenType.IF, identifierStr);
            } else if (identifierStr.equals("else")) {
                return new Token(TokenType.ELSE, identifierStr);
            } else if (identifierStr.equals("while")) {
                return new Token(TokenType.WHILE, identifierStr);
            } else if (identifierStr.equals("return")) {
                return new Token(TokenType.RETURN, identifierStr);
            } else {
                return new Token(TokenType.IDENTIFIER, identifierStr);
            }
        } else if (Character.isDigit(currentChar)) {
            StringBuilder number = new StringBuilder();
            while (Character.isDigit(currentChar)) {
                number.append(currentChar);
                nextChar();
            }
            return new Token(TokenType.NUMBER, number.toString());
        } else {
            error = true;
            return new Token(TokenType.ERROR, "Erro de sintaxe: Caractere não reconhecido '" + currentChar + "'");
        }

        if (currentChar == '=') {
            nextChar();
            if (currentChar == '=') {
                nextChar();
                return new Token(TokenType.EQUALS_EQUALS, "==");
            } else {
                return new Token(TokenType.EQUALS, "=");
            }
        }

        if (currentChar == '+') {
            nextChar();
            return new Token(TokenType.PLUS, "+");
        }

        if (currentChar == '-') {
            nextChar();
            return new Token(TokenType.MINUS, "-");
        }

        if (currentChar == '*') {
            nextChar();
            return new Token(TokenType.MULTIPLY, "*");
        }

        if (currentChar == '/') {
            nextChar();
            return new Token(TokenType.DIVIDE, "/");
        }

        // Adicione mais reconhecimento de tokens conforme necessário

        // Se não reconhecer nenhum token, retorne um token de erro
        return new Token(TokenType.ERROR, "Token não reconhecido: " + currentChar);
    }

    public boolean hasError() {
        return error;
    }   
}
