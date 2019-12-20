import subprocess


if __name__ == '__main__':
    # subprocess.run("python main.py -dataset hs -cuda -encoder bi-lstm-dropout "
    #                "-output_dir ./results/hs/special/bilstm "
    #                "-data_dir ./preprocessed/hs", shell=True)

    # with unary closures

    subprocess.run("python main.py -dataset django -cuda -encoder bi-lstm-dropout "
                   "-unary_closures "
                   "-output_dir ./results/hs/unary_closures/ccg "
                   "-data_dir ./preprocessed/django", shell=True)
    '''

    subprocess.run("python main.py -mode validate -dataset django -cuda -encoder bi-lstm-dropout "
                   "-unary_closures "
                   "-output_dir ./results/hs/unary_closures/ccg "
                   "-data_dir ./preprocessed/django", shell=True)
    '''

'''
    subprocess.run("python main.py -dataset django -cuda -encoder bi-lstm-dropout "
                   "-unary_closures "
                   "-output_dir ./results/hs/unary_closures/bilstm "
                   "-data_dir ./preprocessed/django", shell=True)

    subprocess.run("python main.py -dataset hs -cuda -syntax dependency "
                   "-unary_closures "
                   "-output_dir ./results/hs/unary_closures/dependency "
                   "-data_dir ./preprocessed/hs", shell=True)

    subprocess.run("python main.py -dataset hs -cuda -syntax pcfg "
                   "-unary_closures "
                   "-output_dir ./results/hs/unary_closures/pcfg  "
                   "-data_dir ./preprocessed/hs", shell=True)

    subprocess.run("python main.py -dataset hs -cuda -syntax ccg "
                   "-unary_closures "
                   "-output_dir ./results/hs/unary_closures/ccg "
                   "-data_dir ./preprocessed/hs", shell=True)

    # without unary
    subprocess.run("python main.py -dataset hs -cuda -encoder bi-lstm "
                   "-no_unary_closures "
                   "-output_dir ./results/hs/no_unary_closures/bilstm "
                   "-data_dir ./preprocessed/hs", shell=True)

    subprocess.run("python main.py -dataset hs -cuda -syntax dependency "
                   "-no_unary_closures "
                   "-output_dir ./results/hs/no_unary_closures/dependency "
                   "-data_dir ./preprocessed/hs", shell=True)

    subprocess.run("python main.py -dataset hs -cuda -syntax pcfg "
                   "-no_unary_closures "
                   "-output_dir ./results/hs/no_unary_closures/pcfg "
                   "-data_dir ./preprocessed/hs", shell=True)

    subprocess.run("python main.py -dataset hs -cuda "
                   "-no_unary_closures "
                   "-output_dir ./results/hs/no_unary_closures/ccg "
                   "-data_dir ./preprocessed/hs", shell=True)
'''
