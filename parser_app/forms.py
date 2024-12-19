from django import forms
from . import models, paser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka', 'rezka'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            "media_type"
        ]
    def parser_data(self):
        if self.data['media_type'] == 'rezka':
            rezka_file = paser_rezka.parsing()
            for i in rezka_file:
                models.RezkaModel.objects.create(**i)
        