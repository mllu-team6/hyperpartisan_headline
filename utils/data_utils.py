"""
Copy from utils/data_utils.py
This is a modified and slightly extended version of
https://github.com/HLTCHKUST/hyperpartisan-news-detection/blob/master/utils/data_utils.py
"""
from bs4 import BeautifulSoup as Soup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import re
import string
import torch
from urllib.parse import urlparse
import numpy as np

#####################
### preprocessing ###
#####################
FLAGS = re.MULTILINE | re.DOTALL
def re_sub(pattern, repl, text, flags=None):
    if flags is None:
        return re.sub(pattern, repl, text, flags=FLAGS)
    else:
        return re.sub(pattern, repl, text, flags=(FLAGS | flags))

def clean_txt(text,
              remove_stopwords=False, 
              remove_nonalphanumeric=True,
              use_number_special_token=True,
              remove_numbers=False):
    
    text = text.lower()
 
    text = re.sub(r"-", " ", text)
    text = re.sub(r"[a-zA-Z]+\/[a-zA-Z]+", " ", text)
    text = re.sub(r"\n", " ", text)


    if use_number_special_token:
        text = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", "numberplaceholder", text)  
    elif remove_numbers:
        text = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", "", text)
    
    if remove_stopwords:
        text = text.split()
        stops = set(stopwords.words("english"))
        text = [w for w in text if w not in stops]
        text = " ".join(text)
    
    # Remove URL
    text = re_sub(r"(http)\S+", "", text)
    text = re_sub(r"(www)\S+", "", text)
    text = re_sub(r"(href)\S+", "", text)
    # Remove multiple spaces
    text = re_sub(r"[ \s\t\n]+", " ", text)
    
    # remove repetition
    text = re_sub(r"([!?.]){2,}", r"\1", text)
    text = re_sub(r"\b(\S*?)(.)\2{2,}\b", r"\1\2", text)

    return text.strip()


def parse_xml(article):
    # get meta data
    id = article.get('id')
    date = article.get('published-at')
    title = article.get('title')

    # get external link info
    external_links, internal_count=[],0
    for link in article.find_all('a'):
        if str(link.get('type'))=='internal':
            internal_count+=1
        else:
            external_links.append(link.get('href'))

    # get actual text
    article_text = article.get_text()
    article_text = clean_txt(article_text)
    
    result = [id, {'date':date,'title':title, 'internal':internal_count, 'external':external_links, 'article_text':article_text}]
    return result

##########################################
### char-level RNN data pre-processing ###
##########################################
all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

# Find letter index from all_letters, e.g. "a" = 0
def letterToIndex(letter):
    return all_letters.find(letter)

# Just for demonstration, turn a letter into a <1 x n_letters> Tensor
def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor

# Turn a line into a <line_length x 1 x n_letters>,
# or an array of one-hot letter vectors
def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor