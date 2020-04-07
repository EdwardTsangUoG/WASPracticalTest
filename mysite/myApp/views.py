from django.http import HttpResponse
from django.template import loader
from .models import newsArticle

def index(request):
    list_of_articles = newsArticle.objects.order_by('-pub_date')
    template = loader.get_template('myApp/index.html')
    context = {
        'list_of_articles' : list_of_articles,
    }
    return HttpResponse(template.render(context, request))
    