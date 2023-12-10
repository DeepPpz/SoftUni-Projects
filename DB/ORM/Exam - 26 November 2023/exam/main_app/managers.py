from django.db import models



class AuthorManager(models.Manager):
    
    def get_authors_by_article_count(self):
        return self.annotate(count=models.Count('articles_authors')).order_by('-count', 'email')
