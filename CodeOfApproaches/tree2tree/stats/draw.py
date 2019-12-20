import os

from config import parser
from natural_lang.tree import *


def read_line_from_file(file, line):
    with open(file, 'r') as f:
        _ = [f.readline() for _ in range(line)]
        return f.readline()


def draw_tree(parents_path, cat_path, token_path, line, out_path):
    hs_tree_line = read_line_from_file(parents_path, line)
    hs_tokens = read_line_from_file(token_path, line).split()
    hs_categories = read_line_from_file(cat_path, line).split()

    hs_labels = []
    for i in range(len(hs_categories)):
        label = hs_categories[i]
        if len(hs_tokens) > i and label != hs_tokens[i]:
            label += ' - ' + hs_tokens[i]
        hs_labels.append(label)

    hs_tree = read_tree(hs_tree_line, hs_labels)
    hs_tree.savefig(out_path)


def draw_trees(data_dir, line, split):
    hs_tree_path = os.path.join(data_dir, '{}/{}.in.constituency_parents'.format(split, split))
    hs_category_path = os.path.join(data_dir, '{}/{}.in.constituency_categories'.format(split, split))
    hs_tokens_path = os.path.join(data_dir, '{}/{}.in.tokens'.format(split, split))
    out_path = os.path.join(data_dir, 'pcfg_tree_example_{}_{}.png'.format(split, line))

    draw_tree(hs_tree_path, hs_category_path, hs_tokens_path, line, out_path)

    hs_tree_path = os.path.join(data_dir, '{}/{}.in.dependency_parents'.format(split, split))
    hs_category_path = os.path.join(data_dir, '{}/{}.in.dependency_rels'.format(split, split))
    out_path = os.path.join(data_dir, 'dependency_tree_example_{}_{}.png'.format(split, line))

    draw_tree(hs_tree_path, hs_category_path, hs_tokens_path, line, out_path)

    hs_tree_path = os.path.join(data_dir, '{}/{}.in.ccg_parents'.format(split, split))
    hs_category_path = os.path.join(data_dir, '{}/{}.in.ccg_categories'.format(split, split))
    out_path = os.path.join(data_dir, 'ccg_tree_example_{}_{}.png'.format(split, line))

    draw_tree(hs_tree_path, hs_category_path, hs_tokens_path, line, out_path)


if __name__ == '__main__':
    args = parser.parse_args()
    draw_trees(args.data_dir, 1, 'dev')