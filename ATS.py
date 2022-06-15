class AST:
    pass


class BinaryOperation(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __eq__(self, other):
        return isinstance(other, BinaryOperation) \
               and self.left == other.left \
               and self.token == other.token \
               and self.right == other.right

    def __str__(self):
        return '<BinOp ({}, {}, {})>'.format(
            repr(self.left),
            repr(self.token),
            repr(self.right)
        )

    __repr__ = __str__


class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

    def __eq__(self, other):
        return isinstance(other, UnaryOp) \
               and self.token == other.token \
               and self.expr == other.expr

    def __str__(self):
        return '<UnaryOp {}>'.format(self.token)

    __repr__ = __str__
class Number(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.literal

    def __eq__(self, other):
        return isinstance(other, Number) \
               and self.token == other.token \
               and self.value == other.value

    def __str__(self):
        return '<Number {}>'.format(self.value)

    __repr__ = __str__


class Compound(AST):
    def __init__(self):
        self.children = []

    def __eq__(self, other):
        return isinstance(other, Compound) \
               and self.children == other.children

    def __str__(self):
        return '<Compound {}>'.format(self.children)

    __repr__ = __str__


class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

    def __eq__(self, other):
        return isinstance(other, Assign) \
               and self.left == other.left \
               and self.token == other.token \
               and self.right == other.right

    def __str__(self):        return '<Assign {}={}>'.format(
            self.left,
            self.token,
            self.right
        )

    __repr__ = __str__


class Variable(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.text

    def __eq__(self, other):
        return isinstance(other, Variable) \
               and self.token == other.token \
               and self.value == other.value

    def __str__(self):
        return '<Variable {}={}>'.format(
            self.token,
            self.value
        )

    __repr = __str__


class Program(AST):
    def __init__(self, name, block):
        self.name = name
        self.block = block


class Block(AST):
    def __init__(self, declarations, compound_statement):
        self.declarations = declarations
        self.compound_statement = compound_statement


class VarDecl(AST):
    def __init__(self, var_node, type_node):
        self.var_node = var_node
        self.type_node = type_node


class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.text


class NoOp(AST):
    def __eq__(self, other):
        return isinstance(other, NoOp)

    def __str__(self):
        return '<NoOp>'

    __repr__ = __str__  
