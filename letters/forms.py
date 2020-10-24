from django.forms import ModelForm
from . models import Letter

class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = ('text', )

    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)
        self.fields['text'].widget.attrs.update({'class' : 'textarea', 'placeholder' : 'What\'s in your mind?'})