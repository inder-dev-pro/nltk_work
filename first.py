import nltk
from nltk.corpus import treebank
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('treebank')
sentence= """ At eight o'clock on Thursday morning Arthur didn't feel very good"""
tokens=nltk.word_tokenize(sentence)
tagged=nltk.pos_tag(tokens)
t=treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()