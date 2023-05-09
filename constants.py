LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"--.*", "COMMENT"),
    (r"[ \t\n]+", None),

    # Keywords
    (r"var", "VAR"),
    (r"int", "TYPE_INT"),
    (r"bool", "TYPE_BOOL"),
    (r"read", "READ"),
    (r"write", "WRITE"),
    (r"while", "WHILE"),
    (r"loop", "LOOP"),
    (r"endw", "ENDW"),
    (r"true", "BOOL_LIT_TRUE"),
    (r"false", "BOOL_LIT_FALSE"),
    (r"or", "OR"),
    (r"and", "AND"),
    (r"not", "NOT"),

    # Punctuation
    (r":", "COLON"),
    (r";", "SEMICOLON"),
    (r",", "COMMA"),
    (r"\(", "LEFT_PAREN"),
    (r"\)", "RIGHT_PAREN"),
    (r"\{", "LEFT_BRACE"),
    (r"\}", "RIGHT_BRACE"),

    # Operators
    (r"=", "ASSIGNEMENT"),
    (r"\+", "ADD"),
    (r"(?<!-)-(?!-)", "SUB"),
    (r"\*", "MULT"),
    (r"/", "DIV"),
    (r"%", "MOD"),
    (r"<=", "LESS_EQUAL"),
    (r"<", "LESS_THAN"),
    (r"==", "EQUAL"),
    (r"!=", "NOT_EQUAL"),
    (r">=", "GREATER_EQUAL"),
    (r">", "GREATER_THAN"),

    # Identifiers and Literals
    (r"[a-zA-Z](_|\w)*", "IDENTIFIER"),
    (r"\d+", "INT_LIT"),

    # Expressions
    (r"true|false", "BOOL_LIT"),
    (r"and", "AND"),
    (r"or", "OR"),
    (r"not", "NOT"),

]