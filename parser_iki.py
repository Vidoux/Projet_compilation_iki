# -*- encoding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)


class ParsingException(Exception):
    pass


class Parser:
    def __init__(self, lexems):
        """
        Component in charge of syntaxic analysis.
        """
        self.lexems = lexems

    # ==========================
    #      Helper Functions
    # ==========================

    def accept(self):
        """
        Pops the lexem out of the lexems list.
        """
        self.show_next()
        return self.lexems.pop(0)

    def show_next(self, n=1):
        """
        Returns the next token in the list WITHOUT popping it.
        """
        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error("No more lexems left.")

    def expect(self, tag):
        """
        Pops the next token from the lexems list and tests its type through the tag.
        """
        next_lexem = self.show_next()
        if next_lexem.tag != tag:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Expected {tag}, got {next_lexem.tag} instead"
            )
        return self.accept()

    def remove_comments(self):
        """
        Removes the comments from the token list by testing their tags.
        """
        self.lexems = [lexem for lexem in self.lexems if lexem.tag != "COMMENT"]

    # ==========================
    #     Parsing Functions
    # ==========================

    def parse(self):
        """
        Main function: launches the parsing operation given a lexem list.
        """
        try:
            self.remove_comments()
            self.parse_program()
        except ParsingException as err:
            logger.exception(err)
            raise

    def parse_program(self):
        """
        Parses a program which is a succession of assignments.
        """
        self.expect("TYPE_INT")
        self.expect("KW_MAIN")
        self.expect("LEFT_PAREN")
        self.expect("RIGHT_PAREN")
        self.expect("LEFT_BRACE")
        # Your code here!

        while self.show_next().tag in ["TYPE_INT", "TYPE_BOOL", "TYPE_FLOAT", "TYPE_CHAR"]:
            self.parse_declaration()
        while self.show_next().tag in ["IDENTIFIER"]:
            self.parse_assignment()

        self.expect("RIGHT_BRACE")

    def parse_assignment(self):
        var_name = self.expect("IDENTIFIER")
        if self.show_next().tag == "ASSIGN":
            self.expect("ASSIGN")
            self.parse_expression()
        self.expect("SEMICOLON")

    def parse_declaration(self):
        var_type = self.accept()
        self.expect("IDENTIFIER")
        if self.show_next().tag == "LEFT_BRACKET":
            self.accept()
            self.expect("INTEGER")
            self.expect("RIGHT_BRACKET")
        self.expect("SEMICOLON")

    def parse_expression(self):
        print("Tanguy")
        self.parse_simple_expression()
        if self.show_next().tag in ["LESS_THAN", "GREATER_THAN", "LESS_EQUAL", "GREATER_EQUAL", "EQUAL", "NOT_EQUAL"]:
            self.accept()
            self.parse_simple_expression()

    def parse_simple_expression(self):
        self.parse_term()
        while self.show_next().tag in ["ADD", "SUB", "OR"]:
            self.accept()
            self.parse_term()

    def parse_term(self):
        self.parse_factor()
        while self.show_next().tag in ["MULT", "DIV", "MOD"]:
            self.accept()
            self.parse_factor()

    def parse_factor(self):
        if self.show_next().tag == "NOT":
            self.accept()
            self.parse_factor()
        elif self.show_next().tag in ["INTEGER", "IDENTIFIER"]:
            self.accept()
        elif self.show_next().tag == "LEFT_PAREN":
            self.accept()
            self.parse_expression()
            self.expect("RIGHT_PAREN")
        else:
            raise ParsingException(
                f"ERROR at {str(self.show_next().position)}: Unexpected token {self.show_next().tag}")
