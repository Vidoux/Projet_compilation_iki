from ast_iki import *


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        self.lexems = lexems

    def accept(self):
        return self.lexems.pop(0)

    def show_next(self, n=1):
        try:
            return self.lexems[n - 1]
        except IndexError:
            raise StopIteration("No more lexems left.")

    def expect(self, tag):
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERREUR à {str(self.show_next().position)}: Attendu {tag}, obtenu {next_lexem.tag} à la place"
            )
        return self.accept()

    def remove_comments(self):
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    def parse(self):
        self.remove_comments()
        return self.parse_program()

    def parse_program(self):
        block_node = self.parse_block("main")
        return Program(block_node)

    def parse_block(self, precedent_tag):
        stmt_nodes = []
        if precedent_tag == "main":
            try:
                while True:
                    stmt_node = self.parse_stmt()
                    self.expect("SEMICOLON")
                    stmt_nodes.append(stmt_node)
            except StopIteration:
                return Block(stmt_nodes)
        if precedent_tag == "while":
            while self.show_next().tag != "ENDW":
                stmt_node = self.parse_stmt()
                self.expect("SEMICOLON")
                stmt_nodes.append(stmt_node)
        return Block(stmt_nodes)

    def parse_stmt(self):
        if self.show_next().tag == "VAR":
            return self.parse_declaration()
        elif self.show_next().tag == "IDENTIFIER":
            return self.parse_assignment()
        elif self.show_next().tag == "READ":
            return self.parse_read()
        elif self.show_next().tag == "WRITE":
            return self.parse_write()
        elif self.show_next().tag == "WHILE":
            return self.parse_while()
        else:
            raise ParsingException(
                f"ERREUR à {str(self.show_next().position)}: Symbole inattendu {self.show_next().tag}")

    def parse_declaration(self):
        self.expect("VAR")
        var_name = Identifier(self.expect("IDENTIFIER").value)
        self.expect("COLON")
        type_iki = self.accept().tag
        if type_iki == "TYPE_INT" or type_iki == "TYPE_BOOL":
            var_type = Type(type_iki)
        else:
            raise ParsingException(
                f"ERREUR à {str(self.show_next().position)}: Attendu TYPE_INT ou TYPE_BOOL, obtenu {type_iki} à la place"
            )
        return Declaration(var_name, var_type)

    def parse_assignment(self):
        var_exp = VarExp(Identifier(self.expect("IDENTIFIER").value))
        self.expect("ASSIGNEMENT")
        exp_node = self.parse_exp()
        return Assignment(var_exp, exp_node)

    def parse_read(self):
        self.expect("READ")
        var_exps = []
        var_exp = VarExp(Identifier(self.expect("IDENTIFIER").value))
        var_exps.append(var_exp)
        while self.show_next().tag == "COMMA":
            self.accept()
            var_exp = VarExp(Identifier(self.expect("IDENTIFIER").value))
            var_exps.append(var_exp)
        return Read(var_exps)

    def parse_write(self):
        self.expect("WRITE")
        exp_nodes = []
        exp_node = self.parse_exp()
        exp_nodes.append(exp_node)
        while self.show_next().tag == "COMMA":
            self.accept()
            exp_node = self.parse_exp()
            exp_nodes.append(exp_node)
        return Write(exp_nodes)

    def parse_while(self):
        self.expect("WHILE")
        cond_node = self.parse_exp()
        self.expect("LOOP")

        block_node = self.parse_block("while")

        self.expect("ENDW")
        self.expect("SEMICOLON")
        return WhileLoop(cond_node, block_node)

    def parse_exp(self):
        return self.parse_exp1()

    def parse_exp1(self):
        left = self.parse_exp2()
        while self.show_next().tag == "OR":
            op = self.expect("OR").value
            right = self.parse_exp2()
            left = BinaryOperator(op, left, right)
        return left

    def parse_exp2(self):
        left = self.parse_exp3()
        while self.show_next().tag == "AND":
            op = self.expect("AND").value
            right = self.parse_exp3()
            left = BinaryOperator(op, left, right)
        return left

    def parse_exp3(self):
        left = self.parse_exp4()
        if self.show_next().tag in ["LESS_EQUAL", "LESS_THAN", "EQUAL", "NOT_EQUAL", "GREATER_EQUAL", "GREATER_THAN"]:
            op = self.accept().value
            right = self.parse_exp4()
            left = BinaryOperator(op, left, right)
        return left

    def parse_exp4(self):
        left = self.parse_exp5()
        while self.show_next().tag in ["ADD", "SUB"]:
            op = self.accept().value
            right = self.parse_exp5()
            left = BinaryOperator(op, left, right)
        return left

    def parse_exp5(self):
        left = self.parse_exp6()
        while self.show_next().tag in ["MULT", "DIV", "MOD"]:
            op = self.expect("MULOP").value
            right = self.parse_exp6()
            left = BinaryOperator(op, left, right)
        return left

    def parse_exp6(self):
        if self.show_next().tag == "NOT":
            op = self.expect("NOT").value
            exp_node = self.parse_exp6()
            return UnaryOperator(op, exp_node)
        else:
            return self.parse_exp7()

    def parse_exp7(self):
        if self.show_next().tag == "BOOL_LIT_TRUE":
            return Literal(True)
        elif self.show_next().tag == "BOOL_LIT_FALSE":
            return Literal(False)
        elif self.show_next().tag == "INT_LIT":
            return Literal(int(self.expect("INT_LIT").value))
        elif self.show_next().tag == "LEFT_PAREN":
            self.expect("LEFT_PAREN")
            exp_node = self.parse_exp()
            self.expect("RIGHT_PAREN")
            return exp_node
        elif self.show_next().tag == "IDENTIFIER":
            return self.parse_var_exp()
        else:
            raise ParsingException(
                f"ERREUR à {str(self.show_next().position)}: Symbole inattendu {self.show_next().tag}")

    def parse_var_exp(self):
        var_exp = VarExp(Identifier(self.expect("IDENTIFIER").value))
        if self.show_next().tag == "LEFT_BRACKET":
            self.expect("LEFT_BRACKET")
            index_exp = self.parse_exp()
            self.expect("RIGHT_BRACKET")
            return VarExp(var_exp.identifier, index_exp)
        return var_exp
