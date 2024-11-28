#!/usr/bin/env python3

def return_evens(num_list):
    even = [num for num in num_list if num % 2 ==0]
    return even
    pass

def make_exclamation(sentence_list):
    modified = [objects + "!" for objects in sentence_list]
    return modified
    pass