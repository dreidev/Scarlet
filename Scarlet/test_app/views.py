from models import Article
from django.views.generic import DetailView


class ArticleDetailView(DetailView):

    model = Article
    template_name = "test_app/article_detail.html"
