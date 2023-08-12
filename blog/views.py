from django.shortcuts import render , get_object_or_404 , redirect
from blog.models import Post , Comment
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
import datetime
import pytz
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect


    
    

def home_view(request , **kwargs):
    current_time = datetime.datetime.now( pytz.timezone('Asia/Tehran'))
    posts = Post.objects.filter(published_date__lte=current_time)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'] )
    
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])

    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts , 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)    
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html' , context)

def single_view(request , pid  ):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment was successfully')
        else:
            messages.add_message(request,messages.ERROR,'Invalid comment')


    
    post = get_object_or_404(Post , pk=pid , status = 1 )


    #require of login of user
    if not post.login_require:

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

        comments = Comment.objects.filter(post=post.id , approved = True).order_by('-created_date')

        form = CommentForm()
        context = {'post' : post , 'prev_post' : prev_post , 'next_post' : next_post , 'comments' : comments , 'form':form}

            

        #Counting the number of views
        post.counted_views = post.counted_views + 1
        post.save()


        return render(request, 'blog/blog-single.html' , context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):

            posts= posts.filter(content__contains=s)
    
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)