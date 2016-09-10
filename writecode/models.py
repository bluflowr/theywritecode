from django.db import models

class Word(models.Model):
    words = models.CharField(max_length=200)
    word_type = models.CharField(max_length=5)

    def __str__(self):
        return self.words
