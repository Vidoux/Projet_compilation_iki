LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+", None),

    # Keywords
    (r"int", "TYPE_INT"),
    (r"bool", "TYPE_BOOL"),
    (r"char", "TYPE_CHAR"),
    (r"char", "TYPE_FLOAT"),
    (r"main", "KW_MAIN"),

    # Mots clef du langage
    (r'\b(char)\b', "CHAR"),

    (r'\b(else)\b', "ELSE"),
    (r'\b(if)\b', "IF"),
    (r'\b(int)\b', "INT"),

    (r'\b(while)\b', "WHILE"),


    # Ponctuation
    (r'\{', "LEFT_BRACE"),
    (r'\}', "RIGHT_BRACE"),
    (r'\(', "LEFT_PAREN"),
    (r'\)', "RIGHT_PAREN"),
    (r'\[', "LEFT_BRACKET"),
    (r'\]', "RIGHT_BRACKET"),
    (r';', "SEMICOLON"),
    (r'\+', "ADD"),
    (r'-', "SUB"),
    (r'\*', "MULT"),
    (r'/', "DIV"),
    (r'%', "MOD"),
    (r'\|', "OR"),
    (r'!', "NOT"),
    (r'=', "ASSIGN"),
    (r'<', "LESS_THAN"),
    (r'>', "GREATER_THAN"),
    (r'<=', "LESS_EQUAL"),
    (r'>=', "GREATER_EQUAL"),
    (r'==', "EQUAL"),
    (r'!=', "NOT_EQUAL"),

    # Identifiants
    (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', "IDENTIFIER"),

    # Expression
    (r'\d', "INTEGER")


]
