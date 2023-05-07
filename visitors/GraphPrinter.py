from graphviz import Digraph


class GraphPrinter:
    def __init__(self):
        self.graph = Digraph()
        self.graph.attr(rankdir='LR')
        self.node_count = 0

    def visit_Program(self, node):
        self.graph.node(str(self.node_count), 'Program')
        self.node_count += 1
        node.block.accept(self)

    def visit_Block(self, node):
        self.graph.node(str(self.node_count), 'Block')
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1
        for statement in node.statements:
            statement.accept(self)

    def visit_Declaration(self, node):
        label = f'Declaration({node.variable.identifier_name}, {node.type_.type_name})'
        self.graph.node(str(self.node_count), label)
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1

    def visit_Assignment(self, node):
        self.graph.node(str(self.node_count), 'Assignment')
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1
        node.var_exp.accept(self)
        node.exp.accept(self)

    def visit_Read(self, node):
        self.graph.node(str(self.node_count), 'Read')
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1
        for var_exp in node.var_exps:
            var_exp.accept(self)

    def visit_Write(self, node):
        self.graph.node(str(self.node_count), 'Write')
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1
        for exp in node.exps:
            exp.accept(self)

    def visit_WhileLoop(self, node):
        self.graph.node(str(self.node_count), 'WhileLoop')
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1
        node.exp.accept(self)
        node.block.accept(self)

    def visit_BinaryOperator(self, node):
        label = f'BinaryOperator({node.operator})'
        self.graph.node(str(self.node_count), label)
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1
        node.left_operand.accept(self)
        node.right_operand.accept(self)

    def visit_UnaryOperator(self, node):
        label = f'UnaryOperator({node.operator})'
        self.graph.node(str(self.node_count), label)
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1
        node.operand.accept(self)

    def visit_Literal(self, node):
        label = f'Literal({node.value})'
        self.graph.node(str(self.node_count), label)
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1

    def visit_VarExp(self, node):
        label = f'VarExp({node.identifier.identifier_name})'
        self.graph.node(str(self.node_count), label)
        self.graph.edge(str(self.node_count-1), str(self.node_count))
        self.node_count += 1

    def visit_IfStatement(self, node):
        self.graph.node(str(self.node_count), 'IfStatement')
        self.graph.edge(str(self.node_count - 1), str(self.node_count))
        self.node_count += 1
        node.exp.accept(self)
        node.block.accept(self)
        if node.else_block:
            node.else_block.accept(self)

    def visit_Conditional(self, node):
        self.graph.node(str(self.node_count), 'Conditional')
        self.graph.edge(str(self.node_count - 1), str(self.node_count))
        self.node_count += 1
        node.true_exp.accept(self)
        node.false_exp.accept(self)

    def visit_RelationalOperator(self, node):
        label = f'RelationalOperator({node.operator})'
        self.graph.node(str(self.node_count), label)
        self.graph.edge(str(self.node_count - 1), str(self.node_count))
        self.node_count += 1
        node.left_operand.accept(self)
        node.right_operand.accept(self)

    def visit_Type(self, node):
        label = f'Type({node.type_name})'
        self.graph.node(str(self.node_count), label)
        self.graph.edge(str(self.node_count - 1), str(self.node_count))
        self.node_count += 1

