import networkx as nx


def _structural_similarity(tree1, tree2):
    sim = 1
    length = min(len(tree1.children), len(tree2.children))
    for i in range(length):
        sim += _structural_similarity(tree1.children[i], tree2.children[i])
    return sim


def structural_similarity(tree1, tree2):
    sim = _structural_similarity(tree1, tree2)
    max_size = max(tree1.size(), tree2.size())
    return sim/max_size


def read_tree(line, labels=None):
    parents = list(map(int, line.split()))
    trees = dict()
    root = None
    d = []
    for i in range(1, len(parents) + 1):
        if i - 1 not in trees.keys() and parents[i - 1] != -1:
            idx = i
            prev = None
            while True:
                parent = parents[idx - 1]
                if parent == -1:
                    break
                tree = Tree()
                d.append(tree)
                if prev is not None:
                    tree.add_child(prev)
                trees[idx - 1] = tree
                tree.idx = idx - 1
                if labels is not None:
                    tree.label = labels[tree.idx]
                else:
                    tree.label = str(tree.idx)
                if parent - 1 in trees.keys():
                    trees[parent - 1].add_child(tree)
                    break
                elif parent == 0:
                    root = tree
                    break
                else:
                    prev = tree
                    idx = parent
    if root is not None:
        root._data = d
    return root


# tree object from stanfordnlp/treelstm
class Tree(object):
    def __init__(self):
        self.parent = None
        self.num_children = 0
        self.children = list()

    def add_child(self, child):
        child.parent = self
        self.num_children += 1
        self.children.append(child)

    def size(self):
        if hasattr(self, '_size'):
            return self._size
        count = 1
        for i in range(self.num_children):
            count += self.children[i].size()
        self._size = count
        return self._size

    def data(self):
        """
        :return: list of tree nodes as a plain list
        """
        assert self._data is not None, "Only root node contains the tree list!"
        return self._data

    def depth(self):
        if getattr(self, '_depth'):
            return self._depth
        count = 0
        if self.num_children > 0:
            for i in range(self.num_children):
                child_depth = self.children[i].depth()
                if child_depth > count:
                    count = child_depth
            count += 1
        self._depth = count
        return self._depth

    def get_relations(self, rels=None):
        if rels is None:
            rels = []

        for ch in self.children:
            n1 = '(' + str(self.idx) + ') ' + self.label
            n2 = '(' + str(ch.idx) + ') ' + ch.label
            rels.append((n1, n2))
            ch.get_relations(rels)

        return rels

    def savefig(self, path):
        G = nx.DiGraph()
        G.add_edges_from(self.get_relations())
        p = nx.drawing.nx_pydot.to_pydot(G)
        p.write_png(path)
