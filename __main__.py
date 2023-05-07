# Hello Tanguy

from lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer()
    print(lexer.lex_file("ressources/exemple2.iki"))
    # parser = Parser(lexer.lex_file(sys.argv[1]))
    # parser.parse()
    # print(lexer.lex_file(sys.argv[1]))