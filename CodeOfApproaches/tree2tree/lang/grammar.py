import ast
import inspect
from collections import OrderedDict, defaultdict
import logging
from tqdm import tqdm

from lang.astnode import ASTNode
from lang.util import typename


class Grammar(object):
    def __init__(self, rules):
        """
        instantiate a grammar with a set of production rules of type Rule
        """
        self.rules = rules
        self.rule_index = defaultdict(list)
        self.rule_to_id = OrderedDict()

        node_types = set()
        lhs_nodes = set()
        rhs_nodes = set()
        print("Grammar initialization...")
        for rule in tqdm(self.rules):
            self.rule_index[rule.parent].append(rule)

            # we also store all unique node types
            for node in rule.nodes:
                node_types.add(typename(node.type))

            lhs_nodes.add(rule.parent)
            for child in rule.children:
                rhs_nodes.add(child.as_type_node)

        root_node = lhs_nodes - rhs_nodes
        assert len(root_node) == 1
        self.root_node = next(iter(root_node))

        self.terminal_nodes = rhs_nodes - lhs_nodes
        self.terminal_types = set([n.type for n in self.terminal_nodes])

        self.node_type_to_id = OrderedDict()
        for i, type in enumerate(node_types, start=0):
            self.node_type_to_id[type] = i

        for gid, rule in enumerate(rules, start=0):
            self.rule_to_id[rule] = gid

        self.id_to_rule = OrderedDict((v, k) for (k, v) in self.rule_to_id.items())

    def __iter__(self):
        return self.rules.__iter__()

    def __len__(self):
        return len(self.rules)

    def __getitem__(self, lhs):
        key_node = ASTNode(lhs.type, None)  # Rules are indexed by types only
        if key_node in self.rule_index:
            return self.rule_index[key_node]
        else:
            KeyError('key=%s' % key_node)

    def get_node_type_id(self, node):
        if isinstance(node, ASTNode):
            type_repr = typename(node.type)
            return self.node_type_to_id[type_repr]
        else:
            # assert isinstance(node, str)
            # it is a type
            type_repr = typename(node)
            return self.node_type_to_id[type_repr]

    def is_terminal(self, node):
        return node.type in self.terminal_types

    def is_value_node(self, node):
        raise NotImplementedError

NODE_FIELD_BLACK_LIST = {'ctx'}

TERMINAL_AST_TYPES = {
    ast.Pass,
    ast.Break,
    ast.Continue,
    ast.Add,
    ast.BitAnd,
    ast.BitOr,
    ast.BitXor,
    ast.Div,
    ast.FloorDiv,
    ast.LShift,
    ast.Mod,
    ast.Mult,
    ast.Pow,
    ast.Sub,
    ast.And,
    ast.Or,
    ast.Eq,
    ast.Gt,
    ast.GtE,
    ast.In,
    ast.Is,
    ast.IsNot,
    ast.Lt,
    ast.LtE,
    ast.NotEq,
    ast.NotIn,
    ast.Not,
    ast.USub
}


def is_builtin_type(x):
    return x == str or \
           x == int or \
           x == float or \
           x == bool or \
           x == bytes or \
           x == object or \
           x == 'identifier'


def is_terminal_ast_type(x):
    if inspect.isclass(x) and x in TERMINAL_AST_TYPES:
        return True

    return False


def type_str_to_type(type_str):
    if type_str.endswith('*') or type_str == 'root' or type_str == 'epsilon':
        return type_str
    else:
        try:
            type_obj = eval(type_str)
            if is_builtin_type(type_obj):
                return type_obj
        except:
            pass

        try:
            type_obj = eval('ast.' + type_str)
            return type_obj
        except:
            raise RuntimeError('unidentified type string: %s' % type_str)


def is_compositional_leaf(node):
    is_leaf = True

    for field_name, field_value in ast.iter_fields(node):
        if field_name in NODE_FIELD_BLACK_LIST:
            continue

        if field_value is None:
            is_leaf &= True
        elif isinstance(field_value, list) and len(field_value) == 0:
            is_leaf &= True
        else:
            is_leaf &= False
    return is_leaf


class PythonGrammar(Grammar):
    def __init__(self, rules):
        super(PythonGrammar, self).__init__(rules)

    def is_value_node(self, node):
        return is_builtin_type(node.type)
