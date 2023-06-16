from django.shortcuts import render , get_object_or_404
from blog.models import Post
import datetime
import pytz


    
    

def home_view(request):
    current_time = datetime.datetime.now( pytz.timezone('Asia/Tehran'))
    posts = Post.objects.filter(published_date__lte=current_time)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html' , context)

def single_view(request , pid  ):
    post = get_object_or_404(Post , pk=pid , status = 1 )

    #serching for next post
    if Post.objects.filter( status = 1 , id__gt = post.pk).exists():
        next_posts = Post.objects.filter( status = 1 , id__gt = post.pk).values_list('id', flat=True)
        next_post = Post.objects.get(id = next_posts[0])
    else:
        next_post = None

    #Serching for previous post
    if Post.objects.filter (id__lt = post.pk , status = 1).exists():
        prev_posts_id = Post.objects.filter(id__lt = post.pk , status = 1).values_list("id" , flat=True)
        
        prev_post =Post.objects.get(id = prev_posts_id.__len__())
    else:
        prev_post = None

    context = {'post' : post , 'prev_post' : prev_post , 'next_post' : next_post}

    

    #Counting the number of views
    post.counted_views = post.counted_views + 1
    post.save()


    return render(request, 'blog/blog-single.html' , context)

