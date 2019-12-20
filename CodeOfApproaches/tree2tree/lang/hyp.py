from lang.grammar import Grammar
from lang.astnode import DecodeTree


class Hyp:
    def __init__(self, *args):
        if isinstance(args[0], Hyp):
            hyp = args[0]
            self.grammar = hyp.grammar
            self.tree = hyp.tree.copy()
            self.t = hyp.t
            self.hist_h = list(hyp.hist_h)
            self.log = hyp.log
            self.has_grammar_error = hyp.has_grammar_error
        else:
            assert isinstance(args[0], Grammar)
            grammar = args[0]
            self.grammar = grammar
            self.tree = DecodeTree(grammar.root_node.type)
            self.t=-1
            self.hist_h = []
            self.log = ''
            self.has_grammar_error = False

        self.score = 0.0

        self.__frontier_nt = self.tree
        self.__frontier_nt_t = -1

    def __repr__(self):
        return self.tree.__repr__()

    def can_expand(self, node):
        if self.grammar.is_value_node(node):
            # if the node is finished
            if node.value is not None and node.value.endswith('<eos>'):
                return False
            return True
        elif self.grammar.is_terminal(node):
            return False

        return True

    def apply_rule(self, rule, nt=None):
        if nt is None:
            nt = self.frontier_nt()

        # assert rule.parent.type == nt.type
        if rule.parent.type != nt.type:
            self.has_grammar_error = True

        self.t += 1
        # set the time step when the rule leading by this nt is applied
        nt.t = self.t
        # record the ApplyRule action that is used to expand the current node
        nt.applied_rule = rule

        for child_node in rule.children:
            child = DecodeTree(child_node.type, child_node.label, child_node.value)

            nt.add_child(child)

    def append_token(self, token, nt=None):
        if nt is None:
            nt = self.frontier_nt()

        self.t += 1

        if nt.value is None:
            # this terminal node is empty
            nt.t = self.t
            nt.value = token
        else:
            nt.value += token

    def frontier_nt_helper(self, node):
        if node.is_leaf:
            if self.can_expand(node):
                return node
            else:
                return None

        for child in node.children:
            result = self.frontier_nt_helper(child)
            if result:
                return result
        return None

    def frontier_nt(self):
        if self.__frontier_nt_t == self.t:
            #print('a')
            #print(self.__frontier_nt)
            return self.__frontier_nt
        else:
            #print('b')
            _frontier_nt = self.frontier_nt_helper(self.tree)
            self.__frontier_nt = _frontier_nt
            self.__frontier_nt_t = self.t
            #print(_frontier_nt)
            return _frontier_nt

    def get_action_parent_t(self):
        """
        get the time step when the parent of the current
        action was generated
        WARNING: 0 will be returned if parent if None
        """
        nt = self.frontier_nt()

        if nt.parent:
            return nt.parent.t
        else:
            return 0
