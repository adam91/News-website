from django.conf.urls import url
from news import views
from django.conf import settings
from django.conf.urls.static import static
import os.path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#media_dir = os.path.join(os.path.dirname(__file__),'media')

urlpatterns = [
    #url(r'^media/(.*)$',static.serve,{'document_root': media_dir}),
    url(r'^$', views.all_articles, name='all_articles'),
    url(r'^articles$', views.all_articles, name='all_articles'),
    url(r'^article/new/$', views.article_new, name='article_new'),
    url(r'^category/(?P<category_id>.*)$', views.category, name='category'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail, name='article_detail'),
    url(r'^article/(?P<pk>[0-9]+)/comment/$', views.comment_new, name='comment_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
