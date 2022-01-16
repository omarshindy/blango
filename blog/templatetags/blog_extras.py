from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from blog.models import Post

# regestring template library

register = template.Library()

# getting the user data
user_model = get_user_model()

# adding custom filter to author data
@register.filter
def author_details(author, current_user):
  if not isinstance(author, user_model):
    return ""


  if author == current_user:
    return format_html("<strong>ME</strong>")

  if author.first_name and author.last_name:
    name = f"{author.first_name}  {author.last_name}"

  else:
    name = f"{author.username}"

  if author.email :
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix  = format_html("</a>")
  
  else:
    prefix = ""
    suffix = ""

  return format_html("{} {} {}", prefix, name, suffix)

# Adding custom filter to Post data 
@register.inclusion_tag("blog/post_list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}

    
# Adding ustom template tags

@register.simple_tag
def row(extra_classes = ""):
    return format_html('<div class="row">', extra_classes)


@register.simple_tag
def enddiv():
    return format_html("</div>")

@register.simple_tag
def col(extra_classes = ""):
    return format_html('<div class="col">', extra_classes)


