from ast_iki import *
from visitors.GraphPrinter import GraphPrinter
from visitors.PrettyPrinter import PrettyPrinter


if __name__ == "__main__":
    # Instanciation de l'objet Program
    block = Block([
        Declaration(Identifier("x"), Type("int")),
        Declaration(Identifier("y"), Type("int")),
        WhileLoop(
            BinaryOperator("-", VarExp(Identifier("y")), Literal(5)),
            Block([
                Declaration(Identifier("y"), Type("int")),
                Read([VarExp(Identifier("x")), VarExp(Identifier("y"))]),
                Assignment(
                    VarExp(Identifier("x")),
                    BinaryOperator("*", Literal(2), BinaryOperator("+", Literal(3), VarExp(Identifier("y"))))
                )
            ])
        ),
        Write([Literal(5)])
    ])
    program = Program(block)

    # pp = PrettyPrinter()
    # program.accept(pp)
    ppg = GraphPrinter()
    program.accept(ppg)
    ppg.graph.render();
