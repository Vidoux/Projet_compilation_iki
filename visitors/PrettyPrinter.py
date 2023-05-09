class PrettyPrinter:
    def __init__(self):
        self.indentation_level = 0

    def visit_Program(self, node, parent=None):
        print("Program")
        self.indentation_level += 1
        node.block.accept(self)
        self.indentation_level -= 1

    def visit_Block(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "Block")
        self.indentation_level += 1
        for statement in node.statements:
            statement.accept(self)
        self.indentation_level -= 1

    def visit_Declaration(self, node, parent=None):
        print(
            "|" + "-" * self.indentation_level + "Declaration(" + node.variable.identifier_name + ", " + node.type_.type_name + ")")

    def visit_Assignment(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "Assignment")
        self.indentation_level += 1
        node.var_exp.accept(self)
        node.exp.accept(self)
        self.indentation_level -= 1

    def visit_Read(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "Read")
        self.indentation_level += 1
        for var_exp in node.var_exps:
            var_exp.accept(self)
        self.indentation_level -= 1

    def visit_Write(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "Write")
        self.indentation_level += 1
        for exp in node.exps:
            exp.accept(self)
        self.indentation_level -= 1

    def visit_WhileLoop(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "WhileLoop")
        self.indentation_level += 1
        node.exp.accept(self)
        node.block.accept(self)
        self.indentation_level -= 1

    def visit_BinaryOperator(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "BinaryOperator(" + node.operator + ")")
        self.indentation_level += 1
        node.left_operand.accept(self)
        node.right_operand.accept(self)
        self.indentation_level -= 1

    def visit_UnaryOperator(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "UnaryOperator(" + node.operator + ")")
        self.indentation_level += 1
        node.operand.accept(self)
        self.indentation_level -= 1

    def visit_Literal(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "Literal(" + str(node.value) + ")")

    def visit_VarExp(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "VarExp(" + node.identifier.identifier_name + ")")

    def visit_Identifier(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "Identifier(" + node.identifier_name + ")")

    def visit_Type(self, node, parent=None):
        print("|" + "-" * self.indentation_level + "Type(" + node.type_name + ")")
