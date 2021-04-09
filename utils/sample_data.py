# import sys, os
# sys.path.append('../')

from utils.cleaning import int2rom
from nltk.corpus import wordnet, words
import nltk
import re

def load_odyssey():
    ''' '''
    with open('/Users/brianbarry/nltk_data/odyssey_original.txt','r') as f:
        start_, stop_ = 'Book I', 'FOOTNOTES' #'End of the Project'
        text = f.read()
        #removing Book followed by roman numerals (except V doesn't work??)
        text = re.sub(f'Book ({"|".join(list(map(int2rom,range(1,24))))})', ' ', text[text.index(start_):text.index(stop_)])
        text = re.sub("\n|\r|'", " ", text) #this strips single quotes, add [A-Z][A-Z]+| to ineffectively remove all caps words
        text_words = list(map(str.lower, nltk.word_tokenize(text)))
        text_sents = list(map(str.lower, nltk.sent_tokenize(text)))
        return text_words, text_sents