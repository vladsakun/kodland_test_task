from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from main.forms import PostForm
from main.models import Post

# Main page with all posts
class ShowPosts(ListView):
    queryset = Post.objects.order_by('-post_date')
    template_name = 'posts.html'
    context_object_name = 'posts'

# Create post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post_name = form.cleaned_data.get("post_name")
            post_text = form.cleaned_data.get("post_text")
            post_image = form.cleaned_data.get("post_image")
            obj = Post(post_name=post_name,
                       post_text=post_text,
                       post_image=post_image)
            obj.save()
            # On success redirect on main page
            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})
