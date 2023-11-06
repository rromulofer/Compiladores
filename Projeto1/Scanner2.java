import java.io.IOException;
import java.io.InputStream;

public class Scanner2 {
    private InputStream in;
    private char currentChar;
    private boolean error;

    public Scanner2(InputStream inputStream) {
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

        // Reconhecimento de tokens comuns
        switch (currentChar) {
            case '{':
                nextChar();
                return new Token(TokenType.LEFT_BRACE, "{");
            case '}':
                nextChar();
                return new Token(TokenType.RIGHT_BRACE, "}");
            case '(':
                nextChar();
                return new Token(TokenType.LEFT_PAREN, "(");
            case ')':
                nextChar();
                return new Token(TokenType.RIGHT_PAREN, ")");
            case '[':
                nextChar();
                return new Token(TokenType.LEFT_BRACKET, "[");
            case ']':
                nextChar();
                return new Token(TokenType.RIGHT_BRACKET, "]");
            case ';':
                nextChar();
                return new Token(TokenType.SEMICOLON, ";");
            case ',':
                nextChar();
                return new Token(TokenType.COMMA, ",");
            case '=':
                nextChar();
                if (currentChar == '=') {
                    nextChar();
                    return new Token(TokenType.EQUALS_EQUALS, "==");
                }
                return new Token(TokenType.EQUALS, "=");
            case '+':
                nextChar();
                return new Token(TokenType.PLUS, "+");
            case '-':
                nextChar();
                return new Token(TokenType.MINUS, "-");
            case '*':
                nextChar();
                return new Token(TokenType.MULTIPLY, "*");
            case '/':
                nextChar();
                return new Token(TokenType.DIVIDE, "/");
            case '<':
                nextChar();
                return new Token(TokenType.LESS_THAN, "<");
            case '>':
                nextChar();
                return new Token(TokenType.GREATER_THAN, ">");
            case '!':
                nextChar();
                if (currentChar == '=') {
                    nextChar();
                    return new Token(TokenType.NOT_EQUALS, "!=");
                } else {
                    error = true;
                    return new Token(TokenType.ERROR, "Erro de sintaxe: ! esperava =");
                }
            default:
                // Verifique se é um identificador ou número
                if (Character.isLetter(currentChar) || currentChar == '_') {
                    StringBuilder identifier = new StringBuilder();
                    while (Character.isLetterOrDigit(currentChar) || currentChar == '_') {
                        identifier.append(currentChar);
                        nextChar();
                    }
                    String identifierStr = identifier.toString();
                    switch (identifierStr) {
                        case "int":
                            return new Token(TokenType.INT, identifierStr);
                        case "void":
                            return new Token(TokenType.VOID, identifierStr);
                        case "if":
                            return new Token(TokenType.IF, identifierStr);
                        case "else":
                            return new Token(TokenType.ELSE, identifierStr);
                        case "while":
                            return new Token(TokenType.WHILE, identifierStr);
                        case "return":
                            return new Token(TokenType.RETURN, identifierStr);
                        default:
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
        }
    }

    public boolean hasError() {
        return error;
    }
}

