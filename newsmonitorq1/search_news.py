# coding=utf-8
from newsmonitorq1.files import read_file_by_lines
from collections import defaultdict
from collections import namedtuple

TitleCount = namedtuple('TitleCount', 'title_index count')

DEFAULT_FILENAME = "files/news_titles.txt"


class SearchNews:
    def __init__(self, filename=None):
        self.__filename = filename or DEFAULT_FILENAME
        self.__titles = self.__init_titles()
        self.__words_by_titles = self._create_words_by_title()

    def __init_titles(self):
        return read_file_by_lines(self.__filename)

    def _create_words_by_title(self):
        w = {}
        w = defaultdict(lambda: [], w)
        for index, title in enumerate(self.__titles):
            for word, count in self._words_in_title(title).iteritems():
                w[word].append(TitleCount(index, count))

        return self._sort_words_by_count(w)

    @staticmethod
    def _words_in_title(title):
        words = defaultdict(int)
        for word in title.split():
            words[word.lower()] += 1

        return words

    @staticmethod
    def _sort_words_by_count(words_title_count):
        sorted_w = {}
        for word, title_count in words_title_count.iteritems():
            sorted_w[word] = sorted(title_count, key=lambda k: k.count, reverse=True)

        return sorted_w

    def titles_by_key_word(self, word):
        return map(lambda t: (self.__titles[t.title_index], t.count), self.__words_by_titles.get(word, []))

    def print_titles_by_key_word(self, word):
        titles = self.titles_by_key_word(word.strip().lower())
        if titles:
            print "Titles with the word [%s]: " % word
            for index, title_and_count in enumerate(titles, start=1):
                print "{position} - Title: \"{title}\". The searched word appeared [{count}] times"\
                    .format(position=index, title=title_and_count[0], count=title_and_count[1])
        else:
            print "There are not Titles with the word [%s]" % word
