#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Article(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=256, unique=True)
    text = models.TextField(max_length=5012)
    source = models.CharField(max_length=64)
    photo = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(
            default=timezone.now)

    def __unicode__(self):
        return self.title

class Comment(models.Model):
	article = models.ForeignKey(Article, related_name='comments')
	author = models.CharField(max_length=64)
	text = models.TextField(max_length=1028)
	created_date = models.DateTimeField(
            default=timezone.now)