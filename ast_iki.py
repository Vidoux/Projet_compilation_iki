class IKINode:
    def __init__(self):
        self.name = "IKINode"

    def accept(self, visitor, parent=None):
        method_name = 'visit_' + self.name
        visitor_method = getattr(visitor, method_name)
        return visitor_method(self, parent)


class Program(IKINode):
    def __init__(self, block):
        super().__init__()
        self.name = "Program"
        self.block = block


class Block(IKINode):
    def __init__(self, statements):
        super().__init__()
        self.name = "Block"
        self.statements = statements


class Statement(IKINode):
    def __init__(self):
        super().__init__()
        self.name = "Statement"


class Declaration(Statement):
    def __init__(self, variable, type_):
        super().__init__()
        self.name = "Declaration"
        self.variable = variable
        self.type_ = type_


class Assignment(Statement):
    def __init__(self, var_exp, exp):
        super().__init__()
        self.name = "Assignment"
        self.var_exp = var_exp
        self.exp = exp


class Read(Statement):
    def __init__(self, var_exps):
        super().__init__()
        self.name = "Read"
        self.var_exps = var_exps


class Write(Statement):
    def __init__(self, exps):
        super().__init__()
        self.name = "Write"
        self.exps = exps


class WhileLoop(Statement):
    def __init__(self, exp, block):
        super().__init__()
        self.name = "WhileLoop"
        self.exp = exp
        self.block = block


class Expression(IKINode):
    def __init__(self):
        super().__init__()
        self.name = "Expression"


class BinaryOperator(Expression):
    def __init__(self, operator, left_operand, right_operand):
        super().__init__()
        self.name = "BinaryOperator"
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand


class UnaryOperator(Expression):
    def __init__(self, operator, operand):
        super().__init__()
        self.name = "UnaryOperator"
        self.operator = operator
        self.operand = operand


class Literal(Expression):
    def __init__(self, value):
        super().__init__()
        self.name = "Literal"
        self.value = value


class VarExp(Expression):
    def __init__(self, identifier):
        super().__init__()
        self.name = "VarExp"
        self.identifier = identifier


class Identifier(IKINode):
    def __init__(self, name):
        super().__init__()
        self.name = "Identifier"
        self.identifier_name = name


class Type(IKINode):
    def __init__(self, type_name):
        super().__init__()
        self.name = "Type"
        self.type_name = type_name
