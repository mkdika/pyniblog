from django.shortcuts import render
from .models import Post, Tag, PostComment
from .blogsettings import BlogSetting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# global response object for all pages
response_dict = {'blog': BlogSetting}


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

    response_dict.update({'posts': page_posts})
    return render(request, 'blog/main.html', response_dict)


def post(request, permalink):

    posts = Post.objects.filter(permalink=permalink)
    post = posts[0]
    comments = PostComment.objects.filter(post=post).order_by('-comment_date')

    response_dict.update({'post': post,'comments':comments})
    return render(request, 'blog/post.html', response_dict)


def search(request, search_by, id):

    search = f"{search_by}: {id}"

    if search_by == 'users':
        posts = Post.objects.filter(
            user__username__contains=id).order_by('-post_date')
    elif search_by == 'categories':
        posts = Post.objects.filter(
            category__category_name__contains=id).order_by('-post_date')
    elif search_by == 'tags':
        tag = Tag.objects.get(tag_name=id)
        posts = Post.objects.filter(tags__in=[tag]).order_by('-post_date')

    response_dict.update({ 'posts': posts,'search': search,})
    return render(request, 'blog/search.html', response_dict)


def about(request):

    return render(request, 'blog/about.html', response_dict)


def archive(request, mode):

    if mode == 'year':
        ar_mode = 'archive'
    elif mode == 'categories':
        ar_mode = mode

    posts = Post.objects.filter(release=True).order_by('-post_date')

    response_dict.update({'ar_mode':ar_mode,
                          'posts':posts})

    return render(request, 'blog/archive.html', response_dict)

