


# class GraphPrinter:
#     def __init__(self):
#         import graphviz
#         self.graph = graphviz.Digraph()
#         self.node_counter = 0
#
#     def visit_Program(self, node):
#         self.graph.node(str(self.node_counter), "Program")
#         self.node_counter += 1
#         node.block.accept(self)
#
#     def visit_Block(self, node):
#         self.graph.node(str(self.node_counter), "Block")
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         parent = self.node_counter
#         self.node_counter += 1
#         for statement in node.statements:
#             statement.accept(self)
#         self.graph.edge(str(parent), str(self.node_counter - 1))
#
#     def visit_Declaration(self, node):
#         self.graph.node(str(self.node_counter), "Declaration")
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         self.node_counter += 1
#
#     def visit_Assignment(self, node):
#         self.graph.node(str(self.node_counter), "Assignment")
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         parent = self.node_counter
#         self.node_counter += 1
#         node.var_exp.accept(self)
#         node.exp.accept(self)
#         self.graph.edge(str(parent), str(self.node_counter - 2))
#         self.graph.edge(str(parent), str(self.node_counter - 1))
#
#     def visit_Read(self, node):
#         self.graph.node(str(self.node_counter), "Read")
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         parent = self.node_counter
#         self.node_counter += 1
#         for var_exp in node.var_exps:
#             var_exp.accept(self)
#         self.graph.edge(str(parent), str(self.node_counter - 1))
#
#     def visit_Write(self, node):
#         self.graph.node(str(self.node_counter), "Write")
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         parent = self.node_counter
#         self.node_counter += 1
#         for exp in node.exps:
#             exp.accept(self)
#         self.graph.edge(str(parent), str(self.node_counter - 1))
#
#     def visit_WhileLoop(self, node):
#         self.graph.node(str(self.node_counter), "WhileLoop")
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         parent = self.node_counter
#         self.node_counter += 1
#         node.exp.accept(self)
#         node.block.accept(self)
#         self.graph.edge(str(parent), str(self.node_counter - 2))
#         self.graph.edge(str(parent), str(self.node_counter - 1))
#
#     def visit_BinaryOperator(self, node):
#         self.graph.node(str(self.node_counter), "BinaryOperator " + node.operator)
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         parent = self.node_counter
#         self.node_counter += 1
#         node.left_operand.accept(self)
#         node.right_operand.accept(self)
#         self.graph.edge(str(parent), str(self.node_counter - 2))
#         self.graph.edge(str(parent), str(self.node_counter - 1))
#
#     def visit_UnaryOperator(self, node):
#         self.graph.node(str(self.node_counter), "UnaryOperator " + node.operator)
#         self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
#         parent = self.node_counter
#         self.node_counter += 1
#         node.operand.accept(self)
#         self.graph.edge(str(parent), str(self.node_counter - 1))
#
#     def visit_Literal(self, node):
#         self.graph.node(str(self.node_counter), "Literal " + str(node.value))
#         parent = self.node_counter
#         self.node_counter += 1
#
#
#     def visit_VarExp(self, node):
#         self.graph.node(str(self.node_counter), "VarExp " + node.identifier.identifier_name)
#         parent = self.node_counter
#         self.node_counter += 1
#
#
#     def visit_Identifier(self, node):
#         self.graph.node(str(self.node_counter), "Identifier " + node.identifier_name)
#         parent = self.node_counter
#         self.node_counter += 1
from graphviz import Digraph


class GraphPrinter:
    def __init__(self):
        self.graph = Digraph()
        self.node_counter = 0

    def visit_Program(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "Program")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        node.block.accept(self, current_node_id)

    def visit_Block(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "Block")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        for statement in node.statements:
            statement.accept(self, current_node_id)

    def visit_Declaration(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "Declaration(" + node.variable.identifier_name + ", " + node.type_.type_name + ")")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)

    def visit_Assignment(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "Assignment")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        node.var_exp.accept(self, current_node_id)
        node.exp.accept(self, current_node_id)

    def visit_Read(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "Read")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        for var_exp in node.var_exps:
            var_exp.accept(self, current_node_id)

    def visit_Write(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "Write")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        for exp in node.exps:
            exp.accept(self, current_node_id)


    def visit_WhileLoop(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "WhileLoop")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        node.exp.accept(self, current_node_id)
        node.block.accept(self, current_node_id)

    def visit_BinaryOperator(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, node.operator)
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        node.left_operand.accept(self, current_node_id)
        node.right_operand.accept(self, current_node_id)

    def visit_UnaryOperator(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, node.operator)
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        node.factor.accept(self, current_node_id)

    def visit_Literal(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, str(node.value))
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)

    def visit_VarExp(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, "VarExp")
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)
        node.identifier.accept(self, current_node_id)

    def visit_Identifier(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, node.identifier_name)
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)

    def visit_Type(self, node, parent=None):
        current_node_id = str(self.node_counter)
        self.graph.node(current_node_id, node.type_name)
        self.node_counter += 1
        if parent is not None:
            self.graph.edge(parent, current_node_id)


    # def visit_Program(self, node):
    #     self.graph.node(str(self.node_counter), "Program")
    #     self.node_counter += 1
    #     node.block.accept(self)
    #
    # def visit_Block(self, node):
    #     self.graph.node(str(self.node_counter), "Block")
    #     parent = self.node_counter
    #     self.node_counter += 1
    #     if parent is not None:
    #         self.graph.edge(parent, self.node_counter)
    #     for statement in node.statements:
    #         statement.accept(self)
    #         self.graph.edge(str(parent), str(self.node_counter - 1))
    #
    # def visit_Declaration(self, node):
    #     self.graph.node(str(self.node_counter), "Declaration")
    #     self.graph.edge(str(self.node_counter), str(self.node_counter - 1))
    #     self.node_counter += 1
    #
    # def visit_Assignment(self, node):
    #     self.graph.node(str(self.node_counter), "Assignment")
    #     parent = self.node_counter
    #     self.node_counter += 1
    #     node.var_exp.accept(self)
    #     node.exp.accept(self)
    #     self.graph.edge(str(parent), str(self.node_counter - 2))
    #     self.graph.edge(str(parent), str(self.node_counter - 1))
    #
    # def visit_Read(self, node):
    #     self.graph.node(str(self.node_counter), "Read")
    #     parent = self.node_counter
    #     self.node_counter += 1
    #     for var_exp in node.var_exps:
    #         var_exp.accept(self)
    #         self.graph.edge(str(parent), str(self.node_counter - 1))
    #
    # def visit_Write(self, node):
    #     self.graph.node(str(self.node_counter), "Write")
    #     parent = self.node_counter
    #     self.node_counter += 1
    #     for exp in node.exps:
    #         exp.accept(self)
    #         self.graph.edge(str(parent), str(self.node_counter - 1))
    #
    # def visit_WhileLoop(self, node):
    #     self.graph.node(str(self.node_counter), "WhileLoop")
    #     parent = self.node_counter
    #     self.node_counter += 1
    #     node.exp.accept(self)
    #     node.block.accept(self)
    #     self.graph.edge(str(parent), str(self.node_counter - 2))
    #     self.graph.edge(str(parent), str(self.node_counter - 1))
    #
    # def visit_BinaryOperator(self, node):
    #     self.graph.node(str(self.node_counter), "BinaryOperator " + node.operator)
    #     parent = self.node_counter
    #     self.node_counter += 1
    #     node.left_operand.accept(self)
    #     node.right_operand.accept(self)
    #     self.graph.edge(str(parent), str(self.node_counter - 2))
    #     self.graph.edge(str(parent), str(self.node_counter - 1))
    #
    # def visit_UnaryOperator(self, node):
    #     self.graph.node(str(self.node_counter), "UnaryOperator " + node.operator)
    #     parent = self.node_counter
    #     self.node_counter += 1
    #     node.operand.accept(self)
    #     self.graph.edge(str(parent), str(self.node_counter - 1))
    #
    # def visit_Literal(self, node):
    #     self.graph.node(str(self.node_counter), "Literal " + str(node.value))
    #     self.node_counter += 1
    #
    # def visit_VarExp(self, node):
    #     self.graph.node(str(self.node_counter), "VarExp " + node.identifier.identifier_name)
    #     self.node_counter += 1
    #
    # def visit_Identifier(self, node):
    #     self.graph.node(str(self.node_counter), "Identifier " + node.identifier_name)
    #     self.node_counter += 1
    #
    # def visit_Type(self, node):
    #     self.graph.node(str(self.node_counter), "Type " + node.type_name)
    #     self.node_counter += 1
    #

# class GraphPrinter:
#     def __init__(self):
#         self.graph = Digraph()
#         self.graph.attr(rankdir='TB')
#         self.node_count = 0
#         self.current_node = None
#         # Initialisation de la liste des IDs de nœuds
#         self.node_ids = {}
#
#
#     def get_id(self, node):
#         if node not in self.node_ids:
#             self.node_ids[node] = str(len(self.node_ids))
#         return self.node_ids[node]
#
#     def visit_Program(self, node):
#         # Le nœud Program doit être la racine de l'arbre et il ne peut y avoir qu'un seul Program.
#         node.accept(self)
#
#     def visit_Block(self, node):
#         # Ajout d'un appel à self.graph.edge() pour relier le nœud Block à son parent
#         if self.current_node is not None:
#             self.graph.edge(str(self.current_node), str(self.get_id(node)), label="block")
#         # Itération sur chaque instruction dans le bloc et appel de statement.accept(self) pour générer des
#         # sous-arbres pour chaque instruction
#         for statement in node.statements:
#             statement.accept(self)
#
#     def visit_Declaration(self, node):
#         # Ajout d'un appel à self.graph.edge() pour relier le nœud Declaration à son parent.
#         self.graph.edge(str(self.current_node), str(self.get_id(node)), label=node.var_id.name)
#
#     def visit_Assignment(self, node):
#         # Ajout d'un appel à self.graph.edge() pour relier le nœud Assignment à son parent
#         self.graph.edge(str(self.current_node), str(self.get_id(node)), label="=")
#         # Appeler node.var_exp.accept(self) et node.exp.accept(self) pour générer des sous-arbres pour la variable et l'expression
#         node.var_exp.accept(self)
#         node.exp.accept(self)
#
#     def visit_Read(self, node):
#         self.graph.node(str(self.node_count), 'Read')
#         self.graph.edge(str(self.node_count-1), str(self.node_count))
#         self.node_count += 1
#         for var_exp in node.var_exps:
#             var_exp.accept(self)
#
#     def visit_Write(self, node):
#         self.graph.node(str(self.node_count), 'Write')
#         self.graph.edge(str(self.node_count-1), str(self.node_count))
#         self.node_count += 1
#         for exp in node.exps:
#             exp.accept(self)
#
#     def visit_WhileLoop(self, node):
#         self.graph.node(str(self.node_count), 'WhileLoop')
#         self.node_count += 1
#
#         # Create a node for the condition and add it as a child of the WhileLoop node
#         self.graph.node(str(self.node_count), 'Condition')
#         self.graph.edge(str(self.node_count - 1), str(self.node_count))
#         self.node_count += 1
#         node.exp.accept(self)
#
#         # Create a node for the loop block and add it as a child of the WhileLoop node
#         self.graph.node(str(self.node_count), 'LoopBlock')
#         self.graph.edge(str(self.node_count - 2), str(self.node_count))
#         self.node_count += 1
#         node.block.accept(self)
#
#     def visit_BinaryOperator(self, node):
#         label = f'BinaryOperator({node.operator})'
#         self.graph.node(str(self.node_count), label)
#         self.graph.edge(str(self.node_count-1), str(self.node_count))
#         self.node_count += 1
#         node.left_operand.accept(self)
#         node.right_operand.accept(self)
#
#     def visit_UnaryOperator(self, node):
#         label = f'UnaryOperator({node.operator})'
#         self.graph.node(str(self.node_count), label)
#         self.graph.edge(str(self.node_count-1), str(self.node_count))
#         self.node_count += 1
#         node.operand.accept(self)
#
#     def visit_Literal(self, node):
#         label = f'Literal({node.value})'
#         self.graph.node(str(self.node_count), label)
#         self.graph.edge(str(self.node_count-1), str(self.node_count))
#         self.node_count += 1
#
#     def visit_VarExp(self, node):
#         label = f'VarExp({node.identifier.identifier_name})'
#         self.graph.node(str(self.node_count), label)
#         self.graph.edge(str(self.node_count-1), str(self.node_count))
#         self.node_count += 1
#
#     def visit_Identifier(self, identifier):
#         identifier_node_name = "Identifier_" + str(id(identifier))
#         self.graph.node(identifier_node_name, str(identifier.identifier_name))
#         return identifier_node_name
#
#     def visit_Type(self, type_):
#         type_node_name = "Type_" + str(id(type_))
#         self.graph.node(type_node_name, str(type_.type_name))
#         return type_node_name
