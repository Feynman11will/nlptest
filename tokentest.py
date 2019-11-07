'''
@Author: your name
@Date: 2019-11-07 22:59:59
@LastEditTime: 2019-11-07 23:54:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \nlptest\token.py
'''
import nltk

from nltk.corpus import gutenberg

from pprint import pprint
from nltk.corpus import europarl_raw
# nltk.download('punkt')
# nltk.download('gutenberg')
nltk.download('europarl_raw')
alice  = gutenberg.raw(fileids = 'carroll-alice.txt')
sample = 'Go to command prompt(not necessarily command prompt. You can do it from IDLE also).\
                 Do an nltk.download() in the python interpreter and then download all-corpora and book.\
                      After you do this, run your program. It should work.'

# print(alice)

defaulttks = nltk.sent_tokenize
alice_scentences = defaulttks(text=alice)
# 2
german_txter = europarl_raw.german.raw(fileids='ep-00-01-17.de')
germeny = nltk.data.load(resource_url='tokenizers/punkt/german.pickle')
german_txts = germeny.tokenize(german_txter)
# pprint(german_txts[0:5])
# print(alice_scentences)
# 第三种使用的方法
tks= nltk.tokenize.PunktSentenceTokenizer()
a= tks.tokenize(sample)
# pprint(a)

'''
4 
'''
pt = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<![A-Z]\.)(?<=\.|\?|\!)\s'

tokenizer2 = nltk.tokenize.RegexpTokenizer(pattern = pt,gaps=True)
alices = tokenizer2.tokenize(alice)
pprint(alices)