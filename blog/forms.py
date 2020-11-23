from django import forms
from .models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.CharField(max_length=50)

    def clean_slug(self):
        new_slug = self.cleaned_slug['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug cant be create')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('fuck you'.format(new_slug))

        return new_slug

    def save(self):
        new_tag = Tag.objects.create(title=self.cleaned_data['title'],
                                     slug=self.cleanet_data['slug'])
        return new_tag


