class Checker:
    def __init__(self):
        self.symbol_table = {}

    def visit_Program(self, node, parent=None):
        node.block.accept(self)

    def visit_Block(self, node, parent=None):
        for statement in node.statements:
            statement.accept(self)

    def visit_Declaration(self, node, parent=None):
        variable_name = node.variable.identifier_name
        if variable_name in self.symbol_table:
            raise NameError(f"Variable '{variable_name}' already declared.")
        else:
            self.symbol_table[variable_name] = node.type_

    def visit_Assignment(self, node, parent=None):
        node.var_exp.accept(self)
        node.exp.accept(self)
        variable_name = node.var_exp.identifier.identifier_name
        if variable_name not in self.symbol_table:
            raise NameError(f"Variable '{variable_name}' not declared.")

    def visit_Read(self, node, parent=None):
        for var_exp in node.var_exps:
            var_exp.accept(self)
            variable_name = var_exp.identifier.identifier_name
            if variable_name not in self.symbol_table:
                raise NameError(f"Variable '{variable_name}' not declared.")

    def visit_Write(self, node, parent=None):
        for exp in node.exps:
            exp.accept(self)

    def visit_WhileLoop(self, node, parent=None):
        node.exp.accept(self)
        node.block.accept(self)

    def visit_BinaryOperator(self, node, parent=None):
        node.left_operand.accept(self)
        node.right_operand.accept(self)
        left_type = self.symbol_table.get(node.left_operand.identifier.identifier_name, None)
        right_type = self.symbol_table.get(node.right_operand.identifier.identifier_name, None)
        if left_type.type_name != right_type.type_name:
            raise TypeError(f"Type mismatch in binary operator '{node.operator}'.")
            
    def visit_UnaryOperator(self, node, parent=None):
        node.operand.accept(self)
        operand_type = self.symbol_table.get(node.operand.identifier.identifier_name, None)
        if operand_type != node.type_:
            raise TypeError(f"Type mismatch in unary operator '{node.operator}'.")
            
    def visit_Literal(self, node, parent=None):
        pass
    
    def visit_VarExp(self, node, parent=None):
        variable_name = node.identifier.identifier_name
        if variable_name not in self.symbol_table:
            raise NameError(f"Variable '{variable_name}' not declared.")