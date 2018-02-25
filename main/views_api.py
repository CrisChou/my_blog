from main import models
from django.http import JsonResponse


def init_article(request):
    # article_model = models.Article
    pass



def request_article_type(request):
    article_type = models.Article.type_choices
    return JsonResponse({'data':article_type})
