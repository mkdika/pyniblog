from django.shortcuts import render
from .models import Post
from .blogsettings import BlogSetting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    posts = Post.objects.filter(release=True).order_by('-post_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, BlogSetting.post_per_page)

    try:
        page_posts = paginator.page(page)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    response_dict = {
        'posts': page_posts,
        'blog': BlogSetting
    }
    return render(request, 'blog/main.html', response_dict)


def post(request, permalink):

    post = Post.objects.filter(permalink=permalink)

    response_dict = {
        'post': post[0],
        'blog': BlogSetting
    }
    return render(request, 'blog/post.html', response_dict)
