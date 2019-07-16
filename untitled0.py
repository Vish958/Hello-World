# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:57:08 2019

@author: Vishwesh
"""

print ("Hello Vishwesh")
print ("Hey i wanted to looking for a python devloper")
    name = input('Enter File':)
    handle = open (name,'r')
    counts = dict ()
    
    for line in handle:
    words = line.split()
    for words in words
         counts[word] = counts.get(word,0)+ 1
         
    bigcount =None 
    bigword = word 
        for word, count in list(counts.item()):
            if bigcount is none or count > bigcount:
                bigword = word
                bigcount = count 
                
    print(bigword,bigcount)
    
    
    print ("Enter the word");
    
    