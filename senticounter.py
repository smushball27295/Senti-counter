# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:38:27 2020

@author: aryan
"""

def loadlexicon(fname): #Creating a function to load the lexicons 
    new_lex=set()
    lex_conn=open(fname)
    #add every word in the file to the set
    for line in lex_conn:
        new_lex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return new_lex

def run(path):
    dic={}
    negLex=loadlexicon('negative-words.txt')
    f=open(path)
    for line in f:  
        
        line=line.lower().strip()   
        words=line.split(' ') 
        
        for i,word in enumerate(words): #for every word in the review
            if word in negLex and i == len(words)-1: # if the word is in the negative lexicon
                dic[word] = dic.get(word,0) +1 #update the negative list for this review
                print(dic)
            elif word in negLex:
                dic[word] = dic.get(word,0)           
   

        
    f.close()
    return dic            


if __name__ == "__main__": 
    dic=run('textfile')
    for x in dic:
        print([x,dic.get(x)])
    
    
