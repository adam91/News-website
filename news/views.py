#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

def all_articles(request):
    articles = Article.objects.all().order_by('-created_date')
    return render(request, 'news/all_articles.html', {'articles' : articles})
	
def all_comments(request):
	comments = Comment.objects.all().order_by('-created_date')
	return render(request, 'news/all_comments.html', {'comments' : comments})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})

def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            form.save_m2m()
            return redirect(article_detail, pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'news/article_new.html', {'form': form})

def all_articles(request):
    articles = Article.objects.all().order_by('-created_date')
    return render(request, 'news/all_articles.html', {'articles' : articles})
	
def category(request, category_id):
    articles = Article.objects.filter(category__id__exact=category_id).order_by('-created_date')
    return render(request, 'news/category.html', {'articles': articles})

def comment_new(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(article_detail, pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'news/comment_new.html', {'form': form})
