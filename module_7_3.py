# coding: utf8
class WordsFinder:
    def __init__(self, *args: str):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, encoding='utf-8')as opened_file:
                words_list = []
                for line in opened_file:
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        if symbol in line:
                            if symbol == ' - ':
                                line = line.replace(symbol, ' ')
                                continue
                            line = line.replace(symbol, '')
                    words = line.lower().split()
                    for word in words:
                        words_list.append(word)
            all_words.update({f'{file}': words_list})
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for key, value in all_words.items():
            position = 1
            for obj in value:
                if obj == word.lower():
                    result.update({key: position})
                    break
                position += 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for key, value in all_words.items():
            count = 0
            for obj in value:
                if obj == word.lower():
                    count += 1
            if count > 0:
                result.update({key: count})
        return result
