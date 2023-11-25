#!/usr/bin/env python3

def return_evens(num_list):
    num_events = [num for num in num_list if num % 2 == 0]
    return num_events

def make_exclamation(sentence_list):
    exclamation_sentence = [sentence + '!' for sentence in sentence_list ]

    return exclamation_sentence 