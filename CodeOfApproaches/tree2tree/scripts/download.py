from __future__ import print_function
import sys
import os
import zipfile
import tarfile
import requests


def download(url, dirpath):
    filename = url.split('/')[-1]
    filepath = os.path.join(dirpath, filename)
    try:
        u = requests.get(url)
    except:
        print("URL %s failed to open" %url)
        raise Exception
    try:
        f = open(filepath, 'wb')
    except:
        print("Cannot write %s" %filepath)
        raise Exception

    downloaded = 0
    for buf in u.iter_content(100000):
        if not buf:
            print('')
            break
        else:
            print('', end='\r')
        downloaded += len(buf)
        f.write(buf)
    f.close()
    return filepath


def unzip(filepath):
    print("Extracting: " + filepath)
    dirpath = os.path.dirname(filepath)
    with zipfile.ZipFile(filepath) as zf:
        zf.extractall(dirpath)
    os.remove(filepath)


def untargz(filepath):
    print("Extracting: " + filepath)
    dirpath = os.path.dirname(filepath)
    with tarfile.open(filepath, "r:gz") as tf:
        tf.extractall(dirpath)
    os.remove(filepath)


def download_tagger(dirpath):
    tagger_dir = 'stanford-tagger'
    if os.path.exists(os.path.join(dirpath, tagger_dir)):
        print('Found Stanford POS Tagger - skip')
        return
    url = 'http://nlp.stanford.edu/software/stanford-postagger-2015-01-29.zip'
    filepath = download(url, dirpath)
    with zipfile.ZipFile(filepath) as zf:
        zip_dir = zf.namelist()[0]
        zf.extractall(dirpath)
    os.remove(filepath)
    os.rename(os.path.join(dirpath, zip_dir), os.path.join(dirpath, tagger_dir))


def download_easyccg(dirpath):
    dir = 'easyccg'
    path = os.path.join(dirpath, dir)
    if os.path.exists(path):
        print('Found easyccg - skip')
        return
    os.mkdir(path)

    url = 'https://github.com/mikelewis0/easyccg/raw/master/easyccg.jar'
    download(url, path)

    url = 'https://dl.dropboxusercontent.com/s/4h52nnn81jb6nf9/model.zip'
    filepath = download(url, path)
    unzip(filepath)


def download_parser(dirpath):
    parser_dir = 'stanford-parser'
    if os.path.exists(os.path.join(dirpath, parser_dir)):
        print('Found Stanford Parser - skip')
        return
    url = 'http://nlp.stanford.edu/software/stanford-parser-full-2015-01-29.zip'
    filepath = download(url, dirpath)
    zip_dir = ''
    with zipfile.ZipFile(filepath) as zf:
        zip_dir = zf.namelist()[0]
        zf.extractall(dirpath)
    os.remove(filepath)
    os.rename(os.path.join(dirpath, zip_dir), os.path.join(dirpath, parser_dir))


def download_wordvecs(dirpath):
    if os.path.exists(dirpath):
        print('Found Glove vectors - skip')
        return
    else:
        os.makedirs(dirpath)
    url = 'http://nlp.stanford.edu/data/glove.840B.300d.zip'
    unzip(download(url, dirpath))


def download_django(dirpath):
    if os.path.exists(dirpath + '/en-django'):
        print('Found django dataset - skip')
        return

    url = 'http://ahclab.naist.jp/pseudogen/en-django.tar.gz'
    filename = download(url, dirpath)
    untargz(filename)


def download_bs(dirname):
    if os.path.exists(dirname):
        print('Found BS dataset - skip')
        return

    cmd = ('git clone https://github.com/EdinburghNLP/code-docstring-corpus %s' % dirname)
    os.system(cmd)


def download_hs(dirname):
    if os.path.exists(dirname):
        print('Found HS dataset - skip')
        return

    cmd = ('git clone https://github.com/tsdaemon/card2code %s' % dirname)
    os.system(cmd)


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # data
    data_dir = os.path.join(base_dir, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    wordvec_dir = os.path.join(data_dir, 'glove')

    # libraries
    lib_dir = os.path.join(base_dir, 'lib')

    # download dependencies
    download_tagger(lib_dir)
    download_parser(lib_dir)
    download_easyccg(lib_dir)
    download_wordvecs(wordvec_dir)

    # download data
    download_hs(data_dir + '/card2code')
    #download_bs(data_dir + '/code-docstring-corpus')
    download_django(data_dir)
