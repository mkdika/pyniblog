from django.shortcuts import render
from .models import Post,Tag
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


def search(request, search_by, id):

    search = f"{search_by}: {id}"

    if search_by == 'users':
        posts = Post.objects.filter(user__username__contains=id).order_by('-post_date')
    elif search_by == 'categories':
        posts = Post.objects.filter(category__category_name__contains=id).order_by('-post_date')
    elif search_by == 'tags':
        tag = Tag.objects.get(tag_name=id)
        posts = Post.objects.filter(tags__in=[tag]).order_by('-post_date')

    response_dict = {
        'posts': posts,
        'search': search,
        'blog': BlogSetting,
        
    }
    return render(request, 'blog/search.html', response_dict)