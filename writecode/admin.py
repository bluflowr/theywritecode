from django.contrib import admin
from django import forms

# from .models import Coder, Descriptor, Phrase
from .forms import WordAdminForm
from .models import Word

# class CoderInline(admin.TabularInline):
#     model = Coder

# class CoderAdmin(admin.ModelAdmin):
#     list_display=('coder_type', 'pronoun')

# admin.site.register(Coder, CoderAdmin)
# admin.site.register(Descriptor)
# admin.site.register(Phrase)

class WordAdmin(admin.ModelAdmin):
    form = WordAdminForm
    list_display=('words', 'word_type')

admin.site.register(Word, WordAdmin)