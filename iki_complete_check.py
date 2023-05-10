from lexer import Lexer
from parser_iki import Parser
from visitors.Checker import Checker
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez fournir le nom du fichier en tant que paramètre.")
        sys.exit(1)
        
    try:
        file_name = sys.argv[1]
        lexer = Lexer()
        tokens = lexer.lex_file(file_name)
        parser = Parser(tokens)
        program = parser.parse()
        checker = Checker()
        program.accept(checker)
        
    except Exception as e:
        print(f"{e}")   


