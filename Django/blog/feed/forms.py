from django import forms
from django.core.exceptions import ValidationError
from .models import Post, Tag


class TagForm(forms.Form):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError("slug cannot be 'create'")
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('slug must be unique, {} slug is already exists'.format(new_slug))
        return new_slug

    
class PostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tag', 'date_pub']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tag': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError("slug cannot be 'create'")
        return new_slug
