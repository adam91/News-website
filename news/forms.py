#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django import forms
from .models import *

class ArticleForm(forms.ModelForm):
    category = forms.ModelChoiceField(label='Kategoria', queryset=Category.objects.all())
    title = forms.CharField(label='Tytuł')
    text = forms.CharField(label='Treść', widget=forms.Textarea)
    source = forms.CharField(label='Źródło')
    photo = forms.ImageField(label='Zdjęcie')

    class Meta:
        model = Article
        fields = ('category', 'title', 'text', 'source', 'photo')

class CommentForm(forms.ModelForm):
	author = forms.CharField(label='autor')
	text = forms.CharField(label='', widget=forms.Textarea)

	class Meta:
		model = Comment
		fields = ('text', 'author')