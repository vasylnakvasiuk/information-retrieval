import os
import sys
import pickle
import csv

import nltk


def save_words_to_binary_file(words, filename):
    # Its important to use binary mode
    with open(filename, 'ab') as f:
        pickle.dump(words, f)

def save_words_to_csv_file(words, filename):
    with open(filename, 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(words)

def convert_text_to_terms(text):
    words = []
    for word in nltk.word_tokenize(text.lower()):
        if word.isalnum():
            words.append(word)
    return words

def main():
    for dirpath, _, fnames in os.walk("../samples"):
        for fname in fnames:
            abspath = os.path.join(dirpath, fname)
            with open(abspath) as f:
                words_in_file = []
                for line in f.readlines():
                    words_in_file.extend(convert_text_to_terms(line))

                save_words_to_binary_file(
                    words_in_file, '../results/result-{}.pickle'.format(fname)
                )
                save_words_to_csv_file(
                    words_in_file, '../results/result-{}.csv'.format(fname)
                )
                print(
                    'Words dict of file "{}" has {} words and {} bytes.'.format(
                        fname, len(words_in_file), sys.getsizeof(words_in_file)
                    )
                )

if __name__ == '__main__':
    nltk.download('punkt')
    main()
