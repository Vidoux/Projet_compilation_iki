# Hello Tanguy


from lexer import Lexer
from parser_iki import Parser
from visitors.Checker import Checker
from visitors.GraphPrinter import GraphPrinter
from visitors.PrettyPrinter import PrettyPrinter

if __name__ == "__main__":
    lexer = Lexer()
    tokens = lexer.lex_file("ressources/exemple2.iki")
    parser = Parser(tokens)
    program = parser.parse()

    pp = PrettyPrinter()
    program.accept(pp)

    ppg = GraphPrinter()
    program.accept(ppg)
    ppg.graph.render()

    #checker = Checker()
    #program.accept(checker)
