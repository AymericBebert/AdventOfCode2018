import os

_orig_dir = os.path.dirname(os.path.realpath(__file__))


def resolve_path(*path):
    if isinstance(path, str) and path[0] == "/":
        return path

    return os.path.abspath(os.path.join(_orig_dir, "../", *path))


def get_input_path(fn):
    if not fn.endswith(".txt"):
        fn = fn + ".txt"
    return resolve_path("input", fn)
