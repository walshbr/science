import gensim
import os
import nltk
import string
import csv


class Word2VecModel(object):
    def __init__(self, corpus='leipzig.txt'):
        # self.filenames = self.corpus_manifest(corpus_dir)
        # self.texts = self.read_files_from_folder(self.filenames)
        self.corpus = corpus
        self.sentences = self.read_sentences_from_corpus(self.corpus)
        self.model = self.produce_model(self.sentences)

    def read_sentences_from_corpus(self, corpus_dir):
        """Importer for the Leipzig newspaper corpus,
        which draws in a list of sentences."""
        with open(corpus_dir, 'r') as fin:
            reader = csv.reader(fin, delimiter='\t')
            raw_sents = [sent for _, sent in reader]
            sentences = [
                nltk.tokenize.word_tokenize(sent) for sent in raw_sents]
            sentences = [[token.lower() for token in sent if token not in
                          string.punctuation] for sent in sentences]
            return sentences

    def produce_model(self, sentences):
        return gensim.models.Word2Vec(
            sentences, size=100, window=5,
            min_count=5, sg=0, alpha=0.025,
            iter=5, batch_words=10000)

    def segment(texts):
        """Unused ATM
        Given a list of texts, return a list of sentences for each text."""
        sentences = [
            sentence for text in texts
            for sentence in nltk.tokenize.sent_tokenize(text)]
        words_by_sentence = [
            tokenize(sentence.lower()) for sentence in sentences]
        words_by_sentence = [
            sentence for sentence in words_by_sentence if sentence != []]
        return words_by_sentence

    def tokenize(text):
        """Unused.ATM
        Take a text and return a list of sentences."""

        punctuation_removed = "".join([
            char for char in text if char not in string.punctuation
            ])
        tokens = punctuation_removed.split()
        return tokens

    def corpus_manifest(corpus_dir):
        """Unused ATM
        Given a corpus directory, return a
        list of all the filenames in it."""
        texts = []
        for (root, _, files) in os.walk(corpus_dir):
            for fn in files:
                if fn[0] == '.':
                    pass
                else:
                    texts.append(os.path.join(root, fn))
        return texts

    def read_files_from_folder(filenames):
        """Unused ATM
        Given a list of filenames return texts"""
        texts = []
        for fn in filenames:
            with open(fn, 'r') as fin:
                texts.append(fin.read())
        return texts

    def chicken_nugget(self):
        print('produces a chicken_nugget')

def main():
    # leipzig = 'leipzig.txt'
    # # uncomment to read from corpus folder
    # # corpus = 'corpus/'
    # # filenames = corpus_manifest(corpus)
    # # texts = read_files_from_folder(filenames)
    # # sentences = segment(texts)
    # sentences = read_sentences_from_corpus(leipzig)
    # model = produce_model(sentences)
    # # w2v_model.wv.vocab now is the replacement for model.vocab
    # print(model.vocab)

    model = Word2VecModel()

if __name__ == '__main__':
    main()
