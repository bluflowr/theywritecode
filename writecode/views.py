from django.shortcuts import render

from .models import Word
from secret import top_range, mid_range
import random

#Function to randomize pronouns
def pronoun(number):
    if number >= top_range:
        return "He's "
    elif number >= mid_range and number < top_range:
        return "One's "
    else:
        return "She's "

#Function to get correct article for adjectives
def article(word):
    vowels = ['a','e', 'i', 'o', 'u']
    if word[0] in vowels:
        return "an "
    else:
        return "a "

#Function to create a random sentence
def random_sentence(twc = ''):
    coders = list(Word.objects.filter(word_type = "C"))
    adjs = list(Word.objects.filter(word_type = "A"))
    phrases = list(Word.objects.filter(word_type = "P"))
    rand_coder = random.sample(coders, 2)
    rand_adj = random.sample(adjs, 2)
    rand_phrase = random.sample(phrases, 2)
    rand_pronoun = random.sample(range(1,101), 2)

    twc = (pronoun(rand_pronoun[0]) + article(rand_adj[0].words) + rand_adj[0].words + " " + 
        rand_coder[0].words + " " + rand_phrase[0].words + " " + 
        pronoun(rand_pronoun[1]) + article(rand_adj[1].words) + rand_adj[1].words +
         " " + rand_coder[1].words + " " + rand_phrase[1].words)
    return twc 


def new_plot(request):
    sentence = random_sentence
    return render(request, 'index.html', {'sentence' : sentence})

