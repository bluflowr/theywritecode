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
word_conversion = {
    'C': 'Coder',
    'A': 'Adjective',
    'P': 'Phrase',
    }
def alias_field(obj):
    return (word_conversion[obj.word_type])
alias_field.short_description = 'Types'

class WordAdmin(admin.ModelAdmin):
    form = WordAdminForm
    list_display=('words', alias_field)
    list_filter = ['word_type']
    admin_order_field = 'word_type'


admin.site.register(Word, WordAdmin)