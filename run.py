# coding=utf-8
from newsmonitorq1.search_news import SearchNews


def _get_file_name():
    return raw_input("Enter the file name (absolute path) or press enter to read the default file: ")


def main():
    not_valid_file = True
    while not_valid_file:
        filename = _get_file_name()
        try:
            search_news = SearchNews(filename)
            not_valid_file = False
        except IOError:
            print 'It could not open the file [%s]. Please make sure this file exist or try another file.\n' % filename
        except:
            print 'Sorry something went wrong, please try again'

    while True:
        print '--------------------------------------\n'
        word = raw_input("Enter the word you want to search or press enter to quit: ")
        if word:
            search_news.print_titles_by_key_word(word)
        else:
            print 'Closing the program...'
            exit()

if __name__ == "__main__":
    main()




