from django import forms
from .models import Word

WORD_TYPES = (
    ('C', 'Coder'),
    ('A', 'Adjective'),
    ('P', 'Phrase'),
    )

class WordAdminForm(forms.ModelForm):
    word_type = forms.ChoiceField(widget=forms.RadioSelect, choices = WORD_TYPES)

    class Meta:
        model = Word
        fields = '__all__'

    def clean_word(self):
        word_type = self.cleaned_data['word_type']
        if not word_type:
            raise forms.ValidationError("...")

        if len(word_type) > 2:
            raise forms.ValidationError("...")
        return word_type

