# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:42:54 2022

@author: JackL


"""
import string
from langcalc import ari

def test_sentcount():
    textvalue = '''I am an invisible man. No, I am not a spook like those who haunted Edgar Allan Poe; 
    nor am I one of your Hollywood-movie ectoplasms 
    I am a man of substance, of flesh and bone, fiber and liquids—and I might even be said to possess a mind 
    I am invisible, understand, simply because people refuse to see me'''
    sentence_count = textvalue.count('.')
    assert sentence_count == 1
    
    
def test_wordcount():
    textvalue = 'When I went to the shop, I said "Hello!" to the neighbour at number 45.'
    textvalue = textvalue.translate(str.maketrans('', '', string.punctuation))
    # split string into individual words
    word_list = textvalue.split()
    # count words
    word_count = len(word_list)
    assert word_count == 15
    
def test_charcount():
#    textvalue = '41 42 43 44 45.'
    textvalue = '....' 
    word_list = textvalue.split()
    # count non-space characters
    character_count = 0
    for word in word_list:
        character_count += len(word)
    assert character_count == 4
    
def test_minusindex():
    textvalue = 'I am going in the red car today.'
    score = ari(textvalue) 
    # check score is above min reading age
    assert score > 4
    
def max_wordlength():
    textvalue = '''absolutelement'''
    wordlist = textvalue.split()
    for word in wordlist:
        wordlength = len(word)
    maxwordlen = max(wordlength)
    score = ari(textvalue)
    print(score, maxwordlen)
    if maxwordlen > 10:
        assert  score >= 10   
        

        
    


    