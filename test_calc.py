# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:42:54 2022

@author: JackL


"""

from langcalc import ari


 

def test_sentcount():
    #this tests that the function to count number of sentences using full stops works
    s1 = '''I am an invisible man. No, I am not a spook like those who haunted Edgar Allan Poe; 
    nor am I one of your Hollywood-movie ectoplasms''' 
    s2 = '''I am an invisible man. No. I am not a spook like those who haunted Edgar Allan Poe; 
    nor am I one of your Hollywood-movie ectoplasms'''
    assert ari(s1) != ari(s2) 
    
    
def test_spacecount():
    #this tests that the inclusion of extra spaces does not affect the score as it should count non-space characters only
    s1 = 'When I went to the shop, I waved to the neighbour at number 45.'
    s2 = 'When I went to the shop,    I waved to the neighbour at number 45.'
    assert ari(s1) == ari(s2)
    
    
def test_charcount():
    #this tests that the inclusion of extra punctuation does not affect the score
    s1 = '''I am an invisible man. No, I am not a spook like those who haunted Edgar Allan Poe; 
    nor am I one of your Hollywood-movie ectoplasms'''
    s2 = '''I am an invisible man. No, I am not a 'spook' like those who haunted Edgar Allan-Poe; 
    nor am I one of your Hollywood-movie ectoplasms''' 
    assert ari(s1) == ari(s2) 
    

def test_nosent():
    #this tests that the function to count 1 sentence if there are no stops works
    s = 'When I went to the shop, I waved to the neighbour at number 45'
    assert ari(s)[0] == 2
    
     
def test_minusindex():
    s = 'I am going in the red car today and the sun is very hot, it will be fun.'
    # check score for a simple sentence is at min boundary for mapping to age bracket
    assert ari(s)[0] == 1
    
#def test_max_wordlength():
#    textvalue = '''Nice work man.'''
    #wordlist = textvalue.split()
    #for word in wordlist:
    #    wordlength = len(word)
    #maxwordlen = max(wordlength)
#    score = ari(textvalue)
    #print(score, maxwordlen)
    #if maxwordlen > 10:
#    assert score >= 10     
        

# def test_charcount2():
#    s = '41 42 43 44 45.'
#    s = '....' 
#    word_list = s.split()
#    # count non-space characters
#    #character_count = 0
    #for word in word_list:
    #    character_count += len(word)
    #assert character_count == 4     
    


    