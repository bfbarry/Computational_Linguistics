# import sys, os
# sys.path.append('../')

from utils.cleaning import int2rom
from nltk.corpus import wordnet, words
import nltk
import re

def load_odyssey():
    ''' 
    removes newlines, apostrophes (and their possessive cases, e.g. 's'), single quotes, chapter numbers
    '''
    with open('/Users/brianbarry/nltk_data/odyssey_original.txt','r') as f:
        start_, stop_ = 'Book I', 'FOOTNOTES' #'End of the Project'
        text = f.read()
        #removing Book followed by roman numerals (except V doesn't work??)
        text = re.sub(f'Book ({"|".join(list(map(int2rom,range(1,24))))})', ' ', text[text.index(start_):text.index(stop_)])
        text = re.sub("\n|\r|[()]|\[|\]|\{|\}|[\d-]|[.!?\\-]|'", " ", text) #this strips single quotes, add [A-Z][A-Z]+| to ineffectively remove all caps words
        #regex = re.compile('[^a-zA-Z]') #Too slow!
        #text = regex.sub('', text)
        text_words = list(map(str.lower, nltk.word_tokenize(text))) #or could just use list comp
        [text_words.remove(i) for i in text_words if i == '--' or i == 's']
        text_sents = list(map(str.lower, nltk.sent_tokenize(text)))
        return text_words, text_sents