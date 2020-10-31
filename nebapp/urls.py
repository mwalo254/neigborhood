from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField


urlpatterns=[
    url(r'^$', views.welcome, name="welcome"),
    url(r'^profile/$', views.user_profile, name='user-profile'),
    url(r'^edit/profile/$', views.edit_profile, name="edit-profile"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/hood$', views.create_hood, name='new-hood'),
    # url(r'^updatehood/(\d+)$', views.update_hood, name='update-hood'),
    # url(r'^deletehood/(\d+)$', views.delete_hood, name='delete-hood'),
    # url(r'^joinhood/(\d+)$', views.join, name='join-hood'),
    url(r'^addbusiness/(\d+)$', views.new_bussiness, name='new-business'),
    # url(r'^exithood/(\d+)$', views.exit_hood, name='exit-hood'),
    url(r'^addpost/(\d+)$', views.new_post, name='new-post'),
    url(r'^location$', views.location, name='location'),
    url(r'^myhood/(\d+)', views.my_hood, name='my-hood'),
    url(r'^comment/(\d+)',views.new_comment, name='new-comment'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)