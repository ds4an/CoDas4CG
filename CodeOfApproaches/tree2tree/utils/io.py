import pickle
import subprocess


def deserialize_from_file(path):
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    return obj


def serialize_to_file(obj, path, protocol=pickle.HIGHEST_PROTOCOL):
    with open(path, 'wb') as f:
        pickle.dump(obj, f, protocol=protocol)


def send_telegram(msg):
    subprocess.run(['telegram-send', msg])

