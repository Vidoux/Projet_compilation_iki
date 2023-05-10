import sys

from lexer import Lexer
from parser_iki import Parser
from visitors.Checker import Checker
from visitors.GraphPrinter import GraphPrinter
from visitors.PrettyPrinter import PrettyPrinter

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Veuillez fournir le nom du fichier en tant que paramètre.")
        sys.exit(1)

    try:
        file_name = sys.argv[1]
        # ------Lexer-----
        print("________Lexer_________")
        lexer = Lexer()
        tokens = lexer.lex_file(file_name)
        print("______________________")
        # ------Parser------
        print("________Parser_________")
        parser = Parser(tokens)
        program = parser.parse()
        print("_______________________")
        # ------Visiteur Checker------
        print("________Checker_________")
        checker = Checker()
        program.accept(checker)
        print("________________________")
        # ------Viteur PrettyPrinter------
        print("________PrettyPrinter_________")
        pp = PrettyPrinter()
        program.accept(pp)
        print("______________________________")
        # ------Visiteur GraphPrinter------
        # Ce visiteur génère un graph représentant l'AST
        # le fichier généré est un pdf à la racine du projet
        # nommé Digraph.gv.pdf
        ppg = GraphPrinter()
        program.accept(ppg)
        ppg.graph.render()
    except Exception as e:
        print(f"{e}")


