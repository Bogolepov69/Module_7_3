class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='UTF-8') as file:
                for line in file:
                    line = line.lower()
                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(char, '')
                    words.extend(line.split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        found_words = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                found_words[name] = words.index(word)
        return found_words

    def count(self, word):
        word_count = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            word_count[name] = words.count(word)
        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('text')) # 3 слово по счёту
print(finder2.count('text')) # 4 слова teXT в тексте всего