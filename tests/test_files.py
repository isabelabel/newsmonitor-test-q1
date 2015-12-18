# coding=utf-8
from unittest import TestCase
from newsmonitorq1.files import read_file_by_lines

TESTS_BASE_PATH = "tests/files"


def get_file_name(filename):
    return "{base}/{name}".format(base=TESTS_BASE_PATH, name=filename)


class FilesTest(TestCase):

    def test_existent_file(self):
        lines = read_file_by_lines(get_file_name("titles_tests.txt"))

        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0], 'Frase 1 contendo a palavra frase mais de uma vez')
        self.assertEqual(lines[1], 'Frase 2 repetindo o número 2 e testando acentos a')
        self.assertEqual(lines[2], 'Frase 3 sem conteúdo repetido')

    def test_file_with_empty_line(self):
        lines = read_file_by_lines(get_file_name("file_with_empty_line.txt"))

        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], 'Frase 1')
        self.assertEqual(lines[1], 'Frase 2 repete frase')

    def test_file_not_exist(self):
        self.assertRaises(IOError, read_file_by_lines, get_file_name("not_exist.txt"))
