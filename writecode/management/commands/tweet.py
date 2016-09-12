from django.core.management.base import BaseCommand, CommandError
from writecode.models import Word
from writecode.views import pronoun, article, random_sentence
from secret import ckey, cseckey, access_token, access_token_sec, top_range, mid_range
import random
from twython import Twython

class Command(BaseCommand):

    def handle(self, *args, **options):
        #Setup Twython
        APP_KEY = ckey
        APP_SECRET = cseckey
        OAUTH_TOKEN = access_token
        OAUTH_TOKEN_SECRET = access_token_sec
        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        sentence = ''
        while len(sentence) < 1 or len(sentence) > 140:
            sentence = random_sentence
            sentence = sentence() + " #theywritecode"

        twitter.update_status(status=sentence)
