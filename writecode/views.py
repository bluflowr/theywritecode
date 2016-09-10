from django.shortcuts import render

# from .models import Coder, Descriptor, Phrase
from .models import Word
from secret import top_range, mid_range
import random

# def new_plot(request):
#     rand_coder_ids = random.sample(range(1, Coder.objects.count()+1), 2)
#     rand_adj_ids = random.sample(range(1, Descriptor.objects.count()+1), 4)
#     rand_phrase_ids = random.sample(range(1, Phrase.objects.count()+1), 2)
#     coders = list(Coder.objects.filter(id__in=(rand_coder_ids)))
#     adjs = list(Descriptor.objects.filter(id__in=(rand_adj_ids)))
#     phrases = list(Phrase.objects.filter(id__in=(rand_phrase_ids)))
#     article1 = 'a' if adjs[0].vowel == False else 'an'
#     article2 = 'a' if adjs[2].vowel == False else 'an'
#     sentence = (
#         coders[0].pronoun + " " + article1 + " " + adjs[0].adjective + " " + 
#         adjs[1].adjective + " " + coders[0].coder_type + " " + phrases[0].phrase + ". " + 
#         coders[1].pronoun + " " + article2 + " " + adjs[2].adjective + " " + 
#         adjs[3].adjective + " " + coders[1].coder_type + " " + phrases[1].phrase + ". They write code!"
#     )    
#     return render(request, 'index.html', {'sentence' : sentence})

def pronoun(number):
    if number >= top_range:
        return "He's "
    elif number >= mid_range and number < top_range:
        return "One's "
    else:
        return "She's "

def article(word):
    vowels = ['a','e', 'i', 'o', 'u']
    if word[0] in vowels:
        return "an "
    else:
        return "a "


def new_plot(request):
    coders = list(Word.objects.filter(word_type = "C"))
    adjs = list(Word.objects.filter(word_type = "A"))
    phrases = list(Word.objects.filter(word_type = "P"))
    rand_coder = random.sample(coders, 2)
    rand_adj = random.sample(adjs, 4)
    rand_phrase = random.sample(phrases, 2)
    rand_pronoun = random.sample(range(1,101), 2)

    sentence = (pronoun(rand_pronoun[0]) + article(rand_adj[0].words) + rand_adj[0].words + " " + 
        rand_adj[1].words + " " + rand_coder[0].words + " " + rand_phrase[0].words + " " + 
        pronoun(rand_pronoun[1]) + article(rand_adj[2].words) + rand_adj[2].words + " " + rand_adj[3].words +
         " " + rand_coder[1].words + " " + rand_phrase[1].words + " They write code!")
    

    return render(request, 'index.html', {'sentence' : sentence})

