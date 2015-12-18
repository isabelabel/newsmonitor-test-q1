# coding=utf-8


def read_file_by_lines(filename):
    with open(filename) as f:
        return filter(None, f.read().splitlines())



