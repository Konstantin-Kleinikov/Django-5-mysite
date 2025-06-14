from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render

from blog.models import Post


def post_list(request):
    post_list = Post.published.all()
    # Page pagination with 3 Posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not a number then show the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page number is out of range, the go to last page:
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts},
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post},
    )
