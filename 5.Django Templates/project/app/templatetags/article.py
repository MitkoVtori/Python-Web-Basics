from django import template
from project.app.models import Article


register = template.Library()


@register.inclusion_tag('tags/articles.html', name='articles')
def show_articles():
    articles = Article.objects.all()
    return {'articles': articles}

