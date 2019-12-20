import os
import ast
import numpy as np

from config import parser
from utils.io import deserialize_from_file

splits = [
    'train',
    'test',
    'dev'
]


def number_of_ast_nodes_rec(node):
    return 1 + sum(map(number_of_ast_nodes_rec, ast.iter_child_nodes(node)))


def number_of_ast_nodes(code):
    root_node = ast.parse(code)
    return number_of_ast_nodes_rec(root_node)


def avg_and_max_number_of_ast_nodes(data_dir):
    nodes_numbers = []
    for split in splits:
        file = os.path.join(data_dir, '{}/{}.out.bin'.format(split, split))
        codes = deserialize_from_file(file)
        for code in codes:
            nodes_numbers.append(number_of_ast_nodes(code))

    return np.mean(nodes_numbers), max(nodes_numbers), nodes_numbers


def avg_and_max_number_char_in_code(data_dir):
    char_len = []
    for split in splits:
        file = os.path.join(data_dir, '{}/{}.out.bin'.format(split, split))
        codes = deserialize_from_file(file)
        for code in codes:
            char_len.append(len(code))

    return np.mean(char_len), max(char_len), char_len


def avg_and_max_number_of_actions(data_dir):
    nodes_numbers = []
    for split in splits:
        file = os.path.join(data_dir, '{}/{}.out.bin'.format(split, split))
        codes = deserialize_from_file(file)
        for code in codes:
            nodes_numbers.append(number_of_ast_nodes(code))

    return np.mean(nodes_numbers), max(nodes_numbers), nodes_numbers


def avg_and_max_nodes(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        count = len(lines)
        lens = [len(line.split()) for line in lines]
        max_nodes = max(lens)
        count_nodes = sum(lens)
    return count, count_nodes, max_nodes, lens


def collect_description_stats(data_dir):
    nodes = [1.e-7, 0.0]
    for split in splits:
        token_file = os.path.join(data_dir, '{}/{}.in.tokens'.format(split, split))
        count, tokens_count, tokens_max, lens = avg_and_max_nodes(token_file)
        nodes[0] += count
        nodes[1] += tokens_count
    tokens_avg = nodes[1]/nodes[0]
    return tokens_avg, tokens_max, lens


def number_of_empty_lines(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return sum([1 for l in lines if not l.strip()])


def num_syntax_parse_errors(data_dir, parents):
    errors = 0
    for split in splits:
        file = os.path.join(data_dir, '{}/{}.in.{}_parents'.format(split, split, parents))
        empty_lines = number_of_empty_lines(file)
        errors += empty_lines
    return errors


def avg_nodes_dataset(data_dir, parents):
    count, count_nodes = 0.0, 0.0
    for split in splits:
        file = os.path.join(data_dir, '{}/{}.in.{}_parents'.format(split, split, parents))
        count_, count_nodes_, max_, lens = avg_and_max_nodes(file)
        count += count_
        count_nodes += count_nodes_

    avg = count_nodes/count

    return avg, max_, lens


if __name__ == '__main__':
    args = parser.parse_args()

    tokens_avg, tokens_max, lens = collect_description_stats(args.data_dir)
    print("Avg. tokens: {},\n"
          "Max. tokens: {}.".format(tokens_avg, tokens_max))

    dependency_avg, dependency_max, dependency_lens = avg_nodes_dataset(args.data_dir, "dependency")
    pcfg_avg, pcfg_max, pcfg_lens = avg_nodes_dataset(args.data_dir, "constituency")
    ccg_avg, ccg_max, ccg_lens = avg_nodes_dataset(args.data_dir, "ccg")

    print("Average nodes in dependency trees: {}\n"
          "Average nodes in constituency trees: {}\n"
          "Average nodes in CCG trees: {}".format(dependency_avg, pcfg_avg, ccg_avg))

    print("Max nodes in dependency trees: {}\n"
          "Max nodes in constituency trees: {}\n"
          "Max nodes in CCG trees: {}".format(dependency_max, pcfg_max, ccg_max))

    dependency_errors = num_syntax_parse_errors(args.data_dir, "dependency")
    pcfg_errors = num_syntax_parse_errors(args.data_dir, "constituency")
    ccg_errors = num_syntax_parse_errors(args.data_dir, "ccg")

    print("# errors in dependency trees: {},\n"
          "# errors in constituency trees: {},\n"
          "# errors in CCG trees: {}.".format(dependency_errors, pcfg_errors, ccg_errors))


    # limit = 70
    # dependency_gt = len(list(filter(lambda l: l > limit, dependency_lens)))
    # pcfg_gt = len(list(filter(lambda l: l > limit, pcfg_lens)))
    # ccg_gt = len(list(filter(lambda l: l > limit, ccg_lens)))
    #
    # print("Number of dependency trees longer than {}: {}.".format(limit, dependency_gt))
    # print("Number of pcfg trees longer than {}: {}.".format(limit, pcfg_gt))
    # print("Number of ccg trees longer than {}: {}.".format(limit, ccg_gt))

    ast_avg, ast_max, ast_all = avg_and_max_number_of_ast_nodes(args.data_dir)

    print("Avg. number of nodes: {}.".format(ast_avg))
    print("Max. number of nodes: {}.".format(ast_max))

    char_avg, char_max, char_all = avg_and_max_number_char_in_code(args.data_dir)

    print("Avg. number of char. in code: {}.".format(char_avg))
    print("Max. number of char. in code: {}.".format(char_max))

    # actions_avg, actions_max, actions_all = avg_and_max_number_of_actions(args.data_dir)

