import markdown
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from blog.models import Post

register = template.Library()

# Built-in template tags and filters
# https://docs.djangoproject.com/en/5.2/ref/templates/builtins/
@register.simple_tag
def total_posts():
    """
    Returns the total number of blog posts.
    """
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """
    Returns the latest published blog posts.
    """
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# Aggregation
# https://docs.djangoproject.com/en/5.2/topics/db/aggregation/
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


# Writing custom template filters
# https://docs.djangoproject.com/en/5.2/howto/custom-template-tags/#writing-custom-template-filters
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
