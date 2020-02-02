from django.core.exceptions import ValidationError
from django.db.models import Count
from django.forms import ModelForm

from social.models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'

    def clean(self):
        # TODO переделать этот костыль!
        attributes = self.cleaned_data['attribute']
        if attributes.count() != attributes.aggregate(Count('level', distinct=True))['level__count']:
            raise ValidationError('Attributes cannot be at the same level')
        return self.cleaned_data
