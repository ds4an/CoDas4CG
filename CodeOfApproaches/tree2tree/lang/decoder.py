import sys
import traceback
import astor

from lang.parse import decode_tree_to_python_ast


def decode_python_dataset(model, dataset):
    decode_results = []
    size = len(dataset)

    print('Decoding python dataset')
    for idx in range(size):
        enc_tree, dec_tree, input, code = dataset[idx]
        cand_list = model(enc_tree, dec_tree)

        exg_decode_results = []
        for cid, cand in enumerate(cand_list[:10]):
            try:
                ast_tree = decode_tree_to_python_ast(cand.tree)
                code = astor.to_source(ast_tree)
                exg_decode_results.append((cid, cand, ast_tree, code))
            except:
                print("Exception in converting tree to code:")
                print('-' * 60)
                print('raw_id: %d, beam pos: %d' % (idx, cid))
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)

        decode_results.append(exg_decode_results)

    return decode_results
