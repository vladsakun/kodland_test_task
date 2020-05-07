from django.conf.urls import url

from main import views

urlpatterns = [
    url(r'^$', views.ShowPosts.as_view(), name='show_posts'),
    url(r'^create/post/$', views.create_post),
]
