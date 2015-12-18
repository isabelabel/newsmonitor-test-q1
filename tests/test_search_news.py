# coding=utf-8
from unittest import TestCase
from newsmonitorq1.search_news import SearchNews, TitleCount

FILE_TEST = "tests/files/file_with_empty_line.txt"
# FILE_TEST = "files/file_with_empty_line.txt"


class SearchNewsTest(TestCase):
    def setUp(self):
        self.search_news = SearchNews(filename=FILE_TEST)

    def test_words_in_title_with_duplicated(self):
        result = SearchNews._words_in_title("Um teste um repetido")
        expected_result = {
            "um": 2,
            "teste": 1,
            "repetido": 1,
        }

        self.assertDictContainsSubset(expected_result, result)

    def test_words_in_title_without_duplicated(self):
        result = SearchNews._words_in_title("Uma frase sem conteúdo")
        expected_result = {
            "uma": 1,
            "frase": 1,
            "sem": 1,
            "conteúdo": 1
        }

        self.assertDictContainsSubset(expected_result, result)

    def test_sort_words_by_count(self):
        test_input = {
            "a": [TitleCount(title_index=0, count=1), TitleCount(title_index=1, count=4), TitleCount(title_index=2, count=3)],
            "b": [TitleCount(title_index=0, count=2), TitleCount(title_index=1, count=1)],
            "c": [TitleCount(title_index=0, count=2), TitleCount(title_index=2, count=5)]
        }
        result = self.search_news._sort_words_by_count(test_input)

        self.assertEqual(result["a"], [TitleCount(title_index=1, count=4), TitleCount(title_index=2, count=3), TitleCount(title_index=0, count=1)])
        self.assertEqual(result["b"], [TitleCount(title_index=0, count=2), TitleCount(title_index=1, count=1)])
        self.assertEqual(result["c"], [TitleCount(title_index=2, count=5), TitleCount(title_index=0, count=2)])

    def test_create_words_by_title(self):
        result = self.search_news._create_words_by_title()

        self.assertEqual(result["frase"], [TitleCount(1, 2), TitleCount(0, 1)])
        self.assertEqual(result["1"], [TitleCount(0, 1)])
        self.assertEqual(result["2"], [TitleCount(1, 1)])
        self.assertEqual(result["repete"], [TitleCount(1, 1)])

    def test_titles_by_key_word(self):
        result = self.search_news.titles_by_key_word("frase")

        self.assertEqual([('Frase 2 repete frase', 2), ('Frase 1', 1)], result)

