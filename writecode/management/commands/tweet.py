from django.core.management.base import BaseCommand, CommandError
from writecode.models import Word
from secret import ckey, cseckey, access_token, access_token_sec, top_range, mid_range
import random
from twython import Twython

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

class Command(BaseCommand):

    def handle(self, *args, **options):
        #Setup Twython
        APP_KEY = ckey
        APP_SECRET = cseckey
        OAUTH_TOKEN = access_token
        OAUTH_TOKEN_SECRET = access_token_sec
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        twc = ''
        while len(twc) < 1 or len(twc) > 140:
            coders = list(Word.objects.filter(word_type = "C"))
            adjs = list(Word.objects.filter(word_type = "A"))
            phrases = list(Word.objects.filter(word_type = "P"))
            rand_coder = random.sample(coders, 2)
            rand_adj = random.sample(adjs, 4)
            rand_phrase = random.sample(phrases, 2)
            rand_pronoun = random.sample(range(1,101), 2)

            twc = (pronoun(rand_pronoun[0]) + article(rand_adj[0].words) + rand_adj[0].words + " " + 
                rand_adj[1].words + " " + rand_coder[0].words + " " + rand_phrase[0].words + " " + 
                pronoun(rand_pronoun[1]) + article(rand_adj[2].words) + rand_adj[2].words + " " + rand_adj[3].words +
                 " " + rand_coder[1].words + " " + rand_phrase[1].words + " #theywritecode")
            print (twc + " is " + str(len(twc)) + " char long.")


        print ("FINAL: " + twc + " is " + str(len(twc)) + " char long.")
        twitter.update_status(status=twc)
