import io
from pprint import pprint

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.tfu = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words_list = []
                for line in file:
                    for symbol in self.tfu:
                        line = line.replace(symbol, '')
                    words = line.lower().split()
                    words_list.extend(words)
                all_words[name] = words_list
        return all_words


    def find(self, word):
        dict_w = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_w[name] = words.index(word.lower()) + 1
                return dict_w

    def count(self, word):
        dict_w = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_w[name] = words.count(word.lower())
                return dict_w



finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
