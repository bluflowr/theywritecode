from django.db import models

class Word(models.Model):
    words = models.CharField(max_length=200)
    word_type = models.CharField(max_length=5)

    def __str__(self):
        return self.words


# class Coder(models.Model):
#     coder_type = models.CharField(max_length=200)
#     pronoun = models.CharField(max_length=10)

#     def __str__(self):
#         return self.coder_type

# class Descriptor(models.Model):
#     adjective = models.CharField(max_length=100)
#     vowel = models.BooleanField(default=False)

#     def __str__(self):
#         return self.adjective   

#     def is_vowel(self):
#         if adjective[0] in ['a','e', 'i', 'o', 'u','y']:
#             Descriptor.vowel = True
#         else:
#             Descriptor.vowel = False


# class Phrase(models.Model):
#     phrase = models.CharField(max_length=200)

#     def __str__(self):
#         return self.phrase
