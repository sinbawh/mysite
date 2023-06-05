from django.shortcuts import render , get_object_or_404
from blog.models import Post
import datetime
import pytz

def home_view(request):
    current_time = datetime.now( pytz.timezone('Asia/Tehran'))
    posts = Post.objects.filter(published_date__lte=current_time)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html' , context)

def single_view(request , pid):
    post = get_object_or_404(Post , pk=pid , status = 1)
    context = {'post' : post}
    #Counting the number of views
    Counting = Post.objects.get(id = pid)
    Counting.counted_views = Counting.counted_views + 1
    Counting.save()

    return render(request, 'blog/blog-single.html' , context)

