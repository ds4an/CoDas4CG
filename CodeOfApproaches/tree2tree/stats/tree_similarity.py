import os
import random
import numpy as np

from config import parser
from natural_lang.tree import *
from stats.draw import read_line_from_file


def test_random_similarity(file, fraction_to_test):
    with open(file, 'r') as f:
        tree_lines = f.readlines()
    length = len(tree_lines)
    to_test = int(length*fraction_to_test)
    similarity = []
    for _ in tqdm(range(to_test)):
        i1 = random.randint(0, length - 1)
        i2 = random.randint(0, length - 1)
        tree1 = read_tree(tree_lines[i1])
        tree2 = read_tree(tree_lines[i2])
        if tree1 is not None and tree2 is not None:
            sim = structural_similarity(tree1, tree2)
            similarity.append(sim)
    return similarity


if __name__ == "__main__":
    args = parser.parse_args()
    #random.seed(args.random_seed)

    # test similarity metric is valid
    file = os.path.join(args.data_dir, "dev/dev.in.ccg_parents")
    line = 2
    tree_line = read_line_from_file(file, line)
    tree = read_tree(tree_line)
    sim = structural_similarity(tree, tree)
    assert sim == 1

    # test similarity for many values
    ccg_file = os.path.join(args.data_dir, "train/train.in.ccg_parents")
    pcfg_file = os.path.join(args.data_dir, "train/train.in.constituency_parents")
    dependency_file = os.path.join(args.data_dir, "train/train.in.dependency_parents")

    ccg_sim = np.mean(test_random_similarity(ccg_file, 0.8))
    pcfg_sim = np.mean(test_random_similarity(ccg_file, 0.8))
    dependency_sim = np.mean(test_random_similarity(ccg_file, 0.8))
    print("Dependency trees similarity: {}\n"
          "PCFG trees similarity: {}\n"
          "CCG trees similarity: {}".format(dependency_sim, pcfg_sim, ccg_sim))


