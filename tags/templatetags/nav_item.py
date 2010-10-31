from django import template


register = template.Library()

@register.simple_tag
def nav_item(request, title, link):
    if request.path == link:
        return '<span class="nav-item">%s</span>' % title
    else:
        return '<a href="%s">%s</a>' % (link, title)
